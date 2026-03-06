# Day 66 - Building a REST API with Flask and SQLAlchemy

Day 66 changes the role of the Flask app again. Instead of building pages primarily for a browser user, the application now exposes data endpoints that other clients can consume. The same API could be used by a frontend, a mobile app, a script, or a testing tool like Postman.

This lesson needs a solid amount of theory because REST APIs are one of the most important backend concepts in the course. HTTP methods, JSON serialization, query parameters, and status codes all matter here, and the code makes more sense when those ideas are explained directly.

## 1. The App Now Serves Data as JSON

The home route still renders a simple HTML page:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

But the main purpose of the project is in the data endpoints such as `/all`, `/random`, `/search`, `/add`, `/update-price/<id>`, and `/report-closed/<id>`.

That is the key shift. The app is now exposing resources rather than mainly rendering human-facing pages.

## 2. The Database Model Still Defines the Resource

The `Cafe` model describes the shape of the data the API works with:

```python
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
```

This is important because the API is not returning arbitrary dictionaries invented on the spot. It is exposing data that comes from a structured database model.

So the API layer still sits on top of the same persistence ideas from the earlier SQLAlchemy lessons.

## 3. Serialization Converts Model Objects into JSON-Friendly Data

A Python object cannot be sent directly over HTTP as an API response. It has to be converted into standard data types that JSON can represent.

That is what `to_dict()` does:

```python
def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}
```

This method is a nice teaching example because it automatically walks through the model columns and builds a dictionary from them. Once the model is converted into a plain dictionary, `jsonify()` can turn it into a proper JSON response.

This is one of the core API ideas in the course: backend models usually need a serialization step before they become HTTP response bodies.

## 4. `GET` Routes Read Resources

The app exposes several read-only endpoints. For example, `/all` returns every cafe:

```python
@app.route("/all")
def get_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
```

And `/random` returns one random record:

```python
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())
```

These routes illustrate a core REST idea: `GET` is for retrieval. The client asks for data, and the server returns a representation of the resource.

## 5. Query Parameters Let Clients Filter Results

The `/search` endpoint uses a query parameter:

```python
@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc").title()
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
```

This is useful because it shows another common API pattern. Not every input belongs in the path. When the client is filtering or narrowing a request, query parameters are often a better fit.

So a client can ask for:

`/search?loc=London`

and receive only matching records.

That is a small but important API-design distinction.

## 6. `POST` Creates New Records

The `/add` endpoint handles creation:

```python
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
```

This route is important because it makes the API writable. A client can send form data to the server, and the server turns that input into a new database record.

That is the core use of `POST` in REST-style design: create a new resource.

## 7. `PATCH` Updates Part of an Existing Resource

The `/update-price/<int:cafe_id>` endpoint is a nice example of partial updates:

```python
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
```

This is worth explaining because `PATCH` is different from `POST`. The client is not creating a new cafe. It is changing one field on an existing cafe.

That makes the endpoint a good example of how HTTP methods communicate intent, not just transport data.

## 8. `DELETE` Removes a Resource and Uses Simple Authorization

The delete route checks for an API key before removing a record:

```python
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def remove_cafe(cafe_id):
    api_key = request.headers.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"success": "Successfully deleted the cafe from the database."}), 200
```

This is a helpful early security lesson. An API endpoint that changes or deletes data should not necessarily be open to anyone who can reach the URL.

The protection here is simple, but it teaches the right instinct: destructive operations often need authorization checks.

## 9. Status Codes Help the Client Understand the Result

The API returns status codes alongside some responses:

```python
return jsonify(response={"success": "Successfully updated the price."}), 200
return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
return jsonify(error={"Access Denied": "Sorry, that's not allowed. Make sure you have the correct api-key."}), 403
```

This matters because a good API does not only return data. It also tells the client what happened in a standard HTTP way.

That gives clients two levels of information:

- the JSON body explains the result
- the status code explains the class of outcome

This becomes especially useful when different frontend clients or scripts need to handle success and failure differently.

## 10. The Lesson Is About Resource-Oriented Thinking

The strongest conceptual takeaway from Day 66 is that the app is no longer organized mainly around pages. It is organized around operations on a resource: cafes.

Clients can:

- fetch all cafes
- fetch one random cafe
- search cafes by location
- add a cafe
- patch a price
- delete a cafe

That is the core of resource-oriented API design. The routes and methods are describing what can happen to the resource.

## How to Run the Project

Install the required packages if needed:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```

The API runs on port `5001`, so try endpoints such as:

- `http://127.0.0.1:5001/all`
- `http://127.0.0.1:5001/random`
- `http://127.0.0.1:5001/search?loc=London`

Use a tool like Postman, Insomnia, or `curl` for the `POST`, `PATCH`, and `DELETE` routes.

## Summary

Day 66 turns the Flask app into a real web service. SQLAlchemy models still define the data, but the app now serializes records into JSON, exposes resource-oriented endpoints, and uses HTTP methods to express read, create, update, and delete behavior. The lesson is not just about returning JSON. It is about learning to think in terms of API resources, request methods, and client-server contracts.

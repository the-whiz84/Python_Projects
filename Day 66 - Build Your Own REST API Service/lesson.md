# I. RESTful API

# REST - REpresentational State Transfer

What does it mean to mane a RESTful API?
# REST is an architectural style for designing APIs
# SOAP was the dominant style before REST

# REST was invented in 2000 as a doctorate thesis by Thomas Fielding at University of California
- he came with the idea that all websites will use the same language for APIs
- it would be easy for everybody to work together and talk to each other

# The 2 most important rules for RESTful APIs are:
- use HTTP Request Verbs
- use Specific Pattern of Routes/Endpoint URLs

# 1. HTTP Verbs:
- GET
- POST
- PUT and PATCH (added in 2010)
- DELETE

# THey are similar to DB requests:
- Create
- Read
- Update
- Delete


# 2. Specific Pattern of Routes/Endpoint URLs

# RESTful Routing

# HTTP Verbs            /articles                   /articles/jack-bauer
    GET         Fetches all the articles        Fetches the article on jack-bauer
    POST        Creates one new article             -
    PUT                 -                       Updates the article on jack-bauer
    PATCH               -                       Updates the article on jack-bauer
    DELETE      Deletes all articles            Deletes the article on jack-bauer


# II. Creating an API with Flask

Given our database consists of a bunch of cafes to remote-work from, one of the likely use cases of our API is a developer who wants to serve up a random cafe for their user to go to. So let's create a /random route that serves up a random cafe.

1. Create a /random route in main.py that allows GET requests to be made to it.
2. When someone makes a GET request to the /random route, our Flask server should fetch a random cafe from our database.

Normally, we've been returning HTML templates using render_template(), but this time, because our server is now acting as an API, we want to return a JSON containing the necessary data. Just like real public APIs.

# In order to do this, we have to turn our random_cafe SQLAlchemy Object into a JSON. This process is called serialization.
# Flask has a serialisation helper method built-in called jsonify() . But we have to provide the structure of the JSON to return.

https://tedboy.github.io/flask/generated/flask.jsonify.html

# The method described in the docs has maximum flexibility. It allows you to have perfect control over the JSON response. e.g. You could also structure the response by omitting some properties like id. You could also group the Boolean properties into a subsection called amenities.
    return jsonify(cafe={
    #Omit the id from the response
    # "id": random_cafe.id,
    "name": random_cafe.name,
    "map_url": random_cafe.map_url,
    "img_url": random_cafe.img_url,
    "location": random_cafe.location,
    "coffee_price": random_cafe.coffee_price,
    "seats": random_cafe.seats,
    #Put some properties in a sub-category
    "amenities": {
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        }
    })

# But in most cases, you might just want to return all the data you have on a particular record and it would drive you crazy if you had to write out all that code for every route.
# So another method of serializing our database row Object to JSON is by first converting it to a dictionary and then using jsonify() to convert the dictionary (which is very similar in structure to JSON) to a JSON.

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
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

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())


# III. Difference between PUT and PATCH

# PUT updates the entire entry by replacing it with new values
# PATCH will update the entry with just the desired piece of data


# IV. Build Documentation for Your API (not available in VsCode extension)

If we want other people to use our API, then we have to document how to use it. 
People can't see the code on our servers, so we have to tell them how to interact with our servers via the API constraints.

e.g. What are the routes, what are the required parameters etc.

Luckily for us, if you made all your requests in Postman and you gave each request a name and description then Postman will generate the documentation automatically for you.

# 1. Make sure that you've made each of the requests and they work as you expect.

# 2. Make sure all the requests are saved in the same collection e.g. My collection is called Cafe & Wifi:

# 3. Click on the three dots next to your collection name and go to "Publish Docs":

# 4. Go through the steps to publish your documentation and this is what you should end up with:

# 5. We can now edit out index.html to include an anchor tag to our API's documentation.
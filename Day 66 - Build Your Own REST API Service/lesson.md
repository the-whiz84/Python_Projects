# Day 66 - Building Your Own REST API: Decoupling Data and Design

For the past two weeks, we have worked on "Monolithic" applications—where the Python logic and the HTML templates live in the same project. However, in the professional world, the **Backend** and **Frontend** are often entirely separate systems.

Today, we built a **REST API (REpresentational State Transfer)**. This is the bedrock of modern computing. Your API can simultaneously power a web React app, an iPhone app, and a Tesla dashboard, all using the exact same data endpoints.

## 1. What makes an API "RESTful"?

A true REST API follows six key constraints. Today, we focused on the three most important:

- **Statelessness**: The server doesn't remember anything about the client between requests. Every request must contain all the information needed to fulfill it (like an API Key).
- **Uniform Interface**: We use standard HTTP methods (GET, POST, PATCH, DELETE) to interact with resources (e.g., `/cafes`).
- **Resource-Oriented**: We don't have routes like `/get-all-cafes`. We have a resource `/cafes` and we use different "verbs" (methods) to decide what to do with it.

## 2. Serialization: Transforming Models into JSON

Our database stores `Cafe` objects. But we can't send a Python object across the internet. We must **Serialize** it—turn it into a universal format like **JSON (JavaScript Object Notation)**.

In `main.py`, we implemented a high-performance serialization method using **Python Dictionary Comprehension**:

```python
class Cafe(db.Model):
    # ...
    def to_dict(self):
        # Dynamically map internal columns to external JSON keys
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
```

By calling `jsonify(cafe=cafe.to_dict())`, we transform our complex database record into a simple text string that any programming language (JavaScript, Swift, Kotlin) can understand.

## 3. Mastering the HTTP Verbs: PATCH and Idempotency

A common mistake is using `POST` for everything. A professional REST API respects the "intent" of the HTTP method:

- **`GET`**: Fetches data. (Must be "Read-Only").
- **`POST`**: Creates a NEW resource.
- **`PATCH`**: Updates only a _part_ of a resource. (E.g., just changing the price).
- **`PUT`**: Replaces the _entire_ resource.
- **`DELETE`**: Removes the resource.

**Architectural Insight**: `GET`, `PUT`, and `DELETE` should be **Idempotent**. This means if you run the same request 100 times, the result is the same as running it once. `POST`, however, is **not** idempotent (running it 100 times creates 100 entries).

## 4. Security: API Keys and Status Codes

We implemented **Authentication** by checking for a "Secret" string in the request Headers:

```python
api_key = request.headers.get("api-key")
if api_key != "TopSecretAPIKey":
    return jsonify(error="Forbidden"), 403
```

We also utilized **Precise Status Codes**:

- `200 OK`: Successful read/update.
- `201 Created`: Successful POST.
- `403 Forbidden`: Authentication failure.
- `404 Not Found`: Trying to update a cafe that doesn't exist.

## How to Run the Cafe API

1.  **Dependencies**:
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```
2.  **Launch the Server**:
    ```bash
    python main.py
    ```
3.  **Testing with Postman/Insomnia**:
    - **GET** `http://127.0.0.1:5001/random`: Fetch a random cafe.
    - **PATCH** `http://127.0.0.1:5001/update-price/1?new_price=£3.50`: Update cafe #1.
    - **DELETE** `http://127.0.0.1:5001/report-closed/1`: (Must add `api-key` in the Headers section of Postman).

## Summary

Today, you stopped building "Websites" and started building "Web Services." You learned the six core principles of REST, mastered the art of JSON serialization, and understood how to use HTTP verbs and status codes to build a professional, secure data interface.

Tomorrow, we combine these RESTful principles with our HTML skills to build a **fully-featured, database-backed Blog with full CRUD editing!**

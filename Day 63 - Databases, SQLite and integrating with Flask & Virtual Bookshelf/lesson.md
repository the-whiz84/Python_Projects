# Day 63 - Relational Databases: The SQLAlchemy ORM Architecture

Yesterday, we learned that flat files (CSVs) are dangerous in multi-user web environments due to file locking and performance bottlenecks. Today, we leave the "flat file" world behind and migrate to a professional **Relational Database Management System (RDBMS)**: **SQLite**.

But we didn't just learn how to write SQL; we learned how to use an **Object Relational Mapper (ORM)** called **SQLAlchemy**. This is how senior engineers bridge the gap between Python's Object-Oriented nature and SQL's Set-Based nature.

## 1. The ORM Philosophy: Objects vs. Rows

In a standard database, you think in **Tables and Rows**. In Python, you think in **Classes and Objects**.
An ORM like SQLAlchemy maps these two worlds together:

- A **Class** (e.g., `Book`) maps to a **Table**.
- An **Instance** of that class (`harry_potter`) maps to a **Row**.
- An **Attribute** (`title`) maps to a **Column**.

This abstraction allows us to perform complex database operations without writing a single line of raw SQL string, which protects us from **SQL Injection** attacks and makes our code much easier to test.

## 2. Declarative Mapping: Defining the Schema

In `main.py`, we implemented the modern **Declarative Base** architecture:

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

class Book(db.Model):
    # This explicit type hinting provides IDE autocompletion and safety
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    # ...
```

By inheriting from `db.Model` (which uses our `Base`), SQLAlchemy can introspect our code and automatically generate the necessary `CREATE TABLE` commands.

## 3. The Unit of Work Pattern: Understanding the Session

One of the most common mistakes beginners make is forgetting to `commit()`. To understand why `db.session.add()` isn't enough, you must understand the **Unit of Work** pattern.

The `db.session` is like a "staging area" or a "shuttle" between your Python script and the database:

1.  **`db.session.add(obj)`**: You are telling the session: "I want this change to happen." The change lives in memory.
2.  **`db.session.commit()`**: The session sends all pending changes to the database at once in a single **Transaction**.

**Why do we do this?** Efficiency and Integrity. If you are adding 1,000 books, it is MUCH faster to commit them once at the end than to open 1,000 separate connections to the database.

## 4. The Identity Map Pattern

Have you ever wondered why, if you query for the same book twice, you get the exact same Python object?

```python
book1 = db.session.get(Book, 1)
book2 = db.session.get(Book, 1)
print(book1 is book2) # True!
```

This is the **Identity Map** pattern. SQLAlchemy tracks every object it fetches in the current session. This ensures that your application never has two conflicting "versions" of the same row in memory at the same time.

## 5. The Flask Application Context: `with app.app_context()`

You likely saw this block in your code:

```python
with app.app_context():
    db.create_all()
```

**Architectural Reason**: Flask is designed to handle thousands of concurrent requests. Because of this, the database extension needs to know _which_ application instance it is talking to. Since we are running the `create_all()` command outside of a standard web request, we must manually enter the "Application Context" so the DB knows where to find its configuration (like the URI).

## Running the Virtual Bookshelf

1.  **Set Up Dependencies**:
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```
2.  **Initialize the Database**:
    The script automatically creates an `instance/books.db` file when run. The "Instance" folder is where Flask stores project-specific data that shouldn't typically be committed to Git.
3.  **Start the Server**:
    ```bash
    python main.py
    ```
4.  **The CRUD Test**:
    - **C**reate: Add a book via the `/add` route.
    - **R**ead: View the list on the `/` route.
    - **U**pdate: Change a rating via the `/edit` route.
    - **D**elete: Remove a book via the `/delete` route.

## Summary

Today, you graduated from "Scripting" to "System Architecture." You learned how to use an ORM to secure and abstract your data layer, understood the Transactional nature of Sessions, and learned how to maintain data integrity across server reboots.

Tomorrow, we combine this power with **External APIs** to build a dynamic movie ranking system!

# Day 63 - SQLite and SQLAlchemy CRUD in Flask

Day 63 is a major backend step forward. The application stops treating persistence as a flat file problem and starts using a relational database. Instead of appending rows to CSV text manually, the app defines a model, creates a real database table, queries records through SQLAlchemy, and supports create, read, update, and delete operations through Flask routes.

This lesson needs some theory because databases are a different kind of persistence tool from CSV files. The move to SQLAlchemy and SQLite introduces concepts such as models, sessions, schemas, and application context, and those ideas are foundational for the rest of the Flask data layer.

## 1. The App Now Uses a Real Database Connection

The configuration starts here:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
```

This tells Flask-SQLAlchemy to use an SQLite database file called `books.db`. The important change is conceptual: the application is no longer writing raw text into a file. It is connecting to a database engine that understands tables, columns, and queries.

SQLite is a good teaching choice because it gives you database behavior without needing a separate server process.

## 2. The Model Class Defines the Table Schema

The `Book` model is the core of the lesson:

```python
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
```

This is one of the most important ideas in SQLAlchemy. The Python class is not only a class. It is also the definition of a database table.

That means:

- the class maps to a table
- each instance maps to a row
- each mapped attribute corresponds to a column

This is the core ORM idea. You work with Python objects, and SQLAlchemy translates those operations into database operations underneath.

## 3. Constraints in the Model Matter

The column definitions include rules such as `unique=True` and `nullable=False`:

```python
title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
```

These constraints are worth explaining because they move data rules into the schema itself. The database is not just storing values. It is also enforcing some integrity rules about what kinds of values are allowed.

That is a big step up from CSV. A flat file will store almost anything. A database schema can actively reject invalid or duplicate data.

## 4. `db.create_all()` Builds the Table from the Model

The app creates the schema with:

```python
with app.app_context():
    db.create_all()
```

This line is important because it shows one of the benefits of an ORM. You define the structure in Python, and SQLAlchemy can generate the corresponding table in the database.

The `app.app_context()` part also deserves explanation. Flask extensions like SQLAlchemy need access to the current Flask application configuration. Outside a normal request, the code must enter the application context manually so the extension knows which app it belongs to.

## 5. Reading Data Uses Queries Instead of File Parsing

The home route reads books like this:

```python
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.rating))
    all_books = result.scalars()
    return render_template('index.html', library=all_books)
```

This is a useful contrast with the previous CSV lesson. There is no manual file opening, no delimiter parsing, and no row splitting. Instead, the app asks the database for `Book` records ordered by rating.

That is one of the major benefits of relational storage. Querying becomes part of the system itself rather than something you have to reconstruct manually.

## 6. Creating Records Uses the Session

The `/add` route creates a `Book` instance from form data:

```python
new_book = Book(
    title=request.form['title'],
    author=request.form['author'],
    rating=request.form['rating']
)
db.session.add(new_book)
db.session.commit()
```

This introduces the session workflow that matters throughout SQLAlchemy:

1. create or load an object
2. add or modify it in the session
3. commit the session

`commit()` is important because it is the step that actually persists the change to the database. Without it, the change remains only in the unit-of-work state managed by the session.

## 7. Updating Records Means Loading and Mutating an Existing Object

The `/edit` route shows the update side of CRUD:

```python
book_id = request.form['id']
book_to_update = db.get_or_404(Book, book_id)
book_to_update.rating = request.form['rating']
db.session.commit()
```

This is a strong example of how ORM code feels different from raw SQL. You do not write an `UPDATE` statement yourself. You load an object, change its attribute, and commit the session. SQLAlchemy tracks the change and writes the appropriate SQL behind the scenes.

That object-oriented workflow is one reason ORMs are so popular in Python web development.

## 8. Deleting Records Follows the Same Session Pattern

The `/delete` route completes the CRUD set:

```python
book_id = request.args.get('id')
book_selected = db.get_or_404(Book, book_id)
db.session.delete(book_selected)
db.session.commit()
```

This keeps the same overall pattern:

- identify the target record
- operate on the model object
- commit the result

That consistency is one of the nice things about working with an ORM. Create, update, and delete all use the same session-centered mental model.

## 9. The Routes Now Form a Full CRUD Application

By this point, the app supports all four CRUD operations:

- create a book with `/add`
- read books on `/`
- update a rating on `/edit`
- delete a book on `/delete`

That makes Day 63 more than a database setup lesson. It is the first full Flask app in the course with a real persistent data layer and a complete record lifecycle.

## 10. The Templates Stay Simple Because the Database Logic Lives in Python

The templates are intentionally straightforward. The homepage loops over the `library` records:

```html
{% for book in library %}
<li>{{ book.title }} - {{ book.author }} - {{ book.rating }}/10 
  <a href="{{ url_for('edit', id=book.id) }}">Edit Rating</a>
  <a href="{{ url_for('delete', id=book.id) }}">Delete</a>
</li>
{% endfor %}
```

That is a good architectural boundary. The database logic stays in the routes and model layer, while the template focuses on presentation. As the backend becomes more sophisticated, keeping that separation matters even more.

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```

Then visit:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/add`

Use the homepage links to edit and delete records. The SQLite database file will be created under the app's instance path when needed.

## Summary

Day 63 moves the course from flat-file persistence to relational storage. The `Book` model defines the schema, SQLAlchemy maps Python objects to database rows, and the session handles create, update, and delete operations before committing them to SQLite. The result is the first real CRUD Flask app in the repository, and it lays the groundwork for the more database-driven projects that follow.

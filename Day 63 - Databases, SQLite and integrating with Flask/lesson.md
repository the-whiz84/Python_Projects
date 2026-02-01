# We can see that our list of books is lost when we stop the program as it is saved in a list.

# I. SQLite Databases

First, let's create a database. The most used database in the world is SQLite. 
It's so popular that it's included by default in all Python installations, so if you're creating a Python project, you've already got it installed. 
We're going to create an SQLite database to store our book data.

Let's briefly play with SQLite in a separate project before we turn our attention back to Library website.

# 1. Create a new project and inside the main.py file import the sqlite3 module.
import sqlite3

# 2. Now create a connection to a new database (if the database does not exist then it will be created).
db = sqlite3.connect("books-collection.db")

# 3. Run main.py and you should see a new file appear in PyCharm called books-collection.db

# 4. Next we need to create a cursor which will control our database.
cursor = db.cursor()

So a cursor is also known as the mouse or pointer. If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.

# Creating Tables in our Database
Coming back to the Excel analogy, a single Excel file can contain many tables (sheets), each tab is a different table.

Similarly, our database can contain many tables.

# 5. Let's create one. Add this code below all the previous lines.
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Let's break this down.

cursor                              # - We created this in step 4 and this is the mouse pointer in our database that is going to do all the work.

.execute()                          # - This method will tell the cursor to execute an action. All actions in SQLite databases are expressed as SQL (Structured Query Language) commands. These are almost  like English sentences with keywords written in ALL-CAPS. There are quite a few SQL commands. But don't worry, you don't have to memorize them.

CREATE TABLE                        # -  This will create a new table in the database. The name of the table comes after this keyword.
Docs: https://www.w3schools.com/sql/sql_ref_create_table.asp

books                               # -  This is the name that we've given the new table we're creating.

()                                  # -  The parts that come inside the parenthesis after CREATE TABLE books ( ) are going to be the fields in this table. Or you can imagine it as the Column headings in an Excel sheet.

id INTEGER PRIMARY KEY              # -  This is the first field, it's a field called "id" which is of data type INTEGER and it will be the PRIMARY KEY for this table. The primary key is the one piece of data that will uniquely identify this record in the table. e.g. The primary key of humans might be their passport number because no two people in the same country has the same passport number.

title varchar(250) NOT NULL UNIQUE  # -  This is the second field, it's called "title" and it accepts a variable-length string composed of characters. The 250 in brackets is the maximum length of the text. NOT NULL means it must have a value and cannot be left empty. UNIQUE means no two records in this table can have the same title.

author varchar(250) NOT NULL        # -  A field that accepts variable-length Strings up to 250 characters called author that cannot be left empty.

rating FLOAT NOT NULL               # -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.


# 6. Run the code from step 5 and there will be no noticeable changes. In order to view our database we need to download some specialized software.

Head over to the link below and download DB Browser for your operating system. (If you are on Windows go for the Standard Installer).
https://sqlitebrowser.org/dl/
# On VsCOde we can use SQLite Viewer extension to do the same thing

# 9. To add data to our table we can head back to main.py and write the following code:

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
This will create a new entry in our books table for the Harry Potter book and commit the changes to our database.

# 10. Now comment out the previous line of code where you are created the table called books. Otherwise, you'll get sqlite3.OperationalError: table books already exists.

# 11. Then close down the database in DB Browser by clicking Close Database. Otherwise, you'll get a warning about database locked when you work with the database in PyCharm.

# 12. Now run the code in main.py and re-open the database in DB Browser to see the updated books table. it should look like this:

SQL queries are very sensitive to typos. If instead of writing:

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
You wrote:

cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
Then it won't work at all (can you even spot the difference in the code?)

Luckily, there are much better ways of working with SQLite in Python projects, we can use a tool called SQLAlchemy to write Python code instead of all these error-prone SQL commands. That's what we'll do in the next lesson!


# II. SQLAlchemy
As you've seen, writing SQL commands are complicated and error-prone. It would be much better if we could just write Python code and get the compiler to help us spot typos and errors in our code. That's why SQLAlchemy was created.

SQLAlchemy is defined as an ORM (Object Relational Mapping) library. This means that it's able to map the relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object. This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy.

Let's continue writing some more code in our separate project before we come back to the library of our favorite books.

1. Comment out all the existing code where we create an SQLite database directly using the sqlite3 module (or just close the separate project)

2. Install the required packages flask, SQLAlchemy, and flask_sqlalchemy from the requirements.txt. You can see the packages and their versions in the requirements.txt. PyCharm should have prompted you to install the packages in the requirements.txt file when you first opened the starting project:


# III. CRUD Operations with SQLAlchemy
Hopefully, you figured out how to solve the challenge from the last lesson, as a review, here's a summary of some of the things we did:


# 1. Create a New Database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
 
app = Flask(__name__)
 
class Base(DeclarativeBase):
    pass
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
As of flask-sqlalchemy version 3.1, you need to pass a subclass of DeclarativeBase to the constructor of the database.


# 2. Create a New Table
Next we define and create the model. What is the : used for? Explicitly declaring a variable type. Below we are explicitly saying that id is of type Mapped. SQLAlchemy uses the generic Mapped so that it can type check the data that will be stored in the database.

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
 
with app.app_context():
    db.create_all()


In addition to these things, the most crucial thing to figure out when working with any new database technology is how to CRUD data records.
Create
Read
Update
Delete


So, let's go through each of these using SQLite and SQLAlchemy:


# 3. Create A New Record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
NOTE: When creating new records, the primary key fields is optional. you can also write:

new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

the id field will be auto-generated.


# 4. Read All Records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows.


# 5. Read A Particular Record By Query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
To get a single element we can use scalar() instead of scalars().


# 6. Update A Particular Record By Query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 


# 7. Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  
Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated


# 8. Delete A Particular Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.

from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your secret CSRF key'
bootstrap = Bootstrap5(app)


class BookForm(FlaskForm):
    title = StringField("Book Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = FloatField("Rating from 0 to 10", validators=[DataRequired(), NumberRange(min=0, max=10, message="Enter a float between 0.0-10.0")])
    submit = SubmitField('Add Book')


class UpdateForm(FlaskForm):
    title = StringField(label='Book Name', render_kw={'readonly': True, 'disabled': 'disabled'})
    author = StringField(label='Author', render_kw={'readonly': True, 'disabled': 'disabled'})
    rating = FloatField(label="Rating", validators=[DataRequired(), NumberRange(min=0.0, max=10.0, message="Enter Between 0.0-10.0")])
    submit = SubmitField(label='Update Rating')


##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# All the Flask routes
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # CREATE RECORD
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            rating=form.rating.data
            )
        db.session.add(new_book)
        db.session.commit()
        flash(message=f"Book Name : {new_book.title} Added successfully", category="alert-success")
        return redirect(url_for('home'))
    
    return render_template('add.html', form=form)


@app.route("/edit/<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    form = UpdateForm()
    book_to_edit = db.get_or_404(Book, book_id)
    if form.validate_on_submit():
        book_to_edit.rating = form.rating.data
        db.session.commit()
        flash(f"Rating for book: {book_to_edit.title} updated successfully",category="alert-success")
        return redirect(url_for('home'))
    
    form.title.data = book_to_edit.title
    form.author.data = book_to_edit.author
    form.rating.data = book_to_edit.rating
    return render_template("edit_rating.html", form=form)


@app.route('/delete/<book_id>', methods=['GET', 'POST'])
def delete(book_id):
    book_selected = db.get_or_404(Book, book_id)
    db.session.delete(book_selected)
    db.session.commit()
    flash(message= f"Book Name : {book_selected.title} Deleted successfully",category="alert-danger")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

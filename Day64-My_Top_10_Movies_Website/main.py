from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests, os

TMDB_TOKEN = os.environ.get("TMDB_TOKEN")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie/"
img_base_url =  "https://image.tmdb.org/t/p/w500"

tmdb_headers = {
"accept": "application/json",
"Authorization": f"Bearer {TMDB_TOKEN}"
}


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6942ohtF0"D|jbSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Optional: this will allow each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g. 7.3", validators=[DataRequired(), NumberRange(max=10)], render_kw={'autofocus': True, 'autocomplete': 'off'})
    review = StringField("Your Review", validators=[DataRequired()], render_kw={'autocomplete': 'off'})
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()], render_kw={'autofocus': True, 'autocomplete': 'off'})
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template('index.html', movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_to_edit = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(TMDB_SEARCH_URL, headers=tmdb_headers, params={"query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    
    return render_template('add.html', form=form)


@app.route("/select", methods=['GET', 'POST'])
def select_movie():
    movie_id = request.args.get('id')
    response = requests.get(f"{TMDB_INFO_URL}{movie_id}", headers=tmdb_headers)
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=(data["release_date"]).split("-")[0],
        description=data["overview"],
        img_url=f"{img_base_url}{data["poster_path"]}"
        )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=new_movie.id))


if __name__ == '__main__':
    app.run()

# Day 64 - API-Assisted Movie Catalogs with Flask and SQLAlchemy

Day 64 builds on the database app from the previous lesson, but now the local database is no longer the only source of information. Instead of typing every movie detail manually, the app uses The Movie Database (TMDb) API to search for films, fetch a selected movie's metadata, and then store that result in the local SQLite database for personal ranking and review.

This lesson benefits from a bit of theory because it introduces a common real-world pattern: combine an external API with a local database. The external service provides rich reference data, while the local database stores the user's own curated subset and personal annotations.

## 1. The App Combines a Remote API with a Local Database

At the top of [main.py](/Users/wizard/Developer/Python_Projects/Day%2064%20-%20My%20Top%2010%20Movies%20Website/main.py), the app defines both the TMDb endpoints and the local SQLAlchemy model:

```python
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie/"
img_base_url = "https://image.tmdb.org/t/p/w500"
```

and:

```python
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
```

That pairing is the main architectural idea of the lesson. TMDb acts as the source of movie metadata, while the local database stores the movies the user has chosen, rated, and reviewed.

## 2. The TMDb Token Belongs in the Environment

The app builds the authorization header from an environment variable:

```python
TMDB_TOKEN = os.environ.get("TMDB_TOKEN")

tmdb_headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"
}
```

This is worth keeping in the lesson because it reinforces a good backend habit. API credentials should stay outside the codebase. Environment variables let the app authenticate safely without hardcoding secrets into the project.

That pattern also makes the app easier to run in different environments with different credentials.

## 3. Searching for a Movie Is a Separate Step from Storing It

The `/add` route handles the search stage:

```python
@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(TMDB_SEARCH_URL, headers=tmdb_headers, params={"query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    
    return render_template('add.html', form=form)
```

This is an important design choice. The route does not immediately create a new database row after the user enters a title. First it searches TMDb and shows the possible matches.

That is a realistic application pattern:

- user enters a search query
- app shows candidate records
- user chooses the correct one
- app stores the selected result

Without that middle step, the database would be much more likely to fill with wrong or incomplete movie records.

## 4. The Selection Page Acts as a Disambiguation Step

The [select.html](/Users/wizard/Developer/Python_Projects/Day%2064%20-%20My%20Top%2010%20Movies%20Website/templates/select.html) template renders the search results:

```html
{% for movie in options %}
<p>
  <a href="{{ url_for('select_movie', id=movie.id) }}"> {{ movie.title }} - {{ movie.release_date }}</a>
</p>
{% endfor %}
```

This is a good example of a multi-step workflow. The app is not storing arbitrary search results. It is asking the user to identify the exact movie they meant.

That kind of selection step is common whenever a search result may contain many close matches.

## 5. The Detail Request Hydrates the Local Record

Once the user clicks a result, the `/select` route fetches the full movie details:

```python
@app.route("/select", methods=['GET', 'POST'])
def select_movie():
    movie_id = request.args.get('id')
    response = requests.get(f"{TMDB_INFO_URL}{movie_id}", headers=tmdb_headers)
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=(data["release_date"]).split("-")[0],
        description=data["overview"],
        img_url=f"{img_base_url}{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=new_movie.id))
```

This is one of the most useful backend patterns in the course so far. The app first uses a search API, then uses the chosen record ID to request richer detail, and only after that does it create the local database row.

That keeps the local data more complete and accurate than if it relied only on the original search response.

## 6. The Local Database Stores User-Specific Data

Notice what the TMDb API does not provide for this app:

- your rating
- your ranking
- your review

Those fields are local to the user's own movie list. That is why the app still needs its own database even though it has access to an external movie API.

This is the core architectural reason to combine the two systems:

- external API for canonical movie metadata
- local database for user-specific application state

That separation is very common in production systems.

## 7. Ranking Is Calculated Dynamically from Stored Ratings

The homepage route orders movies by rating and then computes rankings:

```python
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template('index.html', movies=all_movies)
```

This is a useful lesson in derived data. The app stores each movie's rating, but the ranking is recalculated based on the current ordered list. That means the rankings stay in sync when movies are added or updated.

It is a simple example of business logic living in the route layer: the page is not just displaying data, it is computing part of the presentation state from the stored values.

## 8. The Frontend Uses the Database Records as Display Cards

The [index.html](/Users/wizard/Developer/Python_Projects/Day%2064%20-%20My%20Top%2010%20Movies%20Website/templates/index.html) template turns each stored movie into a card:

```html
{% for movie in movies %}
  <div class="card">
    <div class="front" style="background-size: 100% 100%; background-image: url('{{ movie.img_url }}');">
      <p class="large">{{ movie.ranking }}</p>
    </div>
    <div class="back">
      <div class="title">{{ movie.title }} <span class="release_date"> ({{ movie.year }})</span></div>
      <div class="rating">
        <label>{{ movie.rating }}</label>
      </div>
      <p class="review">{{ movie.review }}</p>
      <p class="overview">{{ movie.description }}</p>
    </div>
  </div>
{% endfor %}
```

That template shows the value of the data model clearly. The app is not storing only names. It is storing enough structured information to render a polished, content-rich UI card for each movie.

## 9. The Workflow Is Search, Select, Enrich, Store, Then Review

If you step back, Day 64 teaches a very strong application workflow:

1. user searches for a movie title
2. TMDb returns possible matches
3. user selects the correct movie
4. app fetches full details for that movie
5. app stores the result locally
6. user adds a personal rating and review

That is a richer flow than the earlier CRUD apps, and it feels much closer to a real product.

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Set the required environment variables:

```bash
export FLASK_KEY="your_secret_key"
export TMDB_TOKEN="your_tmdb_bearer_token"
```

Run the app:

```bash
python main.py
```

Then visit:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/add`

Search for a movie, choose one from the TMDb results, then add your rating and review.

## Summary

Day 64 combines an external API with a local SQLAlchemy database. TMDb provides movie metadata, while the local database stores the user's selected movies, ratings, reviews, and computed rankings. The key lesson is architectural: external services are often best used as reference data sources, while the application's own database keeps the user-specific state that makes the product personal.

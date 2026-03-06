# Day 64 - My Top 10 Movies: API-Driven Data Architecture

Yesterday, we learned how to build a persistent database and perform manual CRUD operations. Today, we advance our architecture by connecting our local data store to a global source of truth.

We are building a "Top 10 Movies" website. Instead of manually typing movie descriptions or hunting for poster URLs, we integrate the **TMDb (The Movie Database) API** to automatically populate our database with professional metadata.

## 1. The Hybrid Architecture: Local Cache vs. Global API

In professional software development, your database rarely exists in a vacuum. It often acts as a specialized subset or a local "cache" of a much larger global dataset.

Our app implements a **Multi-Step State Machine**:

1.  **Stage: Search** (GET/POST `/add`): The user enters a title. We query the TMDb `/search/movie` endpoint. We get back a list of 20+ matches.
2.  **Stage: Select** (GET `/select`): We render these matches. The user clicks one. We only have the `id` from the list.
3.  **Stage: Fetch & Hydrate** (GET `/select?id=...`): We take that `id` and hit the TMDb `/movie/{id}` endpoint to get the "Full Profile"—overview, release date, and poster path.
4.  **Stage: Save** (db.session.add): We move this external data into our local SQLAlchemy `Movie` table.
5.  **Stage: Personalize** (GET/POST `/edit`): Since this is "Your" Top 10 list, we immediately redirect you to add your unique rating and review.

This Search-Select-Add-Edit flow is a classic architectural pattern for any data-driven application (e.g., adding a song to a playlist, a product to a cart, or a friend to a list).

## 2. Advanced Requests: Headers and Authentication

To communicate with TMDb, we use the `requests` library. Unlike public APIs, professional services require authentication. We implement this using **Bearer Tokens** in the HTTP Headers:

```python
import os
import requests

TMDB_TOKEN = os.environ.get("TMDB_TOKEN")
tmdb_headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"
}

# Example of a clean API interaction
response = requests.get(TMDB_SEARCH_URL, headers=tmdb_headers, params={"query": movie_title})
data = response.json()["results"]
```

**Senior Tip**: Notice we never hardcode the token. We pull it from `os.environ`. This is the first rule of **The Twelve-Factor App**: "Store config in the environment." This keeps our secrets out of Git and allows us to use different tokens for Development and Production.

## 3. Dynamic Calculation: The Ranking Engine

Our database stores ratings, but how do we determine the #1 movie? We could manually type "Rank 1", but that breaks if we add a new favorite. Instead, we compute the rankings **dynamically** in the view:

```python
@app.route("/")
def home():
    # 1. Fetch all movies sorted by rating (lowest to highest)
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    # 2. Assign rankings based on index
    for i in range(len(all_movies)):
        # If we have 10 movies, the highest rated (last in list) becomes Rank #1
        all_movies[i].ranking = len(all_movies) - i

    # 3. Synchronize this calculation back to the database
    db.session.commit()

    return render_template('index.html', movies=all_movies)
```

By calculating ranks every time the homepage loads, our rankings are always up-to-date. This is a simple example of a **Business Logic Layer** embedded in a web route.

## How to Run the Movie Tracker

1.  **Get an API Token**: Create an account at [The Movie Database (TMDb)](https://www.themoviedb.org/) and generate an API Read Access Token.
2.  **Environment Setup**:
    ```bash
    export TMDB_TOKEN="your_token_here"
    export FLASK_KEY="your_flask_secret"
    ```
3.  **Dependencies**:
    ```bash
    pip install flask flask-sqlalchemy flask-wtf flask-bootstrap requests
    ```
4.  **Launch**:
    ```bash
    python main.py
    ```
5.  **Verification**:
    - Search for a movie like "Avatar" or "Matrix."
    - Select a specific version from the list.
    - Add your rating.
    - Refresh the home page and verify the ranking calculated correctly (Highest rating = #1).

## Summary

Today, you bridged the gap between your local system and the global internet. You learned how to orchestrate a complex multi-step data flow, how to handle authenticated API requests safely, and how to implement dynamic calculation logic in your backend to handle relative data rankings.

Tomorrow, we pause the coding to study **Web Design School**—ensuring the movies we display look as good as the code that fetches them!

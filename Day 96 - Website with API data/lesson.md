# Day 96 - Consuming External APIs in Flask Web Pages

This project is a lightweight Flask site built on top of an external API. Instead of serving only local data, the app fetches information about books and chapters from `the-one-api.dev` and turns that response into rendered pages.

That makes the lesson about bridging remote JSON data into a server-rendered website.

## 1. Fetch External Data Up Front

The app defines the API root and immediately requests the list of books:

```python
API_URL = "https://the-one-api.dev/v2/"

book_response = requests.get(f"{API_URL}book").json()
all_books = book_response["docs"]
book_id = [doc["_id"] for doc in all_books]
```

This is a simple pattern, but it teaches a real tradeoff:

- fetching at import time keeps the routes simple
- it also means app startup depends on the remote API being reachable

For a small project, this is acceptable. It keeps the application easy to read.

## 2. Pass API Data Straight Into Templates

The home route is as small as it should be:

```python
@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)
```

That is a good Flask pattern. The route does not transform more than it needs to. It simply hands the normalized response data to the template layer.

The book-detail route does a little more orchestration:

```python
@app.route("/book/<index>", methods=["GET", "POST"])
def show_book(index):
    requested_book = None
    for book in all_books:
        if book["_id"] == index:
            requested_book = book
            all_chapters = requests.get(f"{API_URL}book/{index}/chapter").json()["docs"]
    return render_template("book.html", book=requested_book, all_chapters=all_chapters)
```

This route uses the book id from the URL, finds the matching record, then performs a second API call for the chapter list.

That is a very common web-app pattern:

- index page with a collection
- detail page with per-item follow-up data

## 3. Keep the Website Simple Around the Data

The project also includes static routes like `about`:

```python
@app.route("/about")
def about():
    return render_template("about.html")
```

That is useful because it keeps the structure of the site familiar. The API-backed pages are not floating alone. They sit inside a normal Flask site with multiple routes and templates.

The larger lesson is that external data does not need a JavaScript-heavy frontend to be useful. A classic Flask template app can still consume remote APIs cleanly.

## How to Run the API-Backed Flask Site

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Flask app:
   ```bash
   python main.py
   ```
3. Open the local site and verify:
   - the home page lists the books returned by the API
   - a `/book/<id>` page loads the corresponding chapters
   - static routes such as `/about` still render normally

## Summary

Today, you connected Flask templates to a live external API. The app fetches book data, reuses ids to request chapter details, and passes the resulting JSON into server-rendered pages. The main skill here is not the API itself. It is learning how to move remote data cleanly into a traditional web route structure.

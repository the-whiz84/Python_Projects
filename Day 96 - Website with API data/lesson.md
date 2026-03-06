# Day 96 - Flask Websites Backed by API Data

This project is a good example of a server-rendered Flask site that does not own its own dataset. Instead of reading from a local database, it requests book and chapter data from `the-one-api.dev` and passes that data into Jinja templates.

That makes the lesson less about Flask basics and more about how a traditional Python web app can sit in front of an external JSON API.

## 1. Treat the External API as the Data Source

The app defines a base URL and immediately requests the list of books:

```python
API_URL = "https://the-one-api.dev/v2/"

book_response = requests.get(f"{API_URL}book").json()
all_books = book_response["docs"]
book_id = [doc["_id"] for doc in all_books]
```

The important shift here is architectural. The Flask app is not generating this content itself. It is acting as the layer that:

- requests remote data
- chooses which parts of that response matter
- turns the result into HTML pages for the browser

That pattern is very common in Python web work. The app server becomes an adapter between a remote service and a user-facing template.

## 2. Understand the Tradeoff of Fetching at Import Time

The book list is fetched when the application module loads, not inside the route function.

That keeps the home route very small:

```python
@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)
```

This is a useful design tradeoff to notice.

Advantages:

- the route stays simple
- the data is available immediately for template rendering
- the code is easy to follow

Costs:

- app startup now depends on the remote API being reachable
- the data is only as fresh as the last application start
- failures at import time are harder to recover from gracefully

For a learning project, this is acceptable. It keeps the flow clear. But it also teaches an important lesson: where you fetch data affects both reliability and design.

## 3. Use URL Parameters to Request More Specific Data

The detail page route takes a book id from the URL:

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

This route demonstrates a common two-step pattern:

1. identify which item the user asked for
2. fetch more detailed data for that specific item

The result is a classic list-and-detail website structure:

- the home page shows the collection of books
- the detail page shows the selected book plus its chapters

That is one of the most useful web patterns to recognize, because it appears everywhere from storefronts to dashboards to documentation sites.

## 4. Let the Template Layer Stay Focused on Presentation

The route functions pass ready-to-use data into Jinja templates instead of building HTML by hand.

On the home page, the template loops through the books:

```html
{% for book in all_books: %}
<div class="post-preview">
    <a href="{{ url_for('show_book', index=book._id) }}">
        <h2 class="post-title">{{ book.name }}</h2>
    </a>
</div>
{% endfor %}
```

This separation is exactly what you want in Flask:

- Python handles data retrieval and routing
- Jinja handles presentation

The templates also use shared partials like `header.html` and `footer.html`, which helps keep the site layout consistent across pages.

## 5. A Flask App Can Be API-Driven Without Becoming a SPA

This lesson is useful because it shows that consuming an API does not automatically mean building a JavaScript-heavy frontend.

The app remains a normal Flask website:

- route functions receive requests
- Python calls the remote API
- Jinja templates render the response into HTML

That approach is often a better fit when:

- the site is simple
- SEO or server rendering matters
- you want straightforward Python-first logic

In other words, an API-backed website does not have to become a separate frontend-plus-backend system just to be valid.

## 6. Keep Supporting Pages Alongside the Dynamic Route

The project includes a static supporting route too:

```python
@app.route("/about")
def about():
    return render_template("about.html")
```

That is worth calling out because it shows how dynamic and static pages coexist naturally in the same Flask app. The API-backed pages do not need their own isolated architecture. They fit into the same route map as the rest of the site.

That is part of what makes Flask a good teaching framework: the jump from simple template pages to API-fed template pages is incremental rather than dramatic.

## How to Run the API-Backed Flask Site

Install the dependencies and start the app:

```bash
pip install -r requirements.txt
python main.py
```

Then verify:

- the home page lists the books returned by the remote API
- clicking a book opens `/book/<id>` and loads the related chapter data
- the `/about` page still renders normally through the same Flask app

Because the project depends on a live external service, the API must be reachable when the app starts.

## Summary

Day 96 shows how a Flask site can use an external API as its data source without abandoning server-rendered templates. You fetched remote JSON data, reused ids to build detail pages, passed normalized responses into Jinja templates, and kept the overall site structure simple and readable. The main lesson is how Flask can act as the middle layer between a remote service and a human-friendly website.

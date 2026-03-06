# Day 57 - Blog Templating: Injecting Logic into HTML

Yesterday, we learned how to serve static HTML files using `render_template`. However, static files are inherently limited; they look the exact same every time you refresh the page.

Modern web applications are dynamic. When you load your Twitter feed, you don't load a static HTML file; a backend server queries a database for the latest posts and dynamically generates the HTML before sending it to you.

Today, we build exactly that. We are constructing a blog that fetches raw JSON data from an external API, transforms that data into Python Objects, and injects those objects directly into our HTML structure using the **Jinja Templating Engine**.

## Passing Variables to the Frontend

Jinja allows us to pass Python variables (strings, integers, lists, dictionaries, or even custom Class objects) into our HTML templates as keyword arguments inside `render_template`.

```python
@app.route("/")
def home():
    current_year = dt.datetime.now().year
    your_name = "Wizard"

    # We pass 'year' and 'name' as kwargs to the template
    return render_template("index.html", year=current_year, name=your_name)
```

Inside `index.html`, we "catch" these variables using Jinja's double curly brace syntax, which evaluates the Python expression and pastes the result into the HTML as text:

```html
<footer>
  <p>Copyright © {{ year }} {{ name }}. All rights reserved.</p>
</footer>
```

When the user visits the page, their browser receives plain HTML: `<p>Copyright © 2026 Wizard. All rights reserved.</p>`. The Python logic is entirely hidden from the client.

## Jinja Control Flow: `{% %}`

The real power of Jinja comes from its ability to execute logic directly inside the HTML file. Jinja uses the `{% %}` syntax for statements like `if` conditions and `for` loops.

In our `blog` route, we fetch an array of posts from an API. Instead of writing raw HTML for each post repeatedly, we can loop over the array directly in the template:

```html
<!-- Inside blog.html -->
<div class="content">
  {% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.subtitle }}</p>
  <a href="{{ url_for('show_post', index=post.id) }}">Read More</a>
  <hr />
  {% endfor %}
</div>
```

**Notice the syntax difference:**

- `{{ }}` is used for **evaluation** (printing a variable's value to the screen).
- `{% %}` is used for **execution** (running a loop or an if-statement without printing anything).
- You must always explicitly close Jinja blocks (e.g., `{% endfor %}`) because HTML doesn't abide by Python's strict spacing rules!

## Passing Complex Objects

In `main.py`, we elevate our architecture. Instead of passing raw JSON dictionaries to our frontend template—which is prone to typos and missing keys—we deserialize the JSON into strongly-typed Python objects:

```python
from post import Post

posts = requests.get("https://api.npoint.io/...").json()
post_objects = []

for post in posts:
    # We create a formal Post object
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    # Pass the list of Objects directly to the template
    return render_template("index.html", posts=post_objects)
```

Now, inside the HTML template, we can access the attributes of the object cleanly: `{{ post.title }}` instead of `{{ post['title'] }}`. This Object-Oriented approach makes your templates significantly more resilient.

## Running the Dynamic Blog

1. Ensure your environment is active and Flask is installed:
   ```bash
   pip install flask requests
   ```
2. Run the main blog server:
   ```bash
   python "main.py"
   ```
3. Open a browser and navigate to `http://127.0.0.1:5000/`. You should see the homepage dynamically populated with posts fetched live from the external JSON API! Click "Read More" to see specific post routes.

## Summary

Today you crossed a major threshold in backend engineering. You successfully integrated an external API (simulating a database), transformed the raw data into Python models, and passed those models into the Jinja rendering engine. You utilized `{% for %}` loops to dynamically generate HTML elements based on your data.

Tomorrow, we step away from Python logic temporarily to learn how to instantly style these pages using **Bootstrap**, the world's most popular CSS framework!

# Day 59 - Blog Templates, Includes, and API-Fed Content

Day 59 takes the Jinja blog idea from the previous lesson and makes it look more like a real multi-page site. Instead of one template doing all the work, the app now has shared header and footer partials, separate routes for home, about, and contact pages, and post content loaded from an external JSON API.

This lesson matters because it starts teaching web-app structure, not just individual Flask features. The code is still small, but the decisions about template reuse, route layout, and shared data are the same kinds of decisions that show up in larger Flask projects.

## 1. Multi-Page Apps Need Shared Layout Structure

The app now has several route handlers:

```python
@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
```

This is a useful step forward from the earlier Flask examples. The app is no longer a single demo route. It has multiple pages, each with a different role:

- homepage with a list of blog posts
- about page
- contact page
- individual post pages

That immediately raises a practical question: how do you avoid repeating the same page chrome on every template?

## 2. `{% include %}` Helps You Reuse Template Pieces

The templates answer that question by using shared partials. For example, [index.html](/Users/wizard/Developer/Python_Projects/Day%2059%20-%20Upgraded%20Blog/templates/index.html) starts and ends with includes:

```html
{% include "header.html" %}
...
{% include 'footer.html' %}
```

This is one of the most valuable Jinja features in the Flask section. It lets you keep repeated markup in one place instead of copying it into every page.

The benefit is practical, not theoretical:

- change the header once
- every page that includes it gets the update

That is the template version of not repeating yourself.

## 3. Includes Make the Page Templates Easier to Read

When the shared pieces are moved into partials, the main page files can focus on their unique content. In the homepage template, the interesting part is the list of posts, not the navbar boilerplate.

This is why template modularity matters. It improves maintainability, but it also improves readability. A developer opening `index.html` can focus on the content that is specific to the homepage instead of scrolling through the same repeated header and footer code over and over.

## 4. API Data Is Loaded Once and Reused Across Requests

At the top of [main.py](/Users/wizard/Developer/Python_Projects/Day%2059%20-%20Upgraded%20Blog/main.py), the app fetches the post data:

```python
posts = requests.get("https://api.npoint.io/7355269ada93b9890800").json()
```

This line is outside the route functions, which is worth explaining. Because it runs when the application starts, the blog data is loaded once and stored in memory. The homepage route can then reuse it without making a fresh HTTP request on every page load.

That is a small but meaningful architectural choice. It keeps the route simple and avoids unnecessary repeated network calls during development.

## 5. The Homepage Template Iterates Over the Blog Data

The homepage displays the posts with a Jinja loop:

```html
{% for blog_post in all_posts: %}
<div class="post-preview">
    <a href="{{ url_for('show_post', index=blog_post.id) }}">
        <h2 class="post-title">{{ blog_post.title }}</h2>
        <h3 class="post-subtitle">{{ blog_post.subtitle }}</h3>
    </a>
    <p class="post-meta">
        Posted by
        <a href="#!">{{ blog_post.author }}</a>
        on {{ blog_post.date }}
    </p>
</div>
<hr class="my-4" />
{% endfor %}
```

This is a good example of how Jinja, Bootstrap, and Flask now work together:

- Flask passes the `all_posts` data into the template
- Jinja loops over it
- Bootstrap classes style the rendered output

The technologies are starting to layer together in a natural way.

## 6. `url_for()` Connects the List View to the Detail View

Inside the loop, each post preview links to a dedicated route:

```html
<a href="{{ url_for('show_post', index=blog_post.id) }}">
```

This is a useful design detail. The template does not hardcode the path as a raw string. Instead, it asks Flask to generate the correct URL for the `show_post` route.

That matters because it keeps the template aligned with the application routing logic. If the route name or path changes later, `url_for()` makes those links easier to maintain than manually assembled URLs.

## 7. The Detail Page Renders One Post at a Time

The route for an individual post looks like this:

```python
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
```

This is straightforward Python, but it teaches an important web-app pattern:

- the route receives an identifier from the URL
- the code selects the matching record
- the template renders that single record

That flow appears in almost every content-based web application.

## 8. The Post Template Uses the Record as Page Context

The [post.html](/Users/wizard/Developer/Python_Projects/Day%2059%20-%20Upgraded%20Blog/templates/post.html) template then renders the selected post:

```html
<header class="masthead" style="background-image: url({{ post.image_url }})">
  ...
  <h1>{{ post.title }}</h1>
  <h2 class="subheading">{{ post.subtitle }}</h2>
  <span class="meta">
    Posted by
    <a href="#!">{{ post.author }}</a>
    on {{ post.date }}
  </span>
</header>
```

That is a good reminder that a template does not need many variables to be powerful. As long as the route passes the right object or dictionary, the template can build a full page from it.

This is the central idea of server-side page composition: the backend prepares the data context, and the template turns that context into presentation.

## 9. The Lesson Is Really About Separation of Concerns

The stronger architectural lesson in Day 59 is separation of concerns:

- routes handle navigation and page selection
- API data provides the content
- shared includes hold the repeated layout pieces
- the page templates focus on their unique content sections

That separation is what makes the blog feel maintainable. It is no longer just "one Flask file and one giant HTML file." It is a small but structured web application.

## How to Run the Project

Install the required packages if needed:

```bash
pip install flask requests
```

Run the app:

```bash
python main.py
```

Then open:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/about`
- `http://127.0.0.1:5000/contact`
- `http://127.0.0.1:5000/post/1`

## Summary

Day 59 upgrades the blog from a single dynamic page into a more realistic multi-page Flask app. The key ideas are template includes for reusable layout, one-time API data loading, `url_for()` for route-aware links, and detail pages built from URL parameters. Together, those pieces make the app cleaner, easier to extend, and closer to how real content-driven sites are organized.

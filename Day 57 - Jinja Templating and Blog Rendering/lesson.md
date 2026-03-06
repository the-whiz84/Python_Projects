# Day 57 - Jinja Templating and Blog Rendering in Flask

Day 57 is where the Flask section starts to feel dynamic in a real web-app sense. The route no longer just returns a fixed template file. Instead, Python gathers data, passes that data into a template, and Jinja uses it to generate different HTML depending on the request.

This lesson benefits from a bit of general theory because Jinja is one of the core pieces that connects backend Python to frontend HTML. Once that connection is clear, the later Flask projects become much easier to follow.

## 1. Templates Become Dynamic When Python Passes Data Into Them

The simplest example is in [server.py](/Users/wizard/Developer/Python_Projects/Day%2057%20-%20Jinja%20Templating%20and%20Blog%20Rendering/server.py):

```python
@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    your_name = "Radu Chiriac"
    return render_template("index.html", num=random_number, year=current_year, name=your_name)
```

This route is still serving an HTML template, but it is no longer serving the exact same output every time. The template receives `num`, `year`, and `name`, so the final HTML can change based on Python values computed at request time.

That is the first important idea of Jinja: a template file is not just static markup. It is a view layer that can receive context from Python.

## 2. `{{ ... }}` Prints Values into the HTML

Jinja uses double curly braces when you want a value inserted into the page:

```html
<p>Copyright {{ year }} {{ name }}</p>
```

This is conceptually simple but very important. The browser never sees the Python code itself. Flask renders the template on the server, Jinja replaces the placeholders with actual values, and only then does the finished HTML go to the browser.

So the sequence is:

1. Flask route gathers or computes data
2. `render_template(...)` passes that data into Jinja
3. Jinja builds the final HTML
4. the browser receives the rendered page

That is classic server-side rendering, but now with actual variables instead of a fixed page file.

## 3. Dynamic Routes Can Feed Dynamic Templates

The `guess` route shows that template rendering can also depend on user input from the URL:

```python
@app.route("/guess/<name>")
def guess(name):
    gender_data = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender_data["gender"]
    age_data = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_data["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)
```

This route combines several ideas from earlier lessons:

- a dynamic path segment provides the `name`
- Python makes external API requests
- the returned JSON is unpacked into useful values
- those values are passed into a template

That makes Day 57 a nice synthesis lesson. Flask routing, HTTP requests, JSON handling, and templating are all working together in one small feature.

## 4. Templates Can Loop Over Data Structures

The real jump in template power appears in the blog example. The [blog.html](/Users/wizard/Developer/Python_Projects/Day%2057%20-%20Jinja%20Templating%20and%20Blog%20Rendering/templates/blog.html) file loops over posts directly inside the template:

```html
{% for blog_post in posts: %}
    <h1>{{ blog_post["title"] }}</h1>
    <h2>{{ blog_post["subtitle"] }}</h2>
    <p>{{ blog_post["body"] }}</p>
{% endfor %}
```

This is where Jinja starts to feel genuinely useful. Instead of writing repeated HTML blocks by hand, the template can generate them based on a Python list.

That is worth pausing on conceptually. The template is still HTML, but it now has just enough control flow to repeat sections and adapt to the data it receives.

## 5. `{{ ... }}` and `{% ... %}` Do Different Jobs

This lesson introduces the two pieces of Jinja syntax you use constantly:

- `{{ ... }}` for outputting a value
- `{% ... %}` for running template logic such as loops or conditionals

That distinction matters because one syntax prints something into the page, while the other controls how the page is built.

For example:

```html
{% for post in posts %}
  <h2>{{ post.title }}</h2>
{% endfor %}
```

The loop itself is control logic. The `post.title` expression is output. Keeping those roles clear makes templates much easier to read.

## 6. The Blog App Turns API Data into Page Content

The more complete blog implementation lives in [main.py](/Users/wizard/Developer/Python_Projects/Day%2057%20-%20Jinja%20Templating%20and%20Blog%20Rendering/main.py):

```python
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
```

This code fetches JSON data and then transforms each dictionary into a `Post` object. That transformation is worth explaining because it improves how the template reads and how the rest of the app is structured.

Instead of leaving the data as raw dictionaries, the app gives each post a simple model:

```python
class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
```

This is a small class, but it makes the data more explicit.

## 7. Small Model Objects Make Templates Cleaner

Using `Post` objects means the template and routes can work with attribute-style access such as `post.id` or `post.title` instead of indexing raw dictionaries everywhere.

This is not only about style. It teaches a useful architectural habit:

- external data comes in as JSON
- Python transforms it into a more convenient internal representation
- templates work with that cleaner representation

That pattern shows up constantly in web applications. Data often enters the system in one shape and gets converted into a better application-level shape before rendering.

## 8. Dynamic Detail Pages Build on Route Parameters

The blog detail route uses an integer path parameter to choose one post:

```python
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
```

This route is a good example of how Flask pages start to resemble real application behavior:

- the homepage lists many posts
- each post links to a dedicated route
- the route selects the matching object
- the template renders the chosen record

It is still a small project, but the page flow is now clearly application-like rather than demo-like.

## 9. This Lesson Introduces the View Layer Properly

One reason Day 57 matters is that it defines the role of the template layer much more clearly than the previous Flask lessons:

- routes gather data
- Python can call APIs or build objects
- templates decide how that data is displayed

That separation is important. If you put too much HTML construction in Python, the route becomes hard to read. If you try to move too much logic into the template, the template becomes messy. Jinja gives you a middle ground where the backend prepares the data and the template renders it.

## How to Run the Project

Install the required packages if needed:

```bash
pip install flask requests
```

Run the Jinja examples in [server.py](/Users/wizard/Developer/Python_Projects/Day%2057%20-%20Jinja%20Templating%20and%20Blog%20Rendering/server.py):

```bash
python server.py
```

Try these routes:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/guess/Ana`
- `http://127.0.0.1:5000/blog`

Run the blog-focused version in [main.py](/Users/wizard/Developer/Python_Projects/Day%2057%20-%20Jinja%20Templating%20and%20Blog%20Rendering/main.py):

```bash
python main.py
```

Then open:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/post/1`

## Summary

Day 57 turns Flask templates into a real view layer. Jinja lets routes pass Python values into HTML, print those values with `{{ ... }}`, and repeat page sections with `{% ... %}` blocks. The lesson also shows a useful architectural step: convert raw API JSON into simple Python objects before rendering. That combination is what makes the blog pages dynamic instead of just static files with placeholders.

# Day 56 - Identity Card & Personal Website: Rendering HTML and Static Files

Yesterday, we took our first steps into Server-Side Rendering (SSR) by returning raw strings of HTML directly from our Python functions. While this works for a tiny `<p>` tag, it is structurally impossible to maintain when building a full website with hundreds of lines of HTML, CSS styling, and JavaScript logic.

To build real web applications, we must separate our Backend logic (Python) from our Frontend presentation (HTML/CSS).

Today, we built a digital "Identity Card" website. To do this, we explore Flask's architectural solution to this separation of concerns: **The Jinja Templating Engine** and the **Static/Template Folder Structure**.

## The Templating Engine: `render_template`

Instead of returning a Python string, we want Flask to grab a physical `.html` file from our hard drive, read it, and send it to the browser as the HTTP Response.

We do this using `render_template`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Flask reads the index.html file and serves it to the client
    return render_template("index.html")
```

Under the hood, `render_template` utilizes an engine called **Jinja**. Jinja allows Flask to scan the HTML file before sending it and inject dynamic Python variables into it (which we will explore heavily tomorrow).

## Architecture: The `templates` Folder

When you call `render_template("index.html")`, Flask does not search your entire hard drive for that file. By default, Flask strictly enforces a specific folder architecture.

It looks exclusively inside a folder named exactly `templates` located in the same directory as your `server.py` file.

```text
/Day 56/
├── server.py
└── templates/
    └── index.html
```

If your HTML file is named `index.html` but it sits in the root folder next to `server.py`, Flask will crash with a `TemplateNotFound` error. This strict enforcement ensures that as your app scales to dozens of pages, your backend files and frontend files never mix.

## Architecture: The `static` Folder

HTML files are rarely alone. They link to CSS stylesheets, JavaScript files, and images.

If you put `profile.jpg` or `styles.css` inside the `templates` folder, or next to `server.py`, the browser will fail to load them. When the browser parses the HTML and sees `<link rel="stylesheet" href="styles.css">`, it sends a secondary GET request to your Flask server asking for that file.

By default, Flask protects your server. It drops all requests for random files, otherwise, anyone could request `server.py` and steal your backend source code!

To securely serve assets like CSS and images, Flask uniquely exposes a single folder to the internet: the `static` folder.

```text
/Day 56/
├── server.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── styles.css
    └── images/
        └── profile.jpg
```

Any file placed inside the `static` folder is automatically served by Flask without you needing to write a specific `@app.route` for it.

### Linking Static Assets in HTML

Because Flask manages the routing, we must update how our HTML links to these files. Instead of a relative path, we can use Jinja syntax to securely ask Flask where the static file is located:

```html
<!-- Inside templates/index.html -->

<!-- Linking a CSS file -->
<link
  rel="stylesheet"
  href="{{ url_for('static', filename='css/styles.css') }}"
/>

<!-- Showing an Image -->
<img
  src="{{ url_for('static', filename='images/profile.jpg') }}"
  alt="Profile Photo"
/>
```

The double curly braces `{{ }}` tell the Jinja engine: "Hey, run the Python code inside here and paste the result into the HTML before sending it to the browser." The `url_for` function calculates the exact, safe path to the asset.

## Running the Identity Card Website

1. Ensure your environment is active and Flask is installed:
   ```bash
   pip install flask
   ```
2. Run the main server script:
   ```bash
   python "server.py"
   ```
3. Open a browser and navigate to `http://127.0.0.1:5000/`. You should see a fully styled, CSS-backed HTML webpage!

## Summary

Today you crossed the bridge from hacking together text strings to building professional Full-Stack architectures. You separated your concerns by placing routing logic in Python, presentation markup in the `templates` folder, and aesthetic assets in the `static` folder.

Tomorrow, we will tap into the true power of the Jinja templating engine, using it to pass live Python variables directly into our HTML to build dynamic, data-driven pages!

# 1. Rendering HTML files with Flask

https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

# Flask uses the Jinja2 template engine to read templates or static files that you store locally
Flask will look for templates in the templates folder.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("zerodawn.html")


# 2. Serving static files with Flask

Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called static in your package or next to your module and it will be available at /static on the application.

To generate URLs for static files, use the special 'static' endpoint name:

url_for('static', filename='style.css')
The file has to be stored on the filesystem as static/style.css.


# By copying my website public folder static, images, css and icons, I was able to recreate the website using Flask


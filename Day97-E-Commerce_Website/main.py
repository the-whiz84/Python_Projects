from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()

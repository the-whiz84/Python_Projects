from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>This is a paragraph</p><img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3RuNGo1eTQ1dGZqa2xoM2Iyd2puODl3Y3B2NHZhaGQzNG44bG1mMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12ELmx0C4EFKcE/giphy.gif' />"


def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return '<em>' + function() + '</em>'
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return '<u>' + function() + '</u>'
    return wrapper_function


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "<h2>Bye!</h2>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name}! You are {number} years old.</p>"


if __name__ == "__main__":
    app.run(debug=True)
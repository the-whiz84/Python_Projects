from flask import Flask

app = Flask(__name__)

# print(__name__)
# __main__


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def say_bye():
    return "<h2>Bye</h2>"

# The most common way flask is run is by using name and main:
if __name__ == "__main__":
    app.run()
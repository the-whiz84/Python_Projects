import requests
from flask import Flask, render_template

app = Flask(__name__)

API_URL = "https://the-one-api.dev/v2/"

book_response = requests.get(f"{API_URL}book").json()
all_books = book_response["docs"]
book_id = [doc["_id"] for doc in all_books]


@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/book/<index>", methods=["GET", "POST"])
def show_book(index):
    requested_book = None
    for book in all_books:
        if book["_id"] == index:
            requested_book = book
            all_chapters = requests.get(f"{API_URL}book/{index}/chapter").json()["docs"]
    return render_template("book.html", book=requested_book, all_chapters=all_chapters)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()

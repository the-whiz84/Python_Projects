# import requests
# from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

from requests_html import HTMLSession
from bs4 import BeautifulSoup
 
WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "./data/100_best_movies.html"
 
# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()
 
    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)
 
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")
 
# Read web file if it exists, load from internet if it doesn't exist
soup = read_web_file()

movies = []
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

for movie in all_movies:
    title = movie.getText()
    movies.append(title)

with open("./data/movies.txt", "a") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")
# Day 45 - Web Scraping with BeautifulSoup

Today we're leaving the world of local files and simple scripts behind and heading out onto the internet. We're going to learn how to "scrape" websites—which is basically just a fancy word for writing a program that can read a website, find the information we want, and pull it out for us.

Whether you want to track prices on Amazon, monitor news headlines, or create a list of the 100 best movies of all time, web scraping is the tool you'll use.

## Getting Started: Requests and BeautifulSoup

To do this properly, we need two libraries:

1. **`requests`**: This is like your browser's delivery driver. It goes to a URL, asks for the HTML, and brings it back to your Python script.
2. **`BeautifulSoup`**: This is your parser. HTML looks like a giant, messy pile of tags to humans, but BeautifulSoup treats it like a structured tree that we can search through easily.

## First Steps: Scraping a Local File

Before we hit the live web, it's easier to practice on a file we already have. Look at `website.html` in your folder. This is a simple personal site, and we can use BeautifulSoup to find specific parts of it.

```python
from bs4 import BeautifulSoup

with open("./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
```

Once you've made your "soup" object, you can start digging. Want all the links?

```python
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))
```

Want a specific heading with a specific ID?

```python
heading = soup.find(name="h1", id="name")
```

The dot notation is your best friend here. If you use CSS selectors in your day-to-day web browsing, you'll love `soup.select()`.

## Scraping a Live Website: Hacker News

Now let's do something more interesting. In `main.py`, we're scraping a live version of Hacker News to find which article is currently the most popular.

```python
response = requests.get("https://appbrewery.github.io/news.ycombinator.com")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
```

Notice the `split()[0]` part. When we scrape the upvotes, we get a string like `"120 points"`. We split it by spaces and grab the first part (`"120"`) then turn it into an integer so we can find the maximum.

```python
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(f"The most popular article is: {article_texts[max_upvotes_index]}")
```

## Project: The 100 Best Movies of All Time

Finally, in `project.py`, we're tackling a big goal: scraping the 100 best movies of all time from Empire Online and saving them to a text file.

**A quick heads-up:** Some modern websites use a lot of JavaScript to show their content. Standard `requests` might just get a blank page. In this project, we use `requests_html` to "render" the page first, which is like telling Python to wait for the JavaScript to finish loading before we start scraping.

```python
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

with open("./data/movies.txt", "a") as file:
    for movie in movies[::-1]: # We reverse it to start from #1
        file.write(f"{movie}\n")
```

## Running the Project

```bash
python "main.py"
```

Running this will show you the top story on Hacker News right now. If you want to build the full 100 movie list, run:

```bash
python "project.py"
```

Check the `data/` folder after it finishes—you'll have a brand new `movies.txt` file waiting for you.

## Moving Forward

Web scraping is a superpower, but remember to use it responsibly. Always check a site's `robots.txt` file (just go to `website.com/robots.txt`) to see what their rules are for bots. Tomorrow, we'll take this a step further by learning how to scrape sites that require you to log in!

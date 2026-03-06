# Day 45 - Web Scraping with BeautifulSoup and HTML Parsing

Day 45 introduces web scraping as a structured parsing task, not just “grabbing text from a page.” The project starts with local HTML so the document tree is easier to understand, then moves to live websites where the same parsing ideas are used on real content. BeautifulSoup is the key tool because it turns raw HTML into something you can search like a nested document.

## 1. Parsing HTML into a Searchable Tree

The local-file example starts with:

```python
with open("./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
```

This is the core of BeautifulSoup usage. Once the HTML is parsed, you no longer have to treat it like one giant string. You can search by tag, class, id, or selector.

That shift is the real lesson: scraping is mostly about navigating document structure.

## 2. Extracting Repeated Elements from a Live Page

The Hacker News example looks for story links and scores:

```python
articles = soup.find_all(name="a", class_="storylink")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
```

This shows two important scraping patterns:

- gather repeated elements into a list
- normalize text so it becomes usable program data

The vote text arrives as something like `"38 points"`, so the script splits the string and converts the number into an integer before comparing values.

## 3. Turning Scraped Data into a Useful Result

Once the texts, links, and votes are collected, the script finds the most popular article:

```python
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
```

This is a good example of why scraping is usually not the final goal. The goal is to extract information that can then be ranked, filtered, saved, or analyzed.

The movie project in `project.py` does the same thing at a larger scale by scraping titles and writing them to `movies.txt`.

## 4. Why Some Sites Need More Than `requests`

The movie script uses `requests_html` to render JavaScript before parsing:

```python
session = HTMLSession()
response = session.get(WEB_PAGE)
response.html.render()
```

That matters because not every site returns finished HTML immediately. Some pages assemble their content in the browser with JavaScript. In those cases, a plain `requests.get()` may not be enough.

This is the broader scraping lesson of the day: the strategy depends on how the target page is built.

## How to Run the Project

1. Open a terminal in this folder.
2. Run the Hacker News scraper:

```bash
python main.py
```

3. Run the movie scraper:

```bash
python project.py
```

4. Check `data/movies.txt` after the movie script finishes and confirm that the scraped titles were written to disk.

## Summary

Day 45 introduces scraping as structured HTML parsing. BeautifulSoup turns pages into searchable trees, repeated elements can be extracted and normalized into lists, and the resulting data can be ranked or saved. The lesson also introduces a practical constraint: some sites need JavaScript rendering before scraping works reliably.

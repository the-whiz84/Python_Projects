# Day 45 - Scraping the Web with BeautifulSoup module

This lesson is manually reconstructed from this day’s real project files and historical lesson notes from git history. It focuses specifically on **Scraping the Web with BeautifulSoup module** and avoids generic cross-day boilerplate.

## Table of Contents

- [1. What You Build](#1-what-you-build)
- [2. Core Concepts](#2-core-concepts)
- [3. Project Structure](#3-project-structure)
- [4. Implementation Walkthrough](#4-implementation-walkthrough)
- [5. Day Code Snippet](#5-day-code-snippet)
- [6. How to Run](#6-how-to-run)
- [7. Common Pitfalls and Debug Tips](#7-common-pitfalls-and-debug-tips)
- [8. Practice Extensions](#8-practice-extensions)
- [9. Key Takeaways](#9-key-takeaways)

## 1. What You Build

You build **Scraping the Web with BeautifulSoup module** as a day-specific project using `requests`, `beautifulsoup`, `bs4`, `html/css`.
Primary entrypoint: `main.py`.

## 2. Core Concepts

- Day-specific stack and techniques: `requests`, `beautifulsoup`, `bs4`, `html/css`.
- Converting raw inputs/events/data into deterministic outputs.
- Organizing logic so the main flow stays readable and debuggable.

Historical lesson signals recovered from git history:
- 100 Movies that You Must Watch
- Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1).
- The result should look something like this:
- 1. Web Scraping

## 3. Project Structure

- `main.py`: Entrypoint script coordinating the full flow.
- `project.py`: Entrypoint script coordinating the full flow.
- `website.html`: Static web page source.

## 4. Implementation Walkthrough

1. Call external web/API resources and normalize returned data before use.
2. Add targeted checks for edge cases and invalid paths before final output.
3. Add targeted checks for edge cases and invalid paths before final output.

## 5. Day Code Snippet

Excerpt from `main.py`:
```python
response = requests.get("https://appbrewery.github.io/news.ycombinator.com")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.getText()
# print(article_text)
# <a class="storylink" href="https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm">Joan Feynman 1927-2020</a>
# Joan Feynman 1927-2020
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").text
# print(article_link)
# print(article_upvote)
# https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm
```

## 6. How to Run

```bash
python "main.py"
```

## 7. Common Pitfalls and Debug Tips

- External sites/APIs change often; verify selectors/fields before assuming parser bugs.
- Reproduce failures with the smallest input first, then expand once stable.

## 8. Practice Extensions

- Add one improvement that increases reliability (validation, retries, or explicit error handling).
- Add one improvement that increases maintainability (refactor repeated logic into helpers/services).
- Add one improvement that increases usability (clearer output, better UI feedback, or richer docs).

## 9. Key Takeaways

- **Scraping the Web with BeautifulSoup module** is strongest when the main flow is simple and each helper has one clear job.
- Real project snippets from this day should be your baseline when reviewing or extending the code.
- Historical lesson notes were preserved and translated into the new structure for continuity.

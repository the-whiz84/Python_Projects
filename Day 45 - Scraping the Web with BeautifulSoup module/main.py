from bs4 import BeautifulSoup
# import lxml  - depending of the website we might need to pass in the lxml.parser instead

# with open("./website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

# for tag in all_anchor_tags:
#     print(tag.getText())

# The App Brewery
# My Hobbies
# Contact Me

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# https://www.appbrewery.co/
# https://angelabauer.github.io/cv/hobbies.html
# https://angelabauer.github.io/cv/contact-me.html

# heading = soup.find(name="h1", id="name")
# print(heading)
# <h1 id="name">Angela Yu</h1>

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# <h3 class="heading">Books and Teaching</h3>

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)
# <h1 id="name">Angela Yu</h1>

# headings = soup.select(".heading")
# print(headings)
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]

import requests

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
# 38 points

article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="storylink")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(int(article_upvotes[0].split()[0]))
# 38

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_upvotes = max(article_upvotes)
print(max_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(max_upvotes_index)
print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
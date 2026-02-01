# 1. Web Scraping

# Is used to look through the underline HTML code of a website to retrieve some information
# Useful when there is no API provided or the API are restrictive

# BeautifulSoup is a Python module that parses HTML content
from bs4 import BeautifulSoup
# import lxml  - depending of the website we might need to pass in the lxml.parser instead

with open("./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
<title>Angela's Personal Site</title>

print(soup.title.name)
title

print(soup.title.string)
Angela's Personal Site

# The entire soup object is all of the HTML code

print(soup)

# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <title>Angela's Personal Site</title>
# </head>
# <body>
# <h1 id="name">Angela Yu</h1>
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# <p>I am an iOS and Web Developer. I love coffee and motorcycles.</p>
# <hr/>
# <h3 class="heading">Books and Teaching</h3>
# <ul>
# <li>The Complete iOS App Development Bootcamp</li>
# <li>The Complete Web Development Bootcamp</li>
# <li>100 Days of Code - The Complete Python Bootcamp</li>
# </ul>
# <hr/>
# <h3 class="heading">Other Pages</h3>
# <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
# <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
# </body>
# </html>

print(soup.prettify())

# <!DOCTYPE html>
# <html>
#  <head>
#   <meta charset="utf-8"/>
#   <title>
#    Angela's Personal Site
#   </title>
#  </head>
#  <body>
#   <h1 id="name">
#    Angela Yu
#   </h1>
#   <p>
#    <em>
#     Founder of
#     <strong>
#      <a href="https://www.appbrewery.co/">
#       The App Brewery
#      </a>
#     </strong>
#     .
#    </em>
#   </p>
#   <p>
#    I am an iOS and Web Developer. I love coffee and motorcycles.
#   </p>
#   <hr/>
#   <h3 class="heading">
#    Books and Teaching
#   </h3>
#   <ul>
#    <li>
#     The Complete iOS App Development Bootcamp
#    </li>
#    <li>
#     The Complete Web Development Bootcamp
#    </li>
#    <li>
#     100 Days of Code - The Complete Python Bootcamp
#    </li>
#   </ul>
#   <hr/>
#   <h3 class="heading">
#    Other Pages
#   </h3>
#   <a href="https://angelabauer.github.io/cv/hobbies.html">
#    My Hobbies
#   </a>
#   <a href="https://angelabauer.github.io/cv/contact-me.html">
#    Contact Me
#   </a>
#  </body>
# </html>

print(soup.a) # returns the first anchor type it finds

<a href="https://www.appbrewery.co/">The App Brewery</a>


# 2. Finding and Selecting particular Elements with BeautifulSoup


# BeautifulSoup has a method called find_all and we pass in search parameters like name 

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# returns a list
[<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]


# If we want to get only the text from the tags, we use a for loop

# for tag in all_anchor_tags:
#    print(tag.getText())

The App Brewery
My Hobbies
Contact Me

# for tag in all_anchor_tags:
#    print(tag.get("href"))

https://www.appbrewery.co/
https://angelabauer.github.io/cv/hobbies.html
https://angelabauer.github.io/cv/contact-me.html


# We can search for specific elements by adding multiple search filters

# heading = soup.find(name="h1", id="name")
# print(heading)
<h1 id="name">Angela Yu</h1>

# We can also search for elements of a certain class but the name we use is class_ so that Python doesn't think that we want to create a new class

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
<h3 class="heading">Books and Teaching</h3>


# In order to do more refined searches we can also search by CSS selectors

# This anchor tag sits inside a paragraph element
# company_url = soup.select_one(selector="p a")
# print(company_url)
<a href="https://www.appbrewery.co/">The App Brewery</a>

# Using id
# name = soup.select_one(selector="#name")
# print(name)
<h1 id="name">Angela Yu</h1>

# Using class
# headings = soup.select(".heading")
# print(headings)
[<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]


# 3. Scraping a live website

# We get the html data of a live website using requests module

import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# To get the title of the first article in the list
article_text = soup.find(name="a", class_="storylink")
print(article_text)
<a class="storylink" href="https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm">Joan Feynman 1927-2020</a>

# To get article link and article score
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").text
print(article_link)
print(article_upvote)
https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm
38 points


# To get all of the article data:

# article_texts = []
# article_links = []
# articles = soup.find_all(name="a", class_="storylink")
# for article_tag in articles:
#    text = article_tag.getText()
#    article_texts.append(text)
#    link = article_tag.get("href")
#    article_links.append(link)

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)
['Joan Feynman 1927-2020', 'Court dismisses Genius lawsuit over lyrics-scraping by Google', "Facebook's new policy bans blackface and some Jewish stereotypes", 'Parallel Seam Carving', "Amazon's business model meets Sweden's labor unions", "3D Printing Integrated Circuits: What's Possible Now and in the Future?", 'Ask HN: How Belarus can keep connected despite internet blackout?', 'Systems Monitoring with Prometheus and Grafana', 'A Keyboard with Blank Keycaps Made Me and Expert Typist', 'JuliaDB', 'Predictions as a Substitute for Reviews', "Let's Build a 28-Core Raspberry Pi Cluster", 'Pumas AI: A platform for pharmaceutical modeling and simulation', 'Mitochondria may hold keys to anxiety and mental health', 'NetSurf, a multi-platform web browser', 'Launch HN: Xkit (YC S18) - OAuth infrastructure as a service', 'A broken cable smashed a hole 100 feet wide in the Arecibo Observatory', 'The Sail ISA specification language', 'Single Page Applications in Rust', 'Deplacy: CUI-Based Tree Visualizer for Universal Dependencies', 'Show HN: Radius – A Meetup.com alternative', 'Brain circuit scores identify clinically distinct biotypes in depression /anxiety', 'Astronomers see a black hole awaken in real time', 'Safe Superintelligence Inc.\n                    ', "How airplanes counteract St. Elmo's Fire during thunderstorms", 'Datadog releases Incident Management, Profiler, Error Tracking, and more', 'How to stop procrastinating by using the Fogg Behaviour Model', 'Mozilla lays off 250 employees while it refocuses on commercial products', 'ZX Spectrum Next - Issue 2', 'A network of 17th-century female spies (2019)']

['https://www.aps.org/archives/publications/apsnews/202008/feynman.cfm', 'https://techcrunch.com/2020/08/11/court-dismisses-genius-lawsuit-over-lyrics-scraping-by-google/', 'https://doi.org/10.1016/j.jasrep.2024.104636', 'https://v2thegreat.com/2024/06/19/lessons-learned-from-scaling-to-multi-terabyte-datasets/', 'https://hakaimagazine.com/videos-visuals/rice-farming-gets-an-ai-upgrade/', 'https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/', 'https://tech.marksblogg.com/yolo-umbra-sar-satellites-ship-detection.html', 'https://twitter.com/lemire/status/1803598132334436415', 'https://futureforum.com/2022/07/15/personal-user-manual/', 'http://www.chrisfenton.com/1-25-scale-cray-c90-wristwatch/', 'https://www.carabinercollection.com/', 'https://github.com/home-sweet-gnome/dash-to-panel', 'https://scottaaronson.blog/?p=710', 'https://stackdiary.com/eu-council-has-withdrawn-the-vote-on-chat-control/', 'https://osrd.fr/en/', 'https://english.elpais.com/climate/2024-06-13/the-30-meter-pass-in-the-pyrenees-through-which-millions-of-insects-migrate.html', 'https://easyos.org/', 'https://www.npr.org/2024/06/10/1247296780/screen-apnea-why-screens-cause-shallow-breathing', 'https://hypermedia.systems/', 'https://github.com/MrKai77/Loop', 'https://www.radius.to', 'https://www.nature.com/articles/s41591-024-03057-9', 'https://www.eso.org/public/germany/news/eso2409/', 'https://ssi.inc', 'https://www.technologyreview.com/2024/06/19/1093446/pneumatic-tubes-hospitals/', 'https://salvagedcircuitry.com/2000a-nand-recovery.html', 'https://news.mit.edu/2024/computer-science-professor-arvind-dies-0618', 'https://blog.mozilla.org/en/mozilla/changing-world-changing-mozilla/', 'https://spectrum.ieee.org/vannevar-bush', 'https://www.ycombinator.com/companies/zep-ai/jobs/J5TD9KW-backend-engineer']

['38 points', '205 points', '165 points', '19 points', '57 points', '40 points', '58 points', '138 points', '29 points', '189 points', '46 points', '108 points', '103 points', '201 points', '188 points', '110 points', '46 points', '25 points', '752 points', '3 points', '242 points', '161 points', '230 points', '1051 points', '30 points', '156 points', '585 points', '1312 points', '24 points', '60 points']

# We use the split method on the score to get an integer only


article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(int(article_upvotes[0].split()[0]))
38

# Getting the article and link for the most upvotes

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# max_upvotes = max(article_upvotes)
# print(max_upvotes)
1312
# max_upvotes_index = article_upvotes.index(max_upvotes)
# print(max_upvotes_index)
27
# print(article_texts[max_upvotes_index])
# print(article_links[max_upvotes_index])

Mozilla lays off 250 employees while it refocuses on commercial products
https://blog.mozilla.org/en/mozilla/changing-world-changing-mozilla/
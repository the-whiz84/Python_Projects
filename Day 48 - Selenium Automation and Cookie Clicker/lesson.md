# Day 48 - Selenium Automation and Cookie Clicker

Day 48 is the point where browser automation becomes a different category of problem from ordinary scraping. With `requests` and BeautifulSoup, we download HTML and inspect it. With Selenium, we launch a real browser, wait for the page to render, locate visible elements, and trigger user actions such as typing, clicking, and pressing Enter.

That extra power is why a little generic theory is useful here. Selenium is not just another parsing library. It works through the browser automation stack, where Python sends commands to WebDriver and WebDriver controls Chrome for us. Once you understand that model, the rest of the lesson becomes much easier to reason about.

## 1. Why Selenium Exists

The earlier scraping projects were built around one assumption: the data we want is already present in the HTML returned by `requests.get()`. Modern websites often break that assumption. Some pages build parts of the interface with JavaScript after the initial request, and many tasks require interaction rather than passive reading.

That is the gap Selenium fills. Instead of asking Python to imitate a browser request, we ask Python to control an actual browser session:

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
```

This is an important conceptual step. `driver` is not parsed HTML. It is an object representing a live browser. That means the program can do things a human would do in the same page: wait for rendering, inspect elements, click buttons, and submit forms.

## 2. Understanding the WebDriver Model

Selenium usually feels easier once you stop thinking about it as "magic Python that knows the browser" and start thinking about it as a client-server system.

- your Python script is the client
- the browser driver is the automation server
- Chrome is the application being controlled

When Python calls `driver.get(...)` or `find_element(...)`, Selenium sends a command through the WebDriver protocol. Chrome then performs the action and returns the result. That design is why Selenium can automate real websites instead of just parsing text.

The `detach=True` option is also worth understanding. Normally, the browser closes when the script exits. Detaching the browser keeps the window open so you can inspect what the automation just did. For learning and debugging, that is extremely helpful.

## 3. Locators: How Selenium Finds the Right Element

Once the page is open, Selenium needs a stable way to find elements. This is where the `By` class comes in:

```python
from selenium.webdriver.common.by import By

search_bar = driver.find_element(By.NAME, value="q")
button = driver.find_element(By.ID, value="submit")
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
bug_report = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
```

These four lines are a good mini-tour of locator strategy.

- `By.ID` is usually the cleanest and most stable option.
- `By.NAME` is common for forms and search fields.
- `By.CSS_SELECTOR` is flexible and readable when IDs are unavailable.
- `By.XPATH` is powerful, but often the most fragile because it can depend on the exact page structure.

This is one of the first lessons in browser automation that really benefits from some theory. A locator is not just a way to "make the code work." It is a maintenance decision. If the page changes slightly next week, a brittle XPath may fail while an ID-based locator keeps working.

## 4. Elements Become Objects You Can Inspect

When Selenium finds an element, it returns a `WebElement` object. That object gives you information about the node and lets you interact with it.

In `main.py`, the project demonstrates that with a few quick inspections:

```python
search_bar = driver.find_element(By.NAME, value="q")
button = driver.find_element(By.ID, value="submit")

# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# print(button.size)
```

This is a useful teaching moment because Selenium does not treat the DOM as plain text. It exposes elements as Python objects with properties and methods. That makes browser automation feel much closer to object interaction than traditional scraping.

## 5. Sending Keyboard Input and Triggering Browser Events

A browser bot becomes useful when it can do more than read the page. In `interaction.py`, Selenium fills the Wikipedia search box and submits it with the keyboard:

```python
from selenium.webdriver.common.keys import Keys

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
```

This small example teaches a larger principle: in Selenium, typing is an event, not just string assignment. `send_keys()` simulates real keyboard input, which means websites can react with the same JavaScript handlers they would use for a human user.

That distinction matters later in the course when we automate login forms, search flows, and multi-step interfaces.

## 6. Cookie Clicker Turns Selenium into a Control Loop

The second script in this folder moves from single actions to repeated automation. Instead of opening a page and locating a few elements, `main_cookie_clicker_bot.py` runs an endless loop, keeps track of time, and makes decisions about upgrades while the game is running.

The setup phase gathers the key pieces of state:

```python
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 6
five_min = time.time() + 60 * 5
```

That code is doing more than setup:

- it stores the clickable cookie element
- it collects every store item once, up front
- it precomputes the upgrade IDs
- it creates two timer checkpoints for periodic buying and final shutdown

This is a strong example of Python automation design. Instead of querying everything from scratch on every loop iteration, the script separates one-time setup from repeated actions.

## 7. Choosing the Best Affordable Upgrade

The `buy_upgrades()` function contains the real decision-making logic:

```python
all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
item_prices = []

for price in all_prices:
    element_text = price.text
    if element_text != "":
        cost = int(element_text.split("-")[1].strip().replace(",", ""))
        item_prices.append(cost)
```

This section is worth expanding because it combines several Python ideas at once:

- Selenium retrieves the visible text from each store row.
- String cleanup removes labels, spaces, and commas.
- `int(...)` converts the cleaned price into a number.
- Python data structures turn that scraped data into a decision model.

The next part creates a dictionary mapping prices to store item IDs, checks the current cookie balance, filters the affordable upgrades, and buys the most expensive option available:

```python
cookie_upgrades = {}
for n in range(len(item_prices)):
    cookie_upgrades[item_prices[n]] = item_ids[n]

money_element = driver.find_element(by=By.ID, value="money").text
if "," in money_element:
    money_element = money_element.replace(",", "")
cookie_count = int(money_element)
```

This is a good example of why automation projects often feel more advanced than the individual syntax they use. The logic is built from familiar tools like loops, dictionaries, conditionals, and type conversion. What makes it interesting is the context: those basics are now driving a live browser session.

## 8. Time-Based Automation Is a New Pattern

The main loop introduces another important concept:

```python
while True:
    cookie.click()

    if time.time() > timeout:
        buy_upgrades()
        timeout = time.time() + 6

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        driver.quit()
        break
```

This is no longer a script that runs top to bottom once. It is a timed control loop. The bot keeps performing one fast action, pauses periodically to reassess the game state, and stops after a fixed duration.

That pattern shows up again and again in automation work:

- poll the current state
- decide whether a condition has changed
- take the next action
- repeat until a stop condition is reached

So even though Cookie Clicker is playful, the design pattern is very real.

## How to Run the Project

Install Selenium if needed:

```bash
pip install selenium
```

Run the basic locator demo:

```bash
python main.py
```

Run the Wikipedia interaction example:

```bash
python interaction.py
```

Run the Cookie Clicker bot:

```bash
python main_cookie_clicker_bot.py
```

Chrome and the matching ChromeDriver setup need to be available on your machine for Selenium to launch the browser correctly.

## Summary

Day 48 introduces browser automation as a new category of Python work. Selenium uses WebDriver to control a real browser, locators determine how reliably you can target page elements, and `WebElement` methods let the script trigger real browser events. The Cookie Clicker bot then turns those building blocks into a control loop with timing, state, and decision-making. That combination of browser control plus ordinary Python logic is the foundation for the much more realistic automation projects that follow.

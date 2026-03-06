# Day 48 - Browser Automation with Selenium: Locators and Actions

Over the last few projects, we've used `BeautifulSoup` to "scrape" data. But there is a fundamental limit to what BeautifulSoup can accomplish: it cannot execute JavaScript. If a website relies heavily on React, Angular, or Vue to render its content, or if you need to actually _perform actions_ (clicking, typing, logging in, navigating complex flows), you need something that controls a physical web browser.

That's where **Selenium** comes in. Think of it as an enterprise-grade remote control for Chrome.

## The Selenium Setup: Understanding Webdriver

Unlike `requests` (which just downloads a string of text), Selenium launches an entire instance of Chrome under the hood using a binary called `chromedriver`. Selenium Python code sends commands over a network protocol to `chromedriver`, which then physically manipulates the browser interface.

```python
from selenium import webdriver

# We must initialize options to manage the Chrome process
chrome_options = webdriver.ChromeOptions()

# By default, Chrome closes the instant the Python script finishes executing.
# We set 'detach' to True to orphan the browser process, keeping it alive for us to inspect.
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
```

## Finding Elements on the Page: The Fragility Hierarchy

Once the DOM is rendered, we use the `By` class to instruct Selenium on exactly which node to target. Finding elements in UI automation requires choosing the most "stable" locator possible. If the engineers who built the website update their codebase next week, you want your script to survive the update.

Here is the hierarchy of locators, ordered from most resilient to most fragile:

### 1. By ID and Name (Highly Resilient)

Engineers rarely change foundational IDs and Names because they are tied directly to backend database schemas and form submissions. Always use these first if available:

```python
search_bar = driver.find_element(By.NAME, value="q")
submit_button = driver.find_element(By.ID, value="submit")
```

### 2. By CSS Selector (Moderately Resilient)

If there is no ID, targeting a specific CSS class hierarchy is powerful, but slightly more prone to breaking if designers rename classes during a branding update:

```python
# Finds an <a> tag nested directly inside an element with class "documentation-widget"
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
```

### 3. By XPath (Extremely Fragile)

XPath is a query language for XML. You can copy the exact XPath path of any element by right-clicking it in the Chrome Inspector. However, because it maps the exact nested tree of the page, if the website inserts a single new `<div>` above your target, the entire XPath breaks. Only use XPath when absolutely necessary:

```python
bug_report = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
```

## Interaction: Sending Keys and Clicks

Finding the element constructs a Python object referencing the physical web element. The second half is triggering events on that reference.

```python
from selenium.webdriver.common.keys import Keys

search = driver.find_element(By.NAME, value="search")

# send_keys can simulate complex keyboard events, not just strings!
search.send_keys("Python", Keys.ENTER)
```

## Building a Bot: The Cookie Clicker State Machine

The real power of Selenium shines when we combine interactions with logic. Today, we're building a bot to play the "Cookie Clicker" game.

This isn't a linear script; it's a **state machine**. We need a continuous game loop that executes rapidly while keeping track of high-level state (the clock).

The bot's polling strategy:

1. Mash the cookie constantly.
2. Set a 5-second timeout marker in the future.
3. Every time the main loop fires, check if the current time exceeds the timeout marker.
4. If it does, scrape the current balance, execute the purchase logic (buying the most expensive upgrade possible), and push the timeout marker another 5 seconds into the future.

```python
import time

timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        # Check current cookie count, strip commas, cast to integer
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

        # Determine the maximum affordable upgrade and trigger a click event
        buy_upgrades()

        # Reset the 5-second polling timer
        timeout = time.time() + 5
```

## Running the Cookie Clicker Bot

1. Open the file `main_cookie_clicker_bot.py`.
2. Run the script from your terminal:
   ```bash
   python "main_cookie_clicker_bot.py"
   ```
3. Leave your mouse alone. Watch the browser as the bot clicks with inhuman speed and strategically buys upgrades automatically!

## Summary

Selenium elevates your Python skills into the realm of Robotic Process Automation (RPA). You learned the architecture of WebDriver communication, how to strategically select DOM nodes using resilient locators, and how to govern a continuous game loop using a time-based state machine.

Tomorrow, we’re going to tackle a far more sophisticated challenge: automating a massive, real-world platform with strict security measures—applying for jobs on LinkedIn!

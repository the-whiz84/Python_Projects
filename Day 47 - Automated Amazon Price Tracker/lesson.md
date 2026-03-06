# Day 47 - Automated Amazon Price Tracker: HTTP Headers, Parsing, and Email Alerts

This project turns a one-off scraper into a practical automation. Instead of printing a page title and stopping, the script checks a live Amazon product page, extracts the current price, compares it with a target, and sends an email when the price drops low enough. That makes Day 47 a useful bridge between three ideas we have already touched separately: HTTP requests, HTML parsing, and automated notifications.

Because this is still a Python course, a little theory matters here. The script works only because Python can imitate a browser well enough to receive the page, turn the returned HTML into structured data, and then hand the result to an SMTP server. If any one of those steps fails, the automation breaks.

## 1. Why This Scraper Needs Browser Headers

The first important concept is that `requests.get()` does not magically behave like Safari or Chrome. By default, it sends a minimal request that clearly identifies itself as a Python script. Large sites such as Amazon often look at request headers before they decide whether to serve the full page, a challenge page, or an outright error.

In this project, the script adds several headers that make the request resemble a normal browser visit:

```python
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'sec-fetch-mode': "navigate",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    'Accept-Language': "en-US,en;q=0.9",
    'sec-fetch-dest': "document",
    'x-forwarded-proto': "https",
    'x-https': "on",
}

response = requests.get(URL, headers=headers)
response.raise_for_status()
```

This is a good example of Python theory meeting real-world web behavior. In class exercises, we often treat an HTTP request as "send URL, get HTML." In production-like scraping, the request metadata matters almost as much as the URL itself. The `User-Agent` string tells the server which browser is supposedly making the request. `Accept-Language` helps the request look like it came from a real person using a browser with language preferences. `response.raise_for_status()` is also important because it stops the script immediately if Amazon answers with an error page.

## 2. Turning Raw HTML into Data with BeautifulSoup and `lxml`

Once the response arrives, the next job is parsing. The script passes the downloaded bytes into BeautifulSoup and asks it to use the `lxml` parser:

```python
html_data = response.content
soup = BeautifulSoup(html_data, "lxml")
```

BeautifulSoup gives us a friendly Python interface for navigating HTML. `lxml` is the parsing engine underneath. That distinction is worth understanding:

- BeautifulSoup helps you search and traverse tags.
- `lxml` handles the low-level parsing work.

Why use `lxml` here instead of the built-in parser? Sites like Amazon produce large, complex HTML documents full of nested elements, tracking markup, and layout variations. `lxml` is faster and generally more tolerant when the markup is messy. For a learning project, this is also a helpful reminder that libraries often work in layers. One tool gives you the API, and another does the heavy lifting.

## 3. Cleaning the Product Name and Price

Scraping is rarely about finding data only once. Usually, the first half is locating the right element, and the second half is cleaning the text into a form Python can use.

This script pulls the price and product name with two separate lookups:

```python
price_data = soup.find(name="span", class_="aok-offscreen")
price_unformatted = (price_data.text).split("€")[1]
price = float(price_unformatted.split()[0])

product_name_data = soup.find(id="productTitle")
product_name = ((product_name_data.text).split(" (")[0]).strip()
```

There are a few useful lessons packed into those lines:

- `soup.find()` returns a tag object, not the final cleaned value you want.
- `.text` gives you the human-readable content inside the tag.
- real page text usually includes currency symbols, extra spaces, or descriptive text that must be removed before comparison.
- `float(...)` converts the cleaned string into a number so the program can use `<` in a meaningful way.

This is a recurring pattern in Python automation. The data you scrape is almost never in the exact shape your logic needs. Small string operations such as `split()` and `strip()` often do the final conversion from page text into program data.

## 4. The Price Alert Rule Is Just Plain Python Logic

After the scraper has a numeric price, the decision itself is simple:

```python
if price < DESIRED_PRICE:
    print("Sending price alert email....")
    message = f"Subject: Amazon Price Tracker Alert\n\nHello,\n\n {product_name} is now ${price}!\n\n{URL}"
```

This section is important because it shows how much automation depends on ordinary control flow. The project feels advanced because it touches Amazon and Gmail, but the core rule is still a basic `if` statement. That is a good lesson to keep in mind throughout the course: advanced projects usually come from combining simple Python ideas with external systems.

You can also see one practical design choice here. The threshold is stored in `DESIRED_PRICE`, which means the alert rule is easy to change without touching the scraping logic. Keeping configuration separate from logic becomes more valuable as projects grow.

## 5. Sending Mail with SMTP and Environment Variables

The final step is notification. Python uses the `smtplib` module to open a connection to Gmail's SMTP server, secure that connection with TLS, log in, and send the message:

```python
my_email = os.environ.get("MY_EMAIL")
email_password = os.environ.get("MY_EMAIL_PASSWD")

connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
with connection:
    connection.starttls()
    connection.login(user=my_email, password=email_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=message
    )
```

There are three concepts worth calling out:

First, the credentials come from environment variables instead of being hardcoded in the file. That keeps secrets out of source code and makes the script safer to store in git.

Second, `starttls()` upgrades the connection to an encrypted one before the login happens. In other words, the script is not just "sending an email"; it is participating in a real network protocol with authentication and transport security.

Third, SMTP is a good example of Python acting as glue between systems. The script scrapes data from one service and then passes the result to another service. A lot of automation work looks exactly like this.

## 6. What Makes This Project Fragile in the Real World

It is also worth being honest about the limits of this approach. Scraping retail sites is fragile because the HTML can change without warning. A class name like `"aok-offscreen"` may work today and fail later. Price formatting can also differ by region, which matters here because the script is scraping a European product page and splitting on the euro symbol.

That does not make the project a bad one. It makes it realistic. A useful scraper often needs maintenance. The skill is not just writing the first version, but also understanding where it can break and how to debug it when the site changes.

## How to Run the Project

1. Set the required environment variables:

```bash
export MY_EMAIL="your_email@gmail.com"
export MY_EMAIL_PASSWD="your_app_password"
```

2. Open [main.py](/Users/wizard/Developer/Python_Projects/Day%2047%20-%20Automated%20Amazon%20Price%20Tracker/main.py) and set the product `URL` and `DESIRED_PRICE`.
3. Install the required packages if needed:

```bash
pip install requests beautifulsoup4 lxml
```

4. Run the script:

```bash
python main.py
```

If Gmail is the sender, you will usually need an app password rather than your normal account password.

## Summary

Day 47 shows how Python automation usually works in practice: fetch data from a web page, clean it into usable values, apply a rule, and trigger an action. The theory matters here because headers explain why the request succeeds, parsing explains how HTML becomes data, and SMTP explains how the script can notify you automatically. The whole project is still powered by familiar Python basics, but now those basics are connected to real web systems.

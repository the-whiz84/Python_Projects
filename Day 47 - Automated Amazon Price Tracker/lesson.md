# Day 47 - Automated Amazon Price Tracker: Beating Bot Detection

We've already learned how to scrape data with BeautifulSoup and how to push data to an API like Spotify. Today, we're building something truly practical: an automated price tracker that watches an Amazon product for you and sends you an email the second it drops below a certain threshold.

This project introduces a massive new hurdle in web scraping: **How do you scrape websites that actively deploy anti-bot countermeasures?**

## The Anatomy of an HTTP Request: Dealing with Headers

When you type a URL into your browser, it sends an HTTP `GET` request to the server. But it doesn't just ask for the HTML file; it sends a block of "meta-information" called **Headers**. These headers tell the server your IP address, your system language, what browser you are using, and even your operating system version.

Amazon's servers look at these headers to fingerprint the incoming request. If they determine you are a human, they serve the HTML. If they determine you are a bot, they flat-out reject your connection.

If we just use a blank `requests.get()`, our script identifies itself as `"User-Agent": "python-requests/2.X.X"`. Amazon will instantly block us. We have to "dress up" our request to look like a real browser running on a real desktop:

```python
headers = {
    # The User-Agent is the single most important header for evading basic bot detection.
    # It tells Amazon exactly what browser and OS we're using.
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15...",

    # Accept-Language tells the server what languages our 'browser' prefers. A bot wouldn't usually send this.
    'Accept-Language': "en-US,en;q=0.9",

    # We can even pretend we just navigated away from a Google Search
    'Referer': 'https://www.google.com'
}

response = requests.get(URL, headers=headers)
```

You can find what your personal headers are by visiting [myhttpheader.com](https://myhttpheader.com). Including these is often the difference between executing your script successfully and getting a "403 Forbidden" or "503 Service Unavailable" error.

## Advanced DOM Parsing with LXML

You'll notice in `main.py` we're importing `lxml` and using it instead of the standard Python `html.parser`.

```python
import lxml
soup = BeautifulSoup(html_data, "lxml")
```

**Why the switch?**
The internet is messy. Massive legacy websites like Amazon are stitched together by hundreds of developers over decades. Their HTML is often malformed—missing closing tags, nested incorrectly, or polluted with tracking scripts.

The built-in `html.parser` is strict. If it hits broken HTML, it might fail or build the soup tree incorrectly. `lxml` is written in highly optimized C. It is not only significantly faster (vital if you are scraping thousands of products), but it is aggressively fault-tolerant. It will happily parse through broken DOM structures and still give you usable data. Ensure you have it installed: `pip install lxml`.

## Finding and Transforming the Price

Amazon changes its layout via A/B testing frequently, so the CSS "selector" (the class we look for) might change depending on the day or even the location you scrape from.

```python
price_data = soup.find(name="span", class_="aok-offscreen")
price_unformatted = (price_data.text).split("$")[1]

# We cast the text string to a floating-point number so we can perform comparative logic
price = float(price_unformatted.split()[0])
```

## The Email Alert: SMTP Security

When the price drops, we want to know immediately. We use `smtplib` to manage a secure connection to Google's mail servers.

```python
if price < DESIRED_PRICE:
    message = f"Subject: Amazon Price Tracker Alert\n\n{product_name} is now ${price}!\n{URL}"

    # 587 is the standard port for secure SMTP submission
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    with connection:
        # Start TLS (Transport Layer Security) to encrypt our password before we send it
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(...)
```

**Watch out—** If you're using Gmail, Google disables basic username/password logins for Python scripts. You must go into your Google Account Security settings, enable 2-Step Verification, and generate a specific 16-character **"App Password"** for your script.

## Running the Amazon Price Tracker

1. Set your environment variables in your terminal:
   ```bash
   export MY_EMAIL='your_email@gmail.com'
   export MY_EMAIL_PASSWD='your_16_char_app_password'
   ```
2. Open `main.py` and set your `URL` and `DESIRED_PRICE`.
3. Run the script:
   ```bash
   python "main.py"
   ```

## Summary

Today's architecture perfectly illustrates the "cat-and-mouse" game of web scraping. By crafting realistic HTTP headers, you bypassed server-side bot detection. By adopting `lxml`, you parsed fractured frontend code into usable data. And by implementing TLS-secured SMTP, you built an alert system that saves you actual money.

Tomorrow, we cross a threshold. We're going to dive into **Selenium**—a tool that abandons `requests` entirely and physically takes control of a real Chrome browser!

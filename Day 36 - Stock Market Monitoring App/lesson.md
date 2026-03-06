# Day 36 - Stock Market Monitoring App

Today we're building a sophisticated stock market monitoring application that tracks a company's stock price, detects significant movements, fetches related news, and sends you SMS alerts. This project combines multiple APIs (Alpha Vantage for stock data, NewsAPI for articles, Twilio for notifications) into a coherent automation pipeline.

This lesson explores how to work with financial data APIs, parse complex JSON responses, calculate meaningful metrics from raw data, and deliver actionable notifications to users.

## Understanding Stock Data APIs

Stock market data APIs provide historical and real-time information about publicly traded companies. Alpha Vantage offers free API access (with rate limits) that gives you daily stock prices, intraday data, and various technical indicators.

The core concept is simple: you ask the API for data about a specific stock (identified by a ticker symbol like "AAPL" for Apple), and it returns a structured response with prices, volumes, and timestamps.

Alpha Vantage's free tier has limitations: you can make 5 API calls per minute and 500 calls per day. For a personal stock monitor like this, that's usually sufficient. The key is designing your code to be efficient—only fetching the data you need and caching when possible.

## The API Request Structure

Here's how we construct the request to Alpha Vantage:

```python
import requests
import os

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("ALPHAVANTAGE_API_KEY"),
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()  # Raises an exception if the request failed
```

The parameters tell Alpha Vantage exactly what data we want:
- `function`: "TIME_SERIES_DAILY" requests daily price data
- `symbol`: "AAPL" specifies Apple Inc
- `apikey`: Our authentication token

## Parsing the Response

Alpha Vantage returns data in a nested dictionary structure. Understanding this structure is crucial:

```python
data = response.json()

# The data looks like:
# {
#     "Time Series (Daily)": {
#         "2024-03-15": {
#             "1. open": "175.00",
#             "2. high": "176.50",
#             "3. low": "174.25",
#             "4. close": "176.00",
#             "5. volume": "45000000"
#         },
#         "2024-03-14": { ... },
#         ...
#     }
# }

# We can convert the entire time series to a list for easier access
data_list = [value for (key, value) in data.items()]
```

The dictionary comprehension `[value for (key, value) in data.items()]` transforms the nested dictionary into a simple list, where index 0 is the most recent day, index 1 is the previous day, and so on.

## Calculating Price Movement

The key metric we care about is the percentage change between yesterday's closing price and the day before:

```python
# Get the two most recent closing prices
yesterday_closing = float(data_list[0]['4. close'])
prev_day_closing = float(data_list[1]['4. close'])

# Calculate the absolute difference
closing_difference = abs(yesterday_closing - prev_day_closing)

# Calculate percentage change
diff_percent = round((closing_difference / prev_day_closing) * 100)
```

This calculation tells us: "The stock moved X% compared to the previous day." A 5% move in either direction is generally considered significant for most stocks.

We use `abs()` (absolute value) because we care about the magnitude of movement, not just whether it went up or down. Later, we determine the direction separately:

```python
if yesterday_closing > prev_day_closing:
    arrow_direction = "🔺"  # Stock went up
else:
    arrow_direction = "🔻"  # Stock went down
```

## Fetching Related News

When we detect a significant price movement, we want to know what's causing it. NewsAPI lets us search for news about a specific company:

```python
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_parameters = {
    "apiKey": os.environ.get("NEWS_API_KEY"),
    "q": COMPANY_NAME,  # Query for the company name
    "pageSize": 3,     # Limit to top 3 articles
    "sortBy": "popularity",  # Get most popular/relevant first
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()["articles"]

# Format each article for SMS
news_list = []
for item in news_data:
    headline = item["title"]
    brief = item["description"]
    url = item["url"]
    
    formatted = f"Headline: {headline}\n\nBrief: {brief}\n\n{url}"
    news_list.append(formatted)
```

NewsAPI returns an "articles" array, where each article has a title, description, source, author, URL, and published timestamp. We format this into a concise message suitable for SMS.

## Sending Structured Alerts

Now we combine everything into a comprehensive alert:

```python
from twilio.rest import Client
import os

# Only send if the price moved significantly (more than 1% in our case)
if diff_percent > 1:
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    
    # Format the main alert with stock movement
    stock_alert = f"{STOCK}: {arrow_direction}{diff_percent}%"
    
    # Send each news article as a separate message
    for article in news_list:
        message = client.messages.create(
            from_=f"whatsapp:{os.environ.get('TWILIO_PHONE_NUMBER')}",
            body=f"{stock_alert}\n\n{article}",
            to=f"whatsapp:{os.environ.get('MY_PHONE_NUMBER')}"
        )
        
        print(f"Sent: {message.status}")
```

The message format looks like this:
```
AAPL: 🔺3%

Headline: Apple Reports Record Q4 Earnings
Brief: Apple Inc. announced quarterly earnings that exceeded analyst expectations...

https://news.com/article-url
```

## Error Handling and Edge Cases

When building real applications that depend on external services, you must handle various failure scenarios:

```python
try:
    # Try to get stock data
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()
    
    # Check if we got valid data
    if "Time Series (Daily)" not in stock_data:
        print("API returned unexpected format")
        # This might happen if the API key is invalid or rate-limited
        
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
    
except KeyError as e:
    print(f"Unexpected response structure: {e}")
```

Common issues include:
- **Rate limiting**: Alpha Vantage limits free tier to 5 calls/minute
- **Invalid API keys**: Check that your key is correct and hasn't expired
- **Market holidays**: No data for weekends/holidays (API returns empty Time Series)
- **API changes**: Services occasionally change their response format

## Architectural Patterns

This project demonstrates several important architectural patterns:

**1. Pipeline Architecture**
```
External APIs → Data Processing → Business Logic → Notifications
```

Each stage is independent. You could swap the notification method (SMS → email → push notification) without changing the data processing logic.

**2. Environment-Based Configuration**
```python
# Configuration lives in environment variables
API_KEYS = {
    "stock": os.environ.get("ALPHAVANTAGE_API_KEY"),
    "news": os.environ.get("NEWS_API_KEY"),
    "twilio": os.environ.get("TWILIO_AUTH_TOKEN"),
}
```

This makes your code portable—you can run it in different environments (development, production) without changing the code.

**3. Conditional Execution**
```python
if should_send_notification(condition):
    send_notification()
```

We only send alerts when meaningful events occur, avoiding notification fatigue.

## Extending the Application

Here are ways you could extend this stock monitor:

1. **Multiple stocks**: Loop through a list of tickers and check each one
2. **Different thresholds**: Allow different alert thresholds per stock
3. **Technical indicators**: Add moving averages, RSI, or MACD calculations
4. **Time-based alerts**: Only check during market hours
5. **Persistent storage**: Save historical alerts to a database for review
6. **Email support**: Add email notifications alongside SMS

## Try It Yourself

```bash
python "main.py"
```

Before running, set these environment variables:
```bash
export ALPHAVANTAGE_API_KEY="your_alphavantage_key"
export NEWS_API_KEY="your_newsapi_key"
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_PHONE_NUMBER="+1234567890"
export MY_PHONE_NUMBER="+1987654321"
```

The script will check Apple's stock, and if it moved more than 1%, send you the latest news about the company.

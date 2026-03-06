# Day 36 - Market Data Monitoring and Event-Based Notifications

Day 36 takes the alerting pattern from the previous lessons and applies it to market data. The script watches a stock, measures whether the price moved enough to matter, fetches related news if it did, and sends those headlines through Twilio. The important lesson is how to turn raw external data into a threshold-based event.

## 1. Reducing Historical Stock Data to a Single Signal

The script begins by requesting daily stock data:

```python
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
```

From there, it compares the two most recent closing prices:

```python
yesterday_closing = data_list[0]['4. close']
prev_day_closing = data_list[1]['4. close']
closing_difference = abs(float(yesterday_closing) - float(prev_day_closing))
diff_percent = round((closing_difference / float(prev_day_closing)) * 100)
```

This is the core reduction step of the project. A large API response gets turned into one number: percentage movement between the last two closes.

That is what makes the app useful. Most monitoring scripts are built around this same idea of compressing a noisy data source into one decision metric.

## 2. Turning a Metric into a Trigger

The stock movement only matters if it crosses a threshold:

```python
if diff_percent > 1:
```

Once the threshold is crossed, the script adds a direction marker:

```python
arrow_direction = ""
if yesterday_closing > prev_day_closing:
    arrow_direction = "🔺"
else:
    arrow_direction = "🔻"
```

This is a small detail, but it improves the notification immediately. The alert does not only say that the stock moved. It also tells the user whether the move was up or down.

## 3. Pulling Context from a Second API

After the price trigger fires, the script asks NewsAPI for articles about the company:

```python
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
data = news_response.json()["articles"]
```

Then it formats a short list of summaries:

```python
news_list = [
    f'Headline: {item["title"]}.\n\nBrief: {item["description"]}\n\n{item["url"]}'
    for item in data
]
```

This is the part that makes the alert actionable. A percentage move alone tells you something happened. The news articles help explain why it might have happened.

That is a useful general pattern for automation: first detect the event, then attach enough context for the user to act on it.

## 4. Sending One Notification per Article

The Twilio loop sends each article as a separate message:

```python
client = Client(account_sid, auth_token)
for article in news_list:
    message = client.messages.create(
        from_=f"whatsapp:{twilio_no}",
        body=f"{STOCK}: {arrow_direction}{diff_percent}%\n\n{article}",
        to=f"whatsapp:{my_tel_no}"
    )
```

This is a clean design because the message template is consistent:

- stock symbol
- direction and percent change
- one article summary

That structure keeps the notification readable even though it is assembled from multiple services.

## How to Run the Project

1. Open a terminal in this folder.
2. Configure the required API keys and Twilio credentials.
3. Run:

```bash
python main.py
```

4. Verify that when the movement threshold is exceeded, the script fetches the latest articles and sends formatted WhatsApp alerts.

## Summary

Day 36 turns stock data into an event-driven notification workflow. The script compares two closing prices, calculates percentage movement, uses that number as a trigger, fetches related news, and sends structured alerts through Twilio. The main lesson is how to turn a stream of external data into a meaningful event plus context.

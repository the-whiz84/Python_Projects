import requests
from twilio.rest import Client
import os

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NO = os.environ.get("TWILIO_WHATSAPP_NO")
MY_TEL_NO = os.environ.get("MY_TEL_NO")


def get_stocks():
    """_summary_ Call the Alpha Vantage API to check the last 2 days stock value for provided STOCK.
    Calculate the closing time difference and return it as a percentage.

    Returns:
        _type_: int
    """
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }

    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()
    data = stock_response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_closing = data_list[0]['4. close']
    prev_day_closing = data_list[1]['4. close']
    closing_difference = float(yesterday_closing) - float(prev_day_closing)
    diff_percent = round((closing_difference / float(prev_day_closing)) * 100)
    return diff_percent


def get_news():
    """_summary_ For the given STOCK, get the most popular 3 news headlines and descriptions and return them in 
    a formatted list.

    Returns:
        _type_: list
    """
    news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "pageSize": "3",
    "sortBy": "popularity",
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    data = news_response.json()["articles"]
    news_list = [f'Headline: {item["title"]}.\n\nBrief: {item["description"]}\n\n{item["url"]}' for item in data]
    return news_list


arrow_direction = None
if get_stocks() > 0:
	arrow_direction = "🔺"
else:
	arrow_direction = "🔻"

if abs(get_stocks()) >= 5:
    get_news()
	
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in get_news():
        message = client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NO}",
            body=f"{STOCK}: {arrow_direction}{get_stocks()}%\n\n{article}",
            to=f"whatsapp:{MY_TEL_NO}"
        )
        print(message.status)

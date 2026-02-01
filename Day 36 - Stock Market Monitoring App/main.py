import requests
from twilio.rest import Client
import os
# import datetime as dt

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_no = os.environ.get("TWILIO_TEL_NO")
my_tel_no = os.environ.get("MY_TEL_NO")


stock_parameters = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK,
	"apikey": STOCK_API_KEY,
}

news_parameters = {
	"apiKey": NEWS_API_KEY,
	"q": COMPANY_NAME,
	"pageSize": "3",
	"sortBy": "popularity",
}
## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

# def stock_variation() -> float:
	# current_date = dt.date.today()
	# yesterday_time_delta = 1
	# prev_time_delta = 2
	# yesterday_date = (current_date - dt.timedelta(yesterday_time_delta)).strftime('%Y-%m-%d')
	# prev_day_date = (current_date - dt.timedelta(prev_time_delta)).strftime('%Y-%m-%d')
	#
	# response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
	# response.raise_for_status()
	# data = response.json()["Time Series (Daily)"]
	#
	# while yesterday_date not in data:
	# 	yesterday_time_delta += 1
	# 	yesterday_date = (current_date - dt.timedelta(yesterday_time_delta)).strftime('%Y-%m-%d')
	#
	# while prev_day_date not in data:
	# 	prev_time_delta += 1
	# 	prev_day_date = (current_date - dt.timedelta(prev_time_delta)).strftime('%Y-%m-%d')

	# recent_closing = round(float(data[yesterday_date]['4. close']), 2)
	# prev_closing = round(float(data[prev_day_date]['4. close']), 2)
	# closing_difference = recent_closing - prev_closing
	# percent_change = round((closing_difference / recent_closing) * 100, 2)
	# return percent_change
#
# if stock_variation() <= -5 or stock_variation() >= 5:
# 	print("Get News")

## Angela's solution

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing = data_list[0]['4. close']
prev_day_closing = data_list[1]['4. close']
closing_difference = abs(float(yesterday_closing) - float(prev_day_closing))
diff_percent = round((closing_difference / float(prev_day_closing)) * 100)


arrow_direction = ""
if yesterday_closing > prev_day_closing:
	arrow_direction = "🔺"
else:
	arrow_direction = "🔻"

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

if diff_percent > 1:
	news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
	news_response.raise_for_status()
	data = news_response.json()["articles"]
	news_list = [f'Headline: {item["title"]}.\n\nBrief: {item["description"]}\n\n{item["url"]}' for item in data]
	print(news_list)
	## STEP 3: Use twilio.com/docs/sms/quickstart/python
	# Send a separate message with each article's title and description to your phone number.
	#HINT 1: Consider using a List Comprehension.
	client = Client(account_sid, auth_token)
	for article in news_list:
		message = client.messages.create(
			from_=f"whatsapp:{twilio_no}",
			body=f"{STOCK}: {arrow_direction}{diff_percent}%\n\n{article}",
			to=f"whatsapp:{my_tel_no}"
		)
		print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


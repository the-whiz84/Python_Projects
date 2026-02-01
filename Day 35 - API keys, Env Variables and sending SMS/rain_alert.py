import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# MY_LAT = 45.649490
# MY_LONG = 25.606550
MY_LAT = 44.351131  #testing location where it rains
MY_LONG = 2.573550	#testing location where it rains

parameters = {
	"lat": MY_LAT,
	"lon": MY_LONG,
	"appid": api_key,
	"units": "metric",
	"cnt": 4,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

id_list = [item["weather"][0]["id"] for item in weather_data]
will_rain = False

for i in id_list:
	if i < 700:
		will_rain = True

if will_rain:
	client = Client(account_sid, auth_token)
	#SMS
	# message = client.messages.create(
	# 	body="It will rain today. Take an ☔️ with you!",
	# 	from_=os.environ.get("TWILIO_PHONE_NUMBER"),
	# 	to=os.environ.get("MY_PHONE_NUMBER"),
	# )
	# Whatsapp
	message = client.messages.create(
		from_='whatsapp:' + os.environ.get("TWILIO_PHONE_NUMBER"),
		body='It will rain today. Take an ☔️ with you!',
		to='whatsapp:' + os.environ.get("MY_PHONE_NUMBER")
	)
	print(message.status)
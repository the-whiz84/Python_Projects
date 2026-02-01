# 1. API - Application Programming Interfaces

# An API is a set of commands, functions, protocols and objects that programmers can use to create software or interact with an external system.

# API endpoint
# api.coinbase.com

# API Request - the way we format the request to get a response
# API Response - the data returned if the request is valid

import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# <Response [200]>


# 2. Working with Responses: HTTP codes, Exceptions and JSON data

# 1xx: Hold On
# 2xx: OK, here you go
# 3xx: Go Away, permission required
# 4xx: You Screwed Up (404 - doesn't exist)
# 5xx: I Screwed Up (server is down/ not responding)

# if response.status_code != 200:
# 	raise Exception("Bad Response from ISS API.")
# Exception: Bad Response from ISS API.

# if response.status_code == 404:
# 	raise Exception("That resource does not exist.")
# elif response.status_code == 401:
# 	raise Exception("You are not authorized to access this data.")

# Instead we use the built in requests module to provide feedback
# response.raise_for_status()
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json

# To get the actual JSON data we use another method
# data = response.json()
# print(data)
# {'message': 'success', 'iss_position': {'latitude': '28.4964', 'longitude': '96.4349'}, 'timestamp': 1725207386}

# data = response.json()
# # print(data)
# # {'latitude': '31.4100', 'longitude': '99.6190'}
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
# ('109.0416', '38.5070')


# 3. Understand API parameters: Match Sunset times with current time
from datetime import datetime

MY_LAT = 45.668330
MY_LONG = 25.596650
parameters = {
	"lat": MY_LAT,
	"lng": MY_LONG,
	"formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunset)
# 4:57:03 PM
time_now = datetime.now()
# print(time_now)
# 2024-09-01 19:52:11.469996
# By adding the formatted parameter we get something similar
# 2024-09-01T16:57:03+00:00

# print(sunset.split("T")[1].split(":")[0])
# ['16', '57', '03+00', '00']

print(sunrise)
print(sunset)
print(time_now.hour)
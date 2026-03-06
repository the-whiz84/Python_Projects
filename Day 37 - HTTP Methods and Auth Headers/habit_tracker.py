import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	# "id": GRAPH_ID,
	# "name": "Coding Graph",
	"unit": "hours",
	"type": "float",
	# "color": "ajisai",
	# "timezone": "Europe/Bucharest",
}

headers = {
	"X-USER-TOKEN": TOKEN
}

today_date = datetime(year=2024, month=9, day=4).strftime("%Y%m%d")
# print(today_date.strftime("%Y%m%d"))

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

coding_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# coding_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today_date}"

pixel_config = {
	"date": today_date,
	"quantity": "4.5",
}
#
response = requests.post(url=coding_graph_endpoint, headers=headers, json=pixel_config)
print(response.text)

# response = requests.put(url=coding_graph_endpoint, headers=headers, json=pixel_config)
# print(response.text)

# response = requests.delete(url=f"{coding_graph_endpoint}/{today_date}", headers=headers)
# print(response.text)
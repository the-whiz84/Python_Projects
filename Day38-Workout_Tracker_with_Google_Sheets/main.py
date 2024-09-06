import requests, os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 185
AGE = 40

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

exercise = input("Tell me what exercises you did: ")

nutritionix_headers = {
	"x-app-id": NUTRITIONIX_APP_ID,
	"x-app-key": NUTRITIONIX_API_KEY,
}

exercise_params = {
	"query": exercise,
	"gender": GENDER,
	"weight_kg": WEIGHT_KG,
	"height_cm": HEIGHT_CM,
	"age": AGE,
}

workout_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=exercise_params)
workout_response.raise_for_status()
workout = workout_response.json()["exercises"]

sheety_headers = {
	"Authorization": f"Bearer {SHEETY_TOKEN}",
	"Content-Type": "application/json",
}

for exercise in workout:
	sheet_body = {
		"workout": {
			"date": today_date,
			"time": today_time,
			"exercise": exercise["name"].title(),
			"duration": exercise["duration_min"],
			"calories": exercise["nf_calories"]
		}
	}
	sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheet_body)
	print(sheety_response.text)

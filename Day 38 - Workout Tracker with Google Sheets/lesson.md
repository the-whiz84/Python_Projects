# Day 38 - Workout Tracker with Google Sheets and Natural Language Processing

Today we're building a sophisticated workout tracker that takes natural language input ("I ran 5 miles and did 30 minutes of yoga"), uses artificial intelligence to understand what exercises you performed, calculates calories burned, and stores everything in a Google Sheet.

This project demonstrates several powerful concepts: natural language processing through APIs, using Google Sheets as a database, and building data pipelines that transform human input into structured data.

## Understanding the Architecture

The application consists of three main components:

1. **Input Layer**: User enters exercise description in natural language
2. **Processing Layer**: Nutritionix API parses the text and extracts exercise data
3. **Storage Layer**: Sheety API writes the data to Google Sheets

This is a classic ETL (Extract, Transform, Load) pattern that appears throughout data engineering and automation.

## Natural Language Processing with Nutritionix

The Nutritionix API is remarkable because it can understand freeform text describing physical activities. You don't need to fill out forms or select from dropdowns—just type what you did.

```python
import requests
import os

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# These headers identify your application to Nutritionix
nutritionix_headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
}

# The user types their workout in plain English
exercise = input("Tell me what exercises you did: ")
# Example: "I ran 3 miles and cycled for 30 minutes"

# Additional parameters help the API give more accurate results
exercise_params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 75.0,
    "height_cm": 175.0,
    "age": 30
}

# Send the request
response = requests.post(
    url=NUTRITIONIX_ENDPOINT, 
    headers=nutritionix_headers, 
    json=exercise_params
)

# Parse the response
exercises = response.json()["exercises"]
```

The response contains structured data for each exercise detected:

```python
# Example response structure:
# {
#     "exercises": [
#         {
#             "tag_id": 59,
#             "user_input": "ran",
#             "duration_min": 30,
#             "met": 9.8,
#             "nf_calories": 294.71,
#             "total_calories": 294.71,
#             "name": "running",
#             "description": null
#         },
#         {
#             "tag_id": 119,
#             "user_input": "cycled",
#             "duration_min": 30,
#             "met": 7.5,
#             "nf_calories": 225.31,
#             "name": "biking",
#             "description": null
#         }
#     ]
# }
```

Each exercise in the response includes:
- `name`: The type of exercise ("running", "biking", etc.)
- `duration_min`: How many minutes
- `nf_calories`: Calories burned (Nutriix's calculation)
- `met`: Metabolic Equivalent of Task (a measure of exercise intensity)

This is incredibly powerful because the user doesn't need to know the MET values or calculate anything—they just type what they did.

## Why Personal Parameters Matter

You'll notice we pass `gender`, `weight_kg`, `height_cm`, and `age` to the API. These matter because calorie calculations depend on body composition:

```python
exercise_params = {
    "query": exercise,
    "gender": "male",        # Males typically burn fewer calories
    "weight_kg": 75.0,      # Heavier people burn more
    "height_cm": 175.0,     # Height affects BMR
    "age": 30              # Younger people generally have higher BMR
}
```

The API uses these values along with the exercise MET value to calculate calories. A 150-pound person doing 30 minutes of running burns different calories than a 200-pound person doing the same exercise.

## Google Sheets as a Database

Sheety (https://sheety.co) is a service that converts Google Sheets into a REST API. This is brilliant for small-to-medium data storage needs because:

1. **No database setup**: Just create a Google Sheet
2. **Visual data**: You can see and edit data in Excel/Sheets format
3. **Built-in sharing**: Easy to collaborate with others
4. **Free tier**: Sufficient for personal projects

### Setting Up Sheety

1. Create a Google Sheet with headers:
   - Date | Time | Exercise | Duration | Calories

2. Go to Sheety.co and connect your sheet
3. Get your API endpoint URL and authentication token

### Reading from Google Sheets

```python
import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

# Get all rows
response = requests.get(SHEETY_ENDPOINT, headers=sheety_headers)
data = response.json()

# data looks like:
# {
#     "workouts": [
#         {
#             "date": "15/03/2024",
#             "time": "09:30:00",
#             "exercise": "Running",
#             "duration": "30",
#             "calories": "295"
#         }
#     ]
# }
```

### Writing to Google Sheets

Writing (POST) is where Sheety really shines:

```python
from datetime import datetime

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

# For each exercise from Nutritionix
for exercise in exercises:
    sheet_body = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),  # "running" → "Running"
            "duration": exercise["duration_min"],
            "calories": round(exercise["nf_calories"])
        }
    }
    
    response = requests.post(
        url=SHEETY_ENDPOINT,
        headers=sheety_headers,
        json=sheet_body
    )
    
    print(f"Added: {exercise['name']} - {exercise['duration_min']} min, {round(exercise['nf_calories'])} cal")
```

The key insight is the JSON structure: `{"workout": {...}}`. Sheety expects the sheet name as the outer key.

## Complete Data Pipeline

Here's how everything fits together:

```python
import requests
import os
from datetime import datetime

def main():
    # ============ STEP 1: Get user input ============
    exercise = input("Tell me what exercises you did: ")
    
    # ============ STEP 2: Process with Nutritionix ============
    nutritionix_headers = {
        "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
        "x-app-key": os.environ.get("NUTRITIONIX_API_KEY"),
    }
    
    exercise_params = {
        "query": exercise,
        "gender": "male",
        "weight_kg": 75.0,
        "height_cm": 175.0,
        "age": 30
    }
    
    response = requests.post(
        url="https://trackapi.nutritionix.com/v2/natural/exercise",
        headers=nutritionix_headers,
        json=exercise_params
    )
    
    exercises = response.json()["exercises"]
    
    # ============ STEP 3: Save to Google Sheets ============
    today = datetime.now()
    today_date = today.strftime("%d/%m/%Y")
    today_time = today.strftime("%H:%M:%S")
    
    sheety_headers = {
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}",
        "Content-Type": "application/json"
    }
    
    print("\nWorkout Summary:")
    print("-" * 40)
    
    for exercise in exercises:
        sheet_body = {
            "workout": {
                "date": today_date,
                "time": today_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": round(exercise["nf_calories"])
            }
        }
        
        response = requests.post(
            url=os.environ.get("SHEETY_ENDPOINT"),
            headers=sheety_headers,
            json=sheet_body
        )
        
        print(f"✓ {exercise['name'].title()}: {exercise['duration_min']} min, {round(exercise['nf_calories'])} cal")
    
    print("-" * 40)
    print("All workouts saved to Google Sheets!")

if __name__ == "__main__":
    main()
```

## Error Handling and Edge Cases

Several things can go wrong in this pipeline:

### 1. Nutritionix doesn't understand the input

If the user types something Nutritionix can't parse, the API returns an empty exercises list:

```python
response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=params)
exercises = response.json().get("exercises", [])

if not exercises:
    print("Couldn't understand that exercise. Try being more specific.")
    print("Example: 'I ran 3 miles' or '30 minutes of cycling'")
```

### 2. Sheety authentication fails

```python
try:
    response = requests.post(url=endpoint, headers=headers, json=body)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if response.status_code == 401:
        print("Authentication failed. Check your Sheety token.")
    elif response.status_code == 403:
        print("Permission denied. Check your sheet sharing settings.")
    else:
        print(f"Error: {e}")
```

### 3. Network issues

```python
try:
    response = requests.post(url, headers=headers, json=body, timeout=10)
except requests.exceptions.Timeout:
    print("Request timed out. Check your internet connection.")
except requests.exceptions.ConnectionError:
    print("Could not connect. Check your internet connection.")
```

## Practical Applications

This pattern—input → API processing → structured storage—appears everywhere:

**Health & Fitness:**
- Sleep tracking
- Food logging
- Weight tracking
- Mood journaling

**Productivity:**
- Time tracking
- Project logging
- Meeting notes

**Finance:**
- Expense tracking
- Receipt logging
- Budget updates

The beauty is that Google Sheets provides immediate visualization—you can create charts, add conditional formatting, and share with others without building a custom frontend.

## Environment Variables Setup

Before running, set these variables:

```bash
export NUTRITIONIX_APP_ID="your_app_id"
export NUTRITIONIX_API_KEY="your_api_key"
export SHEETY_ENDPOINT="https://api.sheety.co/yourusername/workouts"
export SHEETY_TOKEN="your_bearer_token"
```

Get your Nutritionix credentials from https://www.nutritionix.com/business/api

## Try It Yourself

```bash
python "main.py"
```

Type something like:
- "I ran 5 kilometers"
- "30 minutes of yoga and 20 pushups"
- "Swam for an hour"

Watch as each exercise is parsed, calories calculated, and rows added to your Google Sheet.

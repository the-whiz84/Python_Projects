# Day 38 - Natural Language Exercise Parsing and Sheets Logging

Day 38 is one of the first projects in the course that feels like a real personal automation tool. The user types a sentence such as “I ran 5 km and did 30 minutes of yoga,” and the script turns that into structured exercise records with durations and calorie estimates, then logs the result into Google Sheets. What makes the project interesting is not only the APIs involved. It is the fact that each stage transforms the data into a new shape that is better suited for the next stage.

This is a classic ETL-style workflow:

- extract the user’s description
- transform it into structured exercise records
- load those records into a storage system

## 1. Extracting Input in the Most Human-Friendly Form

The script begins with one freeform prompt:

```python
exercise = input("Tell me what exercises you did: ")
```

That is a big user-experience decision. The script is not asking for a rigid form with one field for exercise name, one field for minutes, and one field for calories. It is letting the user describe the workout naturally.

That means the program needs another system to do the hard work of interpretation. This is why Nutritionix is such a good fit for the project. It acts like the parsing layer between human language and structured exercise data.

## 2. Giving the Parsing API Enough Context to Be Useful

The Nutritionix request does more than pass the user’s sentence:

```python
exercise_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
```

These extra fields matter because calorie estimates are not universal. The API is being asked to interpret the exercise and personalize the output.

That is an important lesson in API usage: sometimes the raw user input is not enough. The quality of the response depends on how much context you provide.

Once the request is sent:

```python
workout_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=exercise_params)
workout_response.raise_for_status()
workout = workout_response.json()["exercises"]
```

the result is no longer freeform language. It is a list of normalized exercise entries the script can work with predictably.

## 3. Transforming the API Response into Sheet Rows

The next step is to reshape those exercise records into the payload expected by Sheety:

```python
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
```

This is the transform stage of the pipeline. The Nutritionix response contains more information than the sheet needs, and the keys do not match the sheet’s column structure directly. The code selects the right fields, renames them into the destination shape, and adds local timestamp data.

That local enrichment step is worth noticing:

- Nutritionix provides exercise interpretation
- your script provides the current date and time

The final row is a blend of external API output and local application context.

## 4. Loading the Result into Google Sheets Through Sheety

Once the payload is shaped correctly, the script posts it:

```python
sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheet_body)
print(sheety_response.text)
```

This completes the pipeline. The user’s sentence has now moved through three representations:

1. natural language text
2. parsed exercise records from Nutritionix
3. storage-ready workout rows for Google Sheets

This is why the project matters beyond the individual services. It teaches how multiple APIs can be chained together without becoming tangled, as long as each step has a clear input and output shape.

## 5. Why This Is a Strong Automation Pattern

The project has a reusable structure you will see again:

- collect input in a convenient human form
- delegate interpretation to a service designed for it
- normalize the result
- write it into a system that is easy to inspect later

Google Sheets works especially well here because it acts like a lightweight database while staying visible and editable to the user.

That visibility is useful in automation. A script is often easier to trust when its output lands in a format people can inspect without extra tooling.

## How to Run the Project

1. Open a terminal in this folder.
2. Set the required environment variables for Nutritionix and Sheety.
3. Run:

```bash
python main.py
```

4. Enter a sentence describing one or more exercises.
5. Confirm that the connected sheet receives a new row for each parsed exercise with the current date and time.

## Summary

Day 38 teaches more than “call two APIs.” It teaches a real ETL-style automation flow. The script takes human language, enriches it with body metrics, converts the API response into normalized workout rows, and writes those rows into a persistent store. The core lesson is how data changes shape across a pipeline and why each transformation step has a clear purpose.

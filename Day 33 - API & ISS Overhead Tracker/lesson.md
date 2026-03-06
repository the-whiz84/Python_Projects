# Day 33 - API Requests, JSON Parsing, and External Data Conditions

Day 33 introduces external APIs through a practical notification script. The program checks the ISS position from one API, checks sunrise and sunset data from another API, and sends an email only when both conditions are true. That combination is the important lesson: real automation often depends on joining multiple data sources before taking action.

## 1. Calling an API and Parsing JSON

The ISS position comes from the `open-notify` API:

```python
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

This is the core API workflow:

- send an HTTP request
- fail fast if the response is bad with `raise_for_status()`
- convert the JSON response into a Python dictionary
- extract the fields you actually need

That pattern repeats in almost every API-driven script later in the course.

## 2. Turning Raw Coordinates into a Useful Condition

The script does not need the exact ISS location for display. It needs a simple yes-or-no answer:

```python
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    return True
```

This is a good example of reducing raw data into a condition the rest of the program can use. The script defines “overhead” as being within a five-degree box around the user’s coordinates.

That is not astronomically precise, but it is good enough for a personal alert script. The lesson is that automation often depends on “good enough” rules that simplify the problem into something actionable.

## 3. Combining a Second API with Time-Based Logic

The night check uses a separate API:

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Bucharest",
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
```

Then the script extracts sunrise and sunset hours:

```python
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour
```

This is where the lesson becomes more realistic. One API gives location, another gives visibility context, and the program uses both to decide whether the user should be notified.

That is the bigger programming pattern of the day: gather separate facts, then combine them into one decision.

## 4. Polling on a Schedule and Taking Action

Once the conditions exist, the automation loop is simple:

```python
while True:
    time.sleep(60)
    if check_position() and is_night():
        send_email()
```

The script polls every minute and only sends the email if both helper functions return `True`.

This is a strong example of how small helper functions make automation easier to read. The loop itself does not need to know how the APIs work. It only needs boolean answers from each condition.

## How to Run the Project

1. Open a terminal in this folder.
2. Set the required environment variables:
   `MY_EMAIL`
   `MY_EMAIL_PASSWD`
3. Run:

```bash
python main.py
```

4. Confirm that the script checks once per minute and only sends the message when the ISS is near your configured coordinates and it is nighttime.

## Summary

Day 33 introduces API-based automation through a two-condition alert system. The script fetches JSON data from external services, turns raw coordinates and sunrise/sunset times into boolean checks, and only sends an email when both conditions are satisfied. The project is important because it shows how real scripts combine multiple external signals before acting.

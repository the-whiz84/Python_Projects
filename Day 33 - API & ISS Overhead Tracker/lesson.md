# Day 33 - API & ISS Overhead Tracker

Today we're building a program that tracks the International Space Station (ISS) and emails you when it passes over your location at night. This is our first day working with external APIs—services that other people run that we can call over the internet to get data.

The `requests` library makes HTTP calls easy, and we combine it with sunset/sunrise data to determine if it's dark enough to see the station.

## Calling an API

The open-notify API tells us the ISS's current position:

```python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

`response.json()` parses the JSON response into a Python dictionary. We extract the latitude and longitude from the nested structure.

## Checking if the ISS is overhead

We define a "overhead" zone as within 5 degrees of our position:

```python
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    return True
```

This is a simple bounding box check.

## Is it nighttime?

We need to know if it's dark outside—we can't see the ISS during the day. The sunrise-sunset API gives us that information:

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

if sunset <= time_now <= sunrise:
    return True
```

The API returns times in ISO format (`2024-01-15T07:30:00+00:00`). We split on `T` to get the time part, then split on `:` to get the hour.

## Running on a schedule

The script runs in an infinite loop, checking every 60 seconds:

```python
while True:
    time.sleep(60)
    if check_position() and is_night():
        send_email()
```

This is a simple approach for a personal notification script. For production, you'd use a proper scheduler or cron job.

## Try it yourself

```bash
python "main.py"
```

The script will check every minute and email you when the ISS is overhead and it's dark. Set your `MY_EMAIL` and `MY_EMAIL_PASSWD` environment variables first.

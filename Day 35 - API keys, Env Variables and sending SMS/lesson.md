# Day 35 - Environment Variables, API Keys, and SMS Alerts

Day 35 introduces a pattern that shows up constantly in real projects: use secret credentials from the environment, call an external service, and trigger a user-facing action when some condition is met. The specific tools here are Twilio for messaging and weather data for alerts, but the broader lesson is how external integrations are wired together safely.

## 1. Keeping Credentials Out of the Source Code

The Twilio setup in `main.py` reads secrets from environment variables:

```python
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
```

This is the habit to keep from the lesson. API keys and auth tokens should not live in the source file. They belong in the environment because they are configuration and secrets, not application logic.

That separation matters for both security and reuse. The same code can run in different environments with different credentials without being edited.

## 2. Treating Third-Party Services as Clients You Configure Once

Once the credentials are available, the project creates a Twilio client and uses it to send a message:

```python
message = client.messages.create(
    from_='whatsapp:+1234567890',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+1234567890'
)
```

The important design idea is that the client setup happens once, then the app uses that client for the actual action. This is the same pattern you will see later with database clients, API SDKs, and cloud service libraries.

The messaging example also makes the difference between configuration and runtime data clear:

- credentials identify your account
- message content and recipient are the current task

## 3. Turning External Data into a Notification Decision

The stronger project example is in `rain_alert.py`, where the script checks weather data first:

```python
weather_params = {
    "lat": YOUR_LATITUDE,
    "lon": YOUR_LONGITUDE,
    "appid": os.environ.get("OPENWEATHER_API_KEY"),
    "exclude": "current,minutely,daily"
}
```

Then it inspects the next few forecast hours:

```python
for hour_data in weather_data.get("hourly", [])[:12]:
    weather_id = hour_data.get("weather", [{}])[0].get("id", 0)
    if weather_id < 700:
        will_rain = True
        break
```

This is the bigger automation pattern of the day:

- fetch data from a service
- reduce that data to a yes-or-no decision
- notify the user if the condition is met

That pattern matters more than the specific weather codes. It is the basis for alerts, monitoring scripts, and event-driven automation.

## 4. Why Environment Variables Belong in the Workflow

This lesson is not only about hiding secrets from Git. Environment variables also make the scripts portable. The same program can run on your laptop, on another machine, or in a scheduled job as long as the required variables are present.

That is why the environment is such a common configuration layer for automation scripts. It lets code stay the same while runtime settings change.

## How to Run the Project

1. Open a terminal in this folder.
2. Set the required environment variables, for example:

```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_token_here"
export TWILIO_PHONE_NUMBER="+1234567890"
export MY_PHONE_NUMBER="+1987654321"
```

3. Run:

```bash
python main.py
```

4. If you want to explore the weather-based flow, review `rain_alert.py` and provide the matching API key and location settings before running that script.

## Summary

Day 35 introduces a core integration workflow for real applications. You load secrets from the environment, configure a third-party client, fetch external data when needed, and use that data to decide whether to send a notification. The tools are Twilio and weather APIs here, but the pattern applies far beyond this project.

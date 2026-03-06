# Day 35 - API Keys, Environment Variables, and Sending SMS

Today we're diving into the world of external APIs and securing our credentials. When you build real applications that talk to services like Twilio, Weather APIs, or any other third-party service, you need a way to authenticate yourself without hardcoding passwords into your source code.

This lesson covers three interconnected topics: what API keys are and why they matter, how to store secrets using environment variables, and how to send SMS or WhatsApp messages using Twilio.

## Why API Keys Matter

Every service that provides data or capabilities over the internet needs to know who is making requests. Without authentication, anyone could use a service without paying or respecting rate limits. API keys are the solution— they're unique identifiers that identify you as a user of the service.

When you sign up for a service like Twilio, OpenWeatherMap, or Alpha Vantage, you get an API key (or a pair of keys). These keys are strings of letters and numbers that look something like `SK1234567890ABCDEF`. You include this key in your requests, and the service knows exactly who you are.

Here's the critical rule: never put API keys in your source code that you plan to commit to GitHub. Thousands of developers have had their AWS accounts drained, their Twilio credits stolen, and their APIs abused because they accidentally committed keys to public repositories. The solution is environment variables.

## Understanding Environment Variables

Environment variables are key-value pairs that exist in your operating system's environment. Every process running on your computer has access to these variables. Python can read them through the `os` module.

Think of environment variables as a separate configuration layer that lives outside your code. Your code reads from this layer, but the actual values live somewhere else—usually in your terminal configuration or a `.env` file.

Here's how you read an environment variable in Python:

```python
import os

# This reads the value of MY_API_KEY from the system environment
api_key = os.environ.get("MY_API_KEY")

# If the variable doesn't exist, you get None by default
# You can provide a default value instead:
api_key = os.environ.get("MY_API_KEY", "fallback_default")
```

The difference between `os.environ["KEY"]` and `os.environ.get("KEY")` is important. Using square brackets (`[]`) will raise a KeyError if the variable doesn't exist. Using `.get()` returns None (or your default) if it's missing, which is usually safer for optional configuration.

### Setting Environment Variables

On macOS and Linux, you set environment variables in your terminal using the `export` command:

```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_auth_token_here"
export MY_API_KEY="secret_key_123"
```

These commands set the variables for your current terminal session. If you want them to persist across sessions, you add them to your shell configuration file (like `~/.bashrc` or `~/.zshrc`).

On Windows, you'd use the `set` command in Command Prompt:

```cmd
set TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Or in PowerShell:

```powershell
$env:TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

For development, many developers use a `.env` file combined with the `python-dotenv` library. You create a file called `.env` in your project root:

```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
MY_API_KEY=secret_key_123
```

Then in your Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # This reads the .env file and sets environment variables

api_key = os.environ.get("MY_API_KEY")
```

This approach is convenient because you can add `.env` to your `.gitignore` file, keeping your secrets out of version control while still having them available locally.

## Introducing Twilio

Twilio is a cloud communications platform that lets you send SMS messages, make phone calls, and send WhatsApp messages programmatically. They've made it incredibly simple to integrate communications into your applications.

To use Twilio, you need three things:

1. **Account SID** - A 34-character identifier for your Twilio account
2. **Auth Token** - A secret password for your account
3. **A Twilio phone number** - The number messages will be sent from

You get all of these when you sign up for a free Twilio account. The free account gives you some credit to experiment with.

## Sending SMS with Twilio

The Twilio Python library handles all the complexity of communicating with their API. Here's the basic pattern:

```python
from twilio.rest import Client
import os

# Get credentials from environment variables
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS message
message = client.messages.create(
    body="Hello from Python! This is an SMS message.",
    from_="+1234567890",  # Your Twilio phone number
    to="+1987654321"       # The recipient's phone number
)

# The message object contains the SID, status, and other details
print(f"Message sent with SID: {message.sid}")
print(f"Message status: {message.status}")
```

The `from_` parameter requires a phone number you've purchased through Twilio. The `to` parameter is any valid phone number. Both must be in E.164 format, which means they include the country code: `+1` for US numbers, `+44` for UK numbers, and so on.

## Sending WhatsApp Messages

Twilio also supports WhatsApp messaging. The API is almost identical to SMS, but you use WhatsApp-specific prefixes:

```python
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello via WhatsApp!",
    from_="whatsapp:+1234567890",    # Twilio's WhatsApp sandbox number
    to="whatsapp:+1987654321"         # Recipient's WhatsApp number
)

print(f"WhatsApp message sent: {message.sid}")
```

For WhatsApp, you start with Twilio's sandbox number. Once you've tested and ready to go live, you can connect your own business WhatsApp number.

## Error Handling with Twilio

When working with external APIs, things can go wrong. The network might be down, the recipient's number might be invalid, or you might have exceeded your account balance. Here's how to handle these gracefully:

```python
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Test message",
        from_="+1234567890",
        to="+1987654321"
    )
    print(f"Success! Message SID: {message.sid}")
    
except TwilioRestException as e:
    print(f"Twilio error: {e.code} - {e.msg}")
    # Handle specific error codes
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

Common Twilio error codes include:
- 20003: Authentication failed (check your credentials)
- 21211: Invalid phone number
- 21601: Phone number is not SMS-capable
- 29999: Generic programming error (check your request format)

## Practical Application: Rain Alert

Let's put this together into a practical example. In the project's `rain_alert.py`, you'll see a function that checks the weather and sends an SMS if rain is expected:

```python
import requests
from twilio.rest import Client
import os

def check_weather_and_alert():
    # 1. Check weather using OpenWeatherMap API
    weather_params = {
        "lat": YOUR_LATITUDE,
        "lon": YOUR_LONGITUDE,
        "appid": os.environ.get("OPENWEATHER_API_KEY"),
        "exclude": "current,minutely,daily"
    }
    
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall",
        params=weather_params
    )
    
    # Parse the response to check for rain in the next few hours
    weather_data = response.json()
    will_rain = False
    
    for hour_data in weather_data.get("hourly", [])[:12]:
        weather_id = hour_data.get("weather", [{}])[0].get("id", 0)
        if weather_id < 700:  # Weather codes below 700 indicate rain/snow
            will_rain = True
            break
    
    # 2. Send SMS if rain is expected
    if will_rain:
        client = Client(
            os.environ.get("TWILIO_ACCOUNT_SID"),
            os.environ.get("TWILIO_AUTH_TOKEN")
        )
        
        client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella! ☔",
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            to=os.environ.get("MY_PHONE_NUMBER")
        )
```

This is a complete automation pipeline: fetch data from an external API, make a decision based on that data, and take action (send a notification) based on the result.

## Why This Matters

The combination of API keys, environment variables, and third-party service integration is the foundation of modern application development. Almost every real application you build will need to:

1. Authenticate with external services (API keys)
2. Keep those credentials secure (environment variables)
3. Communicate with users through multiple channels (SMS, email, push notifications)

These patterns appear everywhere, from the simplest scripts to enterprise-scale systems. Master them now, and you'll be able to build sophisticated applications that interact with the world beyond your own servers.

## Try It Yourself

```bash
python "main.py"
```

Before running, make sure you've set the required environment variables:

```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_token_here"
export TWILIO_PHONE_NUMBER="+1234567890"
export MY_PHONE_NUMBER="+1987654321"
```

The script will attempt to send an SMS or WhatsApp message using your Twilio credentials.

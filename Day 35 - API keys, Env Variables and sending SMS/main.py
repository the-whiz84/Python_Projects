# 1. API Authentication

# Many services require an account or to pay for use of API data. Open Weather has a free service with a monthly limit for API calls.
# We need to generate an API key to authenticate in the API request and get the response.


# 2. Sending an SMS via the Twillio App

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#     from_="+15017122661",
#     to="+15558675310",
# )
#
# print(message.body)

# We can also use Whatsapp instead
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+1234567890',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+1234567890'
)

print(message.sid)

# 3. Environment Variables and hiding API keys

# Environment variables are used for :
# - Convenience: storing settings, customization or variables for your code base
# - Security: you can store secrets, passwords or API keys

# We set Environment Variables using the export command in the terminal
# export TWILIO_ACCOUNT_SID=

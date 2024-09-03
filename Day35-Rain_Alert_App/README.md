
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              *
*    Author: Radu Chiriac                                  *
*    Day: 35 - Rain Alert SMS/Whatsapp                     *
*    Subject: API security, Environment Variables, SMS     *
*    Date: 2024-09-03                                      *
************************************************************


# Description
This is an application that uses the APIs from Open Weather Map (https://openweathermap.org/forecast5) and Twilio (https://www.twilio.com)
to check the weather forecast for the next 12 hours and send you a SMS or WhatsApp message to alert you to bring an umbrella with you.

# How to use
- create free accounts on OWM and Twilio
- get your API keys and Twilio telephone number
- for US/Canada, you cannot send SMS from Toll Free Numbers so you need to use the Whatsapp method (https://www.twilio.com/docs/whatsapp/quickstart/python)
- set up the secret keys, telephone numbers etc in your environment (https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html)
- replace the Longitude and Latitude coordinates with your own location
- you can also set the units parameter to "imperial" if you prefer to modify the code and get the temperature
- run the code and receive message if the forecast for the day shows rain
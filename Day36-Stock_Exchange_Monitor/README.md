
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              
*    Author: Radu Chiriac                                  
*    Day: 36 - Stock Exchange Alerts                       
*    Subject: API, Env Variables, Whatsapp alerts          
*    Date: 2024-09-04                                      
************************************************************


# Description
This is an application that uses the APIs from Alpha Vantage (https://www.alphavantage.co) to get given stock name difference for the past 2 days.
If the difference is more than 5%, it fetches the news related to the company name from News API (https://newsapi.org/v2/everything).
It then sends a Whatsapp message from Twilio (https://www.twilio.com) to your number with the top 3 news article headlines, summary and links.


# How to use
- create free accounts on Alpha Vantage, News API and Twilio
- get your API keys and Twilio Whatsapp number
- set up the secret keys, telephone numbers etc in your environment (https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html)
- modify the STOCK and COMPANY_NAME variables with your desired ones
- run it and get notified of changes greater than 5% (you can test it my modifying the if statement to >=1 or lower)

# Disclaimer
The AV free tier only allows 25 API calls per day.
Twilio gives you $25 credit when you sign up and might use small amounts for each Whatsapp message
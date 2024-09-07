
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              *
*    Author: Radu Chiriac                                  *
*    Day: 39/40 - Flight Deal Finder                       *
*    Subject: API, HTTP GET and POST, SMTP, SMS, Email     *
*    Date: 2024-09-07                                      *
************************************************************


# Description
This is an application that uses the APIs from Amadeus (https://developers.amadeus.com) to find the cheapest flights for a given departure and return period. Then you receive a SMS/Whatsapp alert and you send notification emails to a list of people with the deal.
The desired destinations are put in a Google Sheet, like we did in Day 38. Using a Google Form that we attach it as another sheet in the Excel form, we capture first name, last name and email address to be notified. 
It also uses Sheety (https://sheety.co) as an interface to manage Google Sheets.

# How to use
- copy the example sheet from the instructor to your own Google Sheets account (https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?gid=0#gid=0)
- login to Sheety with the same Google account and allow it to view and edit files
- using Sheety documentation, enable Bearer Authentication and create your token.
- save your Sheety endpoint, Token and other API Keys as environment variable for security (see previous days for instructions)
- create a Google Form with 3 questions asking for first name, last name and email address then add it to your Google Sheet as a tab names 'users'
- In the 'prices' tab, update the desired cities you want to visit and the price alert you want to be notified about
- fill in the Google form with some testing data or share it with your friends or family
- modify the variable ORIGIN_CITY_IATA with the IATA code of the departure city (https://www.iata.org/en/publications/directories/code-search/)
- modify the variable STAY_DURATION with the desired return period. It can be a number or a range separated by a comma (for eg, you want return flights between 5 and 10 days later you put ("5,10"))
- run the program and be notified
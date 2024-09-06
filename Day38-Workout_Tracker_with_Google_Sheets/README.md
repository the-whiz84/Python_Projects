
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              *
*    Author: Radu Chiriac                                  *
*    Day: 38 - Workout Tracker using Google Sheets         *
*    Subject: API, HTTP Post, Authorization Headers        *
*    Date: 2024-09-06                                      *
************************************************************


# Description
This is an application for Workout Tracking using Google Sheets. It uses the APIs from from Nutritionix (https://www.nutritionix.com/business/api) that converts natural language input into a dictionary with workout name, duration and calories burned. It also uses Sheety (https://sheety.co) as an interface between Google Sheets and Nutritionix.

# How to use
- copy the example sheet from the instructor to your own Google Sheets account (https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?gid=0#gid=0)
- login to Sheety with the same Google account and allow it to view and edit files
- using Sheety documentation, enable Bearer Authentication and create your token.
- save your Sheety endpoint, Token and other API Keys as environment variable for security (see previous days for instructions)
- update the variables with your own physical parameters
- run the program and update your Google Sheet using natural language
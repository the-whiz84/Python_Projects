
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              *
*    Author: Radu Chiriac                                  *
*    Day: 47 - Amazon Price Tracker                        *
*    Subject: BeautifulSoup, Web Scrapping, smtplib        *
*    Date: 2024-09-12                                      *
************************************************************


# Description
This is a project that scrapes the data from an Amazon page using BeautifulSoup. For the product you are interested in, it checks the price and sends an email alert when that price is lower than the desired amount.

# How to use
- get the URL for an Amazon produce you are interested in
- set up the headers dictionary for your own OS and browser using https://myhttpheader.com
- set up your email address and app password and store them as environment variables (https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html)
- run the program and test it using a lower value than the actual price
- automate the script using cron in Linux/Mac or Task Scheduler in Windows to run daily

# Disclaimer
Amazon website varies by region quite a lot and your product name or prices will be in different currencies or language
You will need to inspect the title and price of the product and replace the variables "price_data" and "product_name_data" with the correct search values
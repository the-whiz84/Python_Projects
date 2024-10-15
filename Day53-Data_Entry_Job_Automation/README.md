
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              
*    Author: Radu Chiriac                                  
*    Day: 53 - Data Entry Job Automation with Google Form  
*    Subject: BeautifulSoup, Selenium, browser automation  
*    Date: 2024-09-14                                      
************************************************************


# Description
This is a project that uses everything we learned about Web Scrapping to automate filling a Google Form with data from a source website using BeautifulSoup and Selenium.

# How to use
- install BeautifulSoup module using 'pip install bs4'
- install Selenium module using 'pip install Selenium'
- if you use other browser than Chrome then replace any reference to it with the one you use (Safari, Firefox etc) 
- check this link for the supported browsers (https://www.selenium.dev/documentation/webdriver/browsers/)
- create a Google Form like we did in Day 40 with 3 questions asking for the listing address, price and url
- attach the Answers to a new Google Sheet 
- update the variables in google_form.py with your own


# Limitations
This project was done on a clone of the live Zillow website. It could be adapted to other rental offers websites by modifying the necessary elements used for web scrapping.
It's very hard to use the Zillow live website due to its bot protection.

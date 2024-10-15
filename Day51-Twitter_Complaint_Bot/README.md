
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              
*    Author: Radu Chiriac                                  
*    Day: 51 - Twitter/X Complaint Bot                     
*    Subject: Web Scrapping, Selenium, browser automation  
*    Date: 2024-09-14                                      
************************************************************


# Description
This is a project that uses Selenium to automate the process of getting your current internet speed from https://speedtest.net and then sending a complaint tweet to your ISP comparing it to your promised speeds. 

# How to use
- install Selenium module using 'pip install Selenium'
- if you use other browser than Chrome then replace any reference to it with the one you use (Safari, Firefox etc) 
- check this link for the supported browsers (https://www.selenium.dev/documentation/webdriver/browsers/)
- modify the variables with your ISP Twitter handle and promised Up/Down speeds in your contract
- run the program and complain on Twitter (x -- whatever)

# Limitations
You have to manually input your MFA code during X login due to bot protection.
Also, do not run the program too many times at once as you will not be able to login to X for a while.

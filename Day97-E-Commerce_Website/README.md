
******************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu
*    Author: Radu Chiriac
*    Day: 97 - Portfolio Projects - eCommerce Website with Payment Integration
*    Subject: Flask, Bootstrap 5, Stripe
*    Date: 2024-10-18
******************************************************************************


# Description

This is the thirteenth project without any guidance from the last Chapter of the Course: Porfolio Projects.


## Prerequisites
- install required packages with `pip install -r requirements.txt`

## How to use
- run main.py in your IDE or in a terminal type `python3 main.py`
- press `Buy` on the featured product in the shop and the Stripe payment process will take over
- enter a dummy card number like `4242 4242 4242 4242` with a valid expiration date and a dummy cvv
- you can find a list of test methods on <a href='https://docs.stripe.com/testing#international-cards'>Stripe's website</a>
## Warning
- other payment options will appear depending on your location, they will actually work, so DO NOT USE them
- even if this is a Test API, I don't want to be responsible if actual money are taken by Stripe
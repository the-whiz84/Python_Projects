
****************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu
*    Author: Radu Chiriac
*    Day: 91 - Portfolio Projects - PDF text to audio file with Amazon Polly
*    Subject: Function, PyPDF2, boto3
*    Date: 2024-10-15
****************************************************************************


# Description

This is the eight project without any guidance from the last Chapter of the Course: Porfolio Projects.


## Prerequisites
- install required packages with `pip install -r requirements.txt`
- you need an AWS free account (first 12 months include 1 million words / month conversion in Amazon Polly)
- create an S3 bucket (5 GB are free) and add it's name to the environment variables
- create AWS API keys and add them to environment variables
- provide the path to a PDF document

## How to use
- run main.py in your IDE or in a terminal type `python3 main.py`
- the mp3 audio file will be saved in your S3 bucket from where you can download it.
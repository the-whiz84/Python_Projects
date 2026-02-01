# 1. SMTP - Simple Mail Transfer Protocol

import smtplib

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
# 	connection.starttls()
# 	connection.login(user=my_email, password=password)
# 	connection.sendmail(
# 		from_addr=my_email,
# 		to_addrs=recipient_email,
# 		msg="Subject: Testing from Birthday Wisher app in Python\n\n Hello,\n This is the content of the email."
# 	)

# connection.close()
# We can instead use the same formatting as with open files


# 2. Datetime Module

# import datetime as dt

# Current date and time
# now = dt.datetime.now()
# print(now)
# 2024-09-01 12:38:59.886372
# year = now.year
# print(year)
# 2024
# if year == 2024:
# 	print("The pandemic is over!")

# This datetime class has many attributes that can be retrieved
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1984, month=10, day=12)
# print(date_of_birth)
# 1984-10-12 00:00:00


# 3. Challenge - Send Motivational quotes on Mondays

import os
import smtplib, random
import datetime as dt

quote_list = []
with open("quotes.txt", "r") as file:
	data = file.readlines()

	for line in data:
		new_line = line.strip()
		quote_list.append(new_line)

quote_of_the_day = random.choice(quote_list)

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_EMAIL_PASSWD")
recipient_email = os.environ.get("MY_EMAIL") # Using self as recipient as example

now = dt.datetime.now()
if now.weekday() == 0:
	with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs=recipient_email,
			msg=f"Subject: Quote of the Day\n\n Hello,\nHere is your quote of the day:\n{quote_of_the_day}"
		)
# Email received
# Hello,
# Here is your quote of the day:
# "You don't have to be great to start, but you have to start to be great." - Zig Ziglar
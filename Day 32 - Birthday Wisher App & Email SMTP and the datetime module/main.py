##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
import datetime as dt
import random, pandas, smtplib
import os

my_email = os.environ.get("MY_EMAIL")
email_password = os.environ.get("MY_EMAIL_PASSWD")
email_server = "smtp.gmail.com"


def send_email(birthday_email, birthday_letter):
	with smtplib.SMTP(host=email_server, port=587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=email_password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs=birthday_email,
			msg=f"Subject: HAPPY BIRTHDAY!!\n\n{birthday_letter}"
		)


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
today = dt.datetime.now()
today_month = today.month
today_day = today.day

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if (today_month, today_day) in birthdays_dict:
	recipient_name = birthdays_dict[today_month, today_day]["name"]
	recipient_email = birthdays_dict[today_month, today_day]["email"]
	# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
	# HINT: https://www.w3schools.com/python/ref_string_replace.asp
	random_choice = random.randint(1, 3)
	with open(f"letter_templates/letter_{random_choice}.txt") as file:
		file_data = file.read()
		new_text = file_data.replace("[NAME]", recipient_name)
		# 4. Send the letter generated in step 3 to that person's email address.
		# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
		send_email(recipient_email, new_text)

# Email received
HAPPY BIRTHDAY
Hey Radu,

Happy birthday! Have a wonderful time today and eat lots of cake!

Lots of love,

Angela
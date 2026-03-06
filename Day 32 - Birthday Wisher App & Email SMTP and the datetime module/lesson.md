# Day 32 - Birthday Wisher App, Email SMTP, and Datetime

Today we're building an automated birthday wisher. The program checks if anyone in your birthday list has a birthday today, picks a random congratulatory letter, personalizes it with their name, and emails it to them.

This introduces three new concepts: the datetime module for working with dates, SMTP for sending emails, and combining file I/O with external APIs.

## Getting today's date

The datetime module gives us access to the current date and time:

```python
import datetime as dt

today = dt.datetime.now()
today_month = today.month
today_day = today.day
```

Now we have the current month and day as integers.

## Matching birthdays

We load the birthdays CSV and turn it into a dictionary where the key is the month-day tuple:

```python
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    recipient_name = birthdays_dict[today_month, today_day]["name"]
    recipient_email = birthdays_dict[today_month, today_day]["email"]
```

This makes lookup O(1) instead of scanning through the whole file each time the script runs.

## Sending emails with SMTP

SMTP (Simple Mail Transfer Protocol) is the standard way to send emails. Python's `smtplib` handles the connection:

```python
def send_email(birthday_email, birthday_letter):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject: HAPPY BIRTHDAY!!\n\n{birthday_letter}"
        )
```

`starttls()` upgrades the connection to encrypted mode. The email credentials come from environment variables—never hardcode passwords in your code.

## Personalizing the letter

We pick a random letter template and replace `[NAME]` with the actual recipient's name:

```python
random_choice = random.randint(1, 3)
with open(f"letter_templates/letter_{random_choice}.txt") as file:
    file_data = file.read()
    new_text = file_data.replace("[NAME]", recipient_name)
    send_email(recipient_email, new_text)
```

## Try it yourself

```bash
python "main.py"
```

Make sure to set `MY_EMAIL` and `MY_EMAIL_PASSWD` environment variables first. For testing, add a birthday entry matching today's date in `birthdays.csv`.

# Day 32 - Email Automation with SMTP and Datetime Scheduling

Day 32 connects local data, calendar logic, and email delivery into one automation workflow. The birthday wisher checks the current date, looks for a matching record in a CSV file, chooses a template, personalizes it, and sends an email. The project is useful because it shows how several simple pieces become an actual automation once they are chained together in the right order.

## 1. Turning the Current Date into a Lookup Key

The script begins by reading the current date:

```python
import datetime as dt

today = dt.datetime.now()
today_month = today.month
today_day = today.day
```

This is a good example of extracting only the values the program actually needs. The automation does not care about the full timestamp. It only cares about month and day.

That keeps the matching logic simple and focused on the birthday use case.

## 2. Converting the Birthday Table into a Searchable Structure

The CSV data is turned into a dictionary keyed by `(month, day)`:

```python
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
```

This is a strong design choice because it converts the birthday table into a lookup structure. Once that dictionary exists, checking whether today matches someone’s birthday is immediate:

```python
if (today_month, today_day) in birthdays_dict:
```

The lesson here is similar to Day 26: load structured data, then reshape it into the Python data structure that best supports the task you want to perform.

## 3. Separating Template Creation from Email Delivery

After a birthday match is found, the script picks a random template and customizes it:

```python
random_choice = random.randint(1, 3)
with open(f"letter_templates/letter_{random_choice}.txt") as file:
    file_data = file.read()
    new_text = file_data.replace("[NAME]", recipient_name)
```

Then the email gets sent through a helper function:

```python
def send_email(birthday_email, birthday_letter):
    with smtplib.SMTP(host=email_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject: HAPPY BIRTHDAY!!\n\n{birthday_letter}"
        )
```

This separation matters. One part of the code prepares the personalized content. Another part handles the transport. That keeps the automation easier to reason about and easier to extend later.

## 4. Why This Counts as a Real Automation

The full workflow is:

- get today’s date
- check the birthday dataset
- generate a personalized message
- send the message through SMTP

That is the real lesson of the day. Automation is rarely one clever line. It is usually a sequence of smaller steps where each step prepares the next one.

The script also introduces a basic operational habit: keep credentials in environment variables instead of hardcoding them into the source.

## How to Run the Project

1. Open a terminal in this folder.
2. Set the required environment variables:
   `MY_EMAIL`
   `MY_EMAIL_PASSWD`
3. Run:

```bash
python main.py
```

4. For testing, make sure `birthdays.csv` contains an entry matching today’s month and day, then confirm that the script selects a template and sends the email.

## Summary

Day 32 shows how local data, date logic, templates, and SMTP fit together in one automation. The script turns the current month and day into a lookup key, finds the right record from a CSV file, personalizes a message, and delivers it through email. It is one of the first lessons that feels like a real scheduled utility rather than a demo.

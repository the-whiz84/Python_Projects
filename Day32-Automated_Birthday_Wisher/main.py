import datetime as dt
import random, pandas, smtplib

my_email = "******"
email_password = "******"
email_server = "******"  # Example for Gmail: "smtp.gmail.com"


def send_email(birthday_email, birthday_letter):
    """Send email to the birthday_email with the body of birthday_letter

    Args:
        birthday_email (_type_): email of the receiver
        birthday_letter (_type_): Text in the body of the email
    """
    with smtplib.SMTP(host=email_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject: HAPPY BIRTHDAY!!\n\n{birthday_letter}"
        )


today = dt.datetime.now()
today_month = today.month
today_day = today.day

birthdays_dict = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for person in birthdays_dict:
    if person['month'] == today_month and person['day'] == today_day:
        recipient_name = person["name"]
        recipient_email = person["email"]
        random_choice = random.randint(1, 3)

        with open(f"letter_templates/letter_{random_choice}.txt") as file:
            file_data = file.read()
            new_text = file_data.replace("[NAME]", recipient_name)

            send_email(recipient_email, new_text)

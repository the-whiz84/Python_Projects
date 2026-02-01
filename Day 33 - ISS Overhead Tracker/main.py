import requests, smtplib, time, os
from datetime import datetime

MY_LAT = 45.649490
MY_LONG = 25.606550



def check_position():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])
	if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
		return True


def is_night():
	parameters = {
		"lat": MY_LAT,
		"lng": MY_LONG,
		"formatted": 0,
		"tzid": "Europe/Bucharest",
	}
	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
	time_now = datetime.now().hour
	if sunset <= time_now <= sunrise:
		return True


def send_email():
	email_server = "smtp.gmail.com"
	my_email = os.environ.get("MY_EMAIL")
	email_password = os.environ.get("MY_EMAIL_PASSWD")
	
	with smtplib.SMTP(host=email_server, port=587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=email_password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs=my_email,
			msg=f"Subject: ISS Tracker\n\nLook Up! ISS is over your area."
		)

while True:
    time.sleep(60)
    if check_position() and is_night():
        send_email()

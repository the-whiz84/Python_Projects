import os, smtplib
from twilio.rest import Client


class NotificationManager:
	#This class is responsible for sending notifications with the deal flight details.
	def __init__(self):
		self.sid = os.environ.get("TWILIO_SID")
		self.token = os.environ.get("TWILIO_TOKEN")
		self.twilio_number = os.environ.get("TWILIO_TEL_NO")
		self.whatsapp_number = os.environ.get("TWILIO_WHATSAPP_NO")
		self.verified_number = os.environ.get("MY_TEL_NO")
		self.email = os.environ.get("MY_EMAIL")
		self.email_password = os.environ.get("MY_EMAIL_PASSWD")

		self.client = Client(self.sid, self.token)
		self.connection = smtplib.SMTP(host="smtp.gmail.com", port=587)

	def send_sms(self, message_body):
		"""
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_TEL_NO` and `MY_TEL_NO` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
		message = self.client.messages.create(
			from_=self.twilio_number,
			body=message_body,
			to=self.verified_number
		)
		# Prints if successfully sent.
		print(message.sid)

	# Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
	# https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

	def send_whatsapp(self, message_body):
		"""
        Sends a Whatsapp message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send a Whatsapp message from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the Whatsapp message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_WHATSAPP_NO` and`MY_TEL_NO` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
		message = self.client.messages.create(
			from_=f"whatsapp:{self.whatsapp_number}",
			body=message_body,
			to=f"whatsapp:{self.verified_number}"
		)
		print(message.sid)

	def send_emails(self, email_list, email_body):
		with self.connection:
			self.connection.starttls()
			self.connection.login(user=self.email, password=self.email_password)
			for email in email_list:
				self.connection.sendmail(
					from_addr=self.email,
					to_addrs=email,
					msg=f'Subject:Flight Club Alert - New Low Price Flight!\n\n{email_body}'.encode('utf-8')
				)

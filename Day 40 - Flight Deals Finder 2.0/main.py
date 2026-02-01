#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_best_price
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"
STAY_DURATION = "3,20"

data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# sheet_data = data_manager.get_destination_data()
sheet_data = [{
    "city": "Paris",
    "iataCode": "PAR",
    "lowestPrice": 500,
    },
    {
        "city": "Frankfurt",
        "iataCode": "FRA",
        "lowestPrice": 250,
    },
    {
        "city": "Tokyo",
        "iataCode": "TYO",
        "lowestPrice": 700,
    },
    {
        "city": "Dublin",
        "iataCode": "DBN",
        "lowestPrice": 300,
    },
    {
        "city": "Vienna",
        "iataCode": "VIE",
        "lowestPrice": 100,
    },
    {
        "city": "Dubai",
        "iataCode": "DXB",
        "lowestPrice": 300,
    }
]

# ==================== Update the Airport Codes in Google Sheet ====================
## Only run first time or when new cities were added to the Google Sheet.

# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#         # slowing down requests to avoid rate limit
#         time.sleep(2)
#
# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()


# ==================== Retrieve your customer emails ====================

# customer_data = data_manager.get_customer_emails()
# # Verify the name of your email column in your sheet. Yours may be different from mine
# customer_email_list = [row["whatIsYourEmailAddress?"] for row in customer_data]
# print(f"Your email list includes {customer_email_list}")
customer_email_list = ["[EMAIL_ADDRESS]", "[EMAIL_ADDRESS]", "[EMAIL_ADDRESS]"]

# ==================== Search for Flights ====================

current_date = dt.date.today()
departure_time_delta = 3
departure_date = (current_date + dt.timedelta(departure_time_delta)).strftime('%Y-%m-%d')


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_date=departure_date,
        duration=STAY_DURATION
    )
    cheapest_flight = find_best_price(flights)
    #Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        message_body = (f"Low price alert! Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to "
                        f"{cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")

        print(f"Check your email. Lower price flight found to {destination['city']}!")
        notification_manager.send_whatsapp(message_body)
        notification_manager.send_emails(email_list=customer_email_list, email_body=message_body)

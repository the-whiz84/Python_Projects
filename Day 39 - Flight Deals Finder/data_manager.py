import requests, os

PRICES_ENDPOINT = os.environ.get("PRICES_ENDPOINT")

class DataManager:
    # This class is responsible for talking to the Sheety API.
    def __init__(self):
        self.token = os.environ.get("SHEETY_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)

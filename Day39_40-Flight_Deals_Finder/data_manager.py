import requests, os


class DataManager:
    # This class is responsible for talking to the Sheety API.
    def __init__(self):
        self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
        self.token = os.environ.get("SHEETY_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        self.destination_data = {}
        self.customer_data = {}


    def get_destination_data(self):
        response = requests.get(url= self.prices_endpoint, headers=self.headers)
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
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)


    def get_customer_emails(self):
        response = requests.get(url= self.users_endpoint, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

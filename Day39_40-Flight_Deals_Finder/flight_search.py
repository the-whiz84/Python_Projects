import requests, os

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v1/shopping/flight-dates"
CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API
    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self.token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        """
		Retrieves the IATA code for a specified city using the Amadeus Location API.
		Parameters:
		city_name (str): The name of the city for which to find the IATA code.
		Returns:
		str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
		or "Not Found" if no match is found due to a KeyError.

		The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
		name and other parameters to refine the search. It then attempts to extract the IATA code
		from the JSON response.
		- If the city is not found in the response data (i.e., the data array is empty, leading to
		an IndexError), it logs a message indicating that no airport code was found for the city and
		returns "N/A".
		- If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading
		to a KeyError), it logs a message indicating that no airport code was found for the city
		and returns "Not Found".
		"""
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=CITIES_ENDPOINT,
            headers=headers,
            params=query
        )

        try:
            iata_code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_date, duration):
        """
        Searches for flight options between two cities on specified range of departure and return dates
        using the Amadeus API.
        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_date (string): The departure date.
            duration (str): The duration of stay. Can be provided as a range of different days separated by a comma
        Returns:
            dict or None: A dictionary containing flight offer data if the query is successful; None
            if there is an error.
        The function constructs a query with the flight search parameters and sends a GET request to
        the API. It handles the response, checking the status code and parsing the JSON data if the
        request is successful. If the response status code is not 200, it logs an error message and
        provides a link to the API documentation for status code details.
        """

        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "origin": origin_city_code,
            "destination": destination_city_code,
            "departureDate": from_date,
            "duration": duration,
            "nonStop": False,
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search/api-reference")
            print("Response body:", response.text)
            return None

        return response.json()
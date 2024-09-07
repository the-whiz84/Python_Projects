
class FlightData:

    def __init__(self, price=None, origin_airport=None, destination_airport=None, departure_date=None, return_date=None):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
         - price: The cost of the flight.
         - origin_airport: The IATA code for the flight's origin airport.
         - destination_airport: The IATA code for the flight's destination airport.
         - out_date: The departure date for the flight.
         - return_date: The return date for the flight.
         """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = departure_date
        self.return_date = return_date


def find_best_price(data):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.
    Args:
        data (dict): The JSON data containing flight information returned by the API.
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.
    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
     FlightData object with the details of the most affordable flight.
    """

    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Data from the first flight in the json
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["total"])
    origin = first_flight["origin"]
    destination = first_flight["destination"]
    departure_date = first_flight["departureDate"]
    return_date = first_flight["returnDate"]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date)

    for flight in data["data"]:
        price = float(flight["price"]["total"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["origin"]
            destination = flight["destination"]
            departure_date = flight["departureDate"]
            return_date = flight["returnDate"]
            cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
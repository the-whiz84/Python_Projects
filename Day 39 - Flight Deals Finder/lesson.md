# Day 39 - Flight Deals Finder: Multi-Service Architecture

Today we're building a sophisticated flight deal detection system. This project represents a significant leap in complexity—we're coordinating multiple external services, implementing intelligent pricing logic, and building a system that runs autonomously to find deals.

This lesson explores the architecture of multi-service applications, data layer design, and building production-quality automation.

## The Problem We're Solving

Finding cheap flights is time-consuming. You have to:
1. Know which airports to search from
2. Search multiple destinations
3. Check prices across date ranges
4. Repeat regularly to catch sales

Our solution: a system that checks flight prices automatically, compares them to target prices, and alerts you when deals are found.

## System Architecture

The application is divided into four distinct services, each with a single responsibility:

```
┌─────────────────────────────────────────────────────────────┐
│                        main.py                                │
│                    (Orchestrator)                            │
└─────────────────┬───────────────────────────────────────────┘
                  │
      ┌───────────┼───────────┬───────────────┐
      ▼           ▼           ▼               ▼
┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐
│DataMgr │ │FlightSrch│ │FlightData│ │NotificationMgr │
│(Sheets)│ │(Amadeus)│ │(Parser)  │ │(Twilio/Email)  │
└─────────┘ └──────────┘ └──────────┘ └──────────────────┘
```

This is the **Service-Oriented Architecture (SOA)** pattern—each component is independent, testable, and replaceable.

## Service 1: DataManager - Google Sheets Integration

The DataManager handles all communication with Google Sheets. It manages:
- Reading destination cities and their IATA codes
- Reading target price thresholds
- Writing updated IATA codes when we discover them

```python
class DataManager:
    def __init__(self):
        self.endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.token = os.environ.get("SHEETY_TOKEN")
        self.destination_data = []
    
    def get_destination_data(self):
        """Fetch all destinations from Google Sheets"""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(self.endpoint, headers=headers)
        
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        """Update IATA codes that were previously empty"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        for city in self.destination_data:
            # Sheety uses row-based endpoints: /prices/2
            row_endpoint = f"{self.endpoint}/{city['id']}"
            
            data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            
            response = requests.put(row_endpoint, json=data, headers=headers)
```

The key insight: Google Sheets becomes our "database" for configuration. Users can add destinations, change target prices, and enable/disable cities without touching code.

## Service 2: FlightSearch - Flight API Integration

The FlightSearch service wraps the Amadeus API (or similar flight search API) to query real-time flight prices:

```python
class FlightSearch:
    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        self.base_url = "https://api.amadeus.com"
    
    def get_access_token(self):
        """Authenticate with Amadeus and get a bearer token"""
        response = requests.post(
            f"{self.base_url}/v1/security/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            }
        )
        return response.json()["access_token"]
    
    def check_flights(self, origin_city_code, destination_city_code, from_date, duration):
        """Search for flights between two cities"""
        token = self.get_access_token()
        
        headers = {"Authorization": f"Bearer {token}"}
        
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_date,
            "adults": 1,
            "max": 10,  # Return up to 10 flight options
        }
        
        response = requests.get(
            f"{self.base_url}/v2/shopping/flight-offers",
            headers=headers,
            params=params
        )
        
        return response.json()
```

Amadeus is a major Global Distribution System (GDS) used by airlines and travel agencies. Their API provides real pricing data, not estimates.

## Service 3: FlightData - Data Processing

Raw flight API responses are complex. FlightData parses them into simple objects:

```python
class FlightData:
    def __init__(self, data):
        self.data = data
    
    @property
    def price(self):
        """Get the price in dollars"""
        try:
            return int(self.data["offerItems"][0]["price"]["total"])
        except (KeyError, IndexError, ValueError):
            return "N/A"
    
    @property
    def origin_airport(self):
        try:
            return self.data["offerItems"][0]["segments"][0]["departure"]["iataCode"]
        except (KeyError, IndexError):
            return "N/A"
    
    @property
    def destination_airport(self):
        try:
            return self.data["offerItems"][0]["segments"][-1]["arrival"]["iataCode"]
        except (KeyError, IndexError):
            return "N/A"
    
    @property
    def out_date(self):
        try:
            return self.data["offerItems"][0]["segments"][0]["departure"]["at"][:10]
        except (KeyError, IndexError):
            return "N/A"
    
    @property
    def return_date(self):
        try:
            return self.data["offerItems"][0]["segments"][-1]["arrival"]["at"][:10]
        except (KeyError, IndexError):
            return "N/A"
```

This is the **Data Transfer Object (DTO)** pattern—transforming complex API responses into simple, consistent objects.

## Service 4: NotificationManager - Alert Delivery

The NotificationManager handles all forms of user notification:

```python
class NotificationManager:
    def __init__(self):
        self.twilio_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.twilio_token = os.environ.get("TWILIO_AUTH_TOKEN")
    
    def send_whatsapp(self, message_body):
        """Send a WhatsApp message via Twilio"""
        if not self.twilio_sid:
            print("Twilio not configured, skipping notification")
            return
        
        client = Client(self.twilio_sid, self.twilio_token)
        
        message = client.messages.create(
            body=message_body,
            from_=f"whatsapp:{os.environ.get('TWILIO_PHONE_NUMBER')}",
            to=f"whatsapp:{os.environ.get('MY_PHONE_NUMBER')}"
        )
        
        print(f"WhatsApp sent: {message.sid}")
```

## The Main Orchestration Loop

The main.py ties everything together:

```python
import datetime as dt
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"  # London
STAY_DURATION = "3,20"    # Between 3 and 20 days

def main():
    # Initialize all services
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    
    # Get destinations from Google Sheets
    sheet_data = data_manager.get_destination_data()
    
    # Calculate departure date (today + 3 days)
    current_date = dt.date.today()
    departure_date = (current_date + dt.timedelta(days=3)).strftime('%Y-%m-%d')
    
    # Check each destination
    for destination in sheet_data:
        city = destination["city"]
        iata_code = destination["iataCode"]
        lowest_price = destination["lowestPrice"]
        
        print(f"Checking flights to {city}...")
        
        # Search for flights
        flights = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=iata_code,
            from_date=departure_date,
            duration=STAY_DURATION
        )
        
        # Find the cheapest flight
        if flights and "data" in flights:
            cheapest = FlightData(flights["data"][0])
            
            # Compare to target price
            if cheapest.price != "N/A" and cheapest.price < lowest_price:
                print(f"  → DEAL FOUND! £{cheapest.price} (target: £{lowest_price})")
                
                # Send notification
                message = f"Low price alert! £{cheapest.price} to fly from {cheapest.origin_airport} to {cheapest.destination_airport} on {cheapest.out_date} until {cheapest.return_date}."
                
                notification_manager.send_whatsapp(message)
        
        # Respect API rate limits
        time.sleep(2)

if __name__ == "__main__":
    main()
```

## The "Data Layering" Concept

This project demonstrates **data layering**—transforming data through multiple stages:

1. **Source Data**: Google Sheets (user configuration)
2. **Query Data**: Parameters sent to flight API
3. **Response Data**: Raw JSON from API
4. **Domain Data**: FlightData objects with clean properties
5. **Action Data**: Notification messages

Each layer is independent. You could swap the Google Sheet for a database, or swap WhatsApp for email, without changing other components.

## Why This Architecture Matters

This is how professional software is built. Each service:

- **Does one thing well**: DataManager only deals with Sheets
- **Can be tested independently**: Mock the API, test your logic
- **Can be swapped**: Change from Amadeus to Skyscanner without rewriting everything
- **Can be scaled**: Run different services on different machines if needed

## Rate Limiting and API Etiquette

A critical consideration when building multi-service applications: **respect rate limits**.

```python
import time

# BAD: Will get you banned
for destination in destinations:
    search_flights(destination)  # 1000 requests in 1 second

# GOOD: Respectful of API limits
for destination in destinations:
    search_flights(destination)
    time.sleep(2)  # Wait 2 seconds between requests
```

Most free APIs limit you to 5-10 requests per minute. The 2-second delay above allows 30 requests per minute—well within limits.

## Environment Setup

Set these variables before running:

```bash
export AMADEUS_API_KEY="your_amadeus_key"
export AMADEUS_API_SECRET="your_amadeus_secret"
export SHEETY_ENDPOINT="https://api.sheety.co/username/prices"
export SHEETY_TOKEN="your_bearer_token"
export TWILIO_ACCOUNT_SID="ACxxxxx"
export TWILIO_AUTH_TOKEN="your_token"
export TWILIO_PHONE_NUMBER="+1234567890"
export MY_PHONE_NUMBER="+1987654321"
```

## Try It Yourself

```bash
python "main.py"
```

The system will:
1. Read your destinations from Google Sheets
2. Search for flights to each city
3. Compare prices to your targets
4. Send WhatsApp alerts for any deals found

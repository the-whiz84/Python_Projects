# Day 39 - Flight Deal Search Architecture and Data Layering

Day 39 is where the course starts to feel much more like systems design. The flight deal finder is not one clever function. It is several small services working together:

- a data layer that stores destinations and thresholds
- a flight-search layer that talks to Amadeus
- a parsing layer that reduces raw offers into the cheapest useful result
- a notification layer that sends the alert

The key lesson is architectural layering. Each class exists so `main.py` can focus on business rules instead of low-level API details.

## 1. Treating Google Sheets as the Configuration Store

`DataManager` owns the destination dataset:

```python
response = requests.get(url=PRICES_ENDPOINT, headers=self.headers)
data = response.json()
self.destination_data = data["prices"]
```

This means the monitored cities, airport codes, and price thresholds are not hardcoded into the algorithm itself. Even though `main.py` currently shows a temporary local `sheet_data` list, the intended architecture is clear: the sheet is the configuration source.

That design matters because the monitored destinations are data, not code. The user should be able to change them without rewriting application logic.

`update_destination_codes()` reinforces that role:

```python
response = requests.put(
    url=f"{PRICES_ENDPOINT}/{city['id']}",
    json=new_data,
    headers=self.headers
)
```

The data layer is not only read-only. It also repairs or enriches the stored configuration by filling in missing IATA codes.

## 2. Isolating Amadeus Authentication and Query Logic

`FlightSearch` handles the Amadeus-specific responsibilities:

```python
self.token = self._get_new_token()
```

and:

```python
def check_flights(self, origin_city_code, destination_city_code, from_date, duration):
```

This is a strong separation boundary. The rest of the application should not need to know:

- how the bearer token is requested
- which endpoints are used
- how query parameters are shaped

That information belongs in the service that speaks to Amadeus, not in the orchestration layer.

The same applies to `get_destination_code()`. Airport-code lookup is conceptually related to flight search, so it lives in the same boundary instead of leaking into unrelated modules.

## 3. Reducing Raw Offers into a Stable Internal Object

The Amadeus response is still too large and awkward for the rest of the app. That is why the parsing layer exists:

```python
first_flight = data['data'][0]
lowest_price = float(first_flight["price"]["total"])
...
cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date)
```

Then `find_best_price()` iterates through all returned flights and keeps the cheapest one.

This reduction step is more important than it first appears. Most applications do not want to pass raw API payloads around forever. They want one internal representation that keeps only the fields relevant to the business decision.

That is what `FlightData` provides:

- price
- origin and destination codes
- departure date
- return date

Once the data is in that shape, the rest of the program becomes much easier to read.

## 4. Letting `main.py` Read Like a Deal Rule

Because the services are separated, the orchestration loop is simple:

```python
for destination in sheet_data:
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_date=departure_date,
        duration=STAY_DURATION
    )
    cheapest_flight = find_best_price(flights)
```

Then the actual rule is easy to see:

```python
if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
    notification_manager.send_whatsapp(...)
```

This is what good layering buys you. The top-level program expresses the domain rule:

- search for flights
- find the cheapest
- compare to threshold
- notify if it qualifies

without dragging token handling, JSON parsing, or Twilio details into the same loop.

## 5. Why This Architecture Matters Beyond Flights

The same pattern applies far beyond travel alerts:

- one layer for stored configuration
- one layer for external search or retrieval
- one layer for parsing into internal objects
- one layer for output or notification

That is why Day 39 is such a jump in complexity. It is teaching service composition, not just another API call.

## How to Run the Project

1. Open a terminal in this folder.
2. Configure the required environment variables for Sheety, Amadeus, and Twilio.
3. Run:

```bash
python main.py
```

4. Verify that the script checks each destination, finds the cheapest available option, and only sends a message when the price beats the configured threshold.

## Summary

Day 39 is a layering lesson disguised as a flight script. `DataManager` owns destination configuration, `FlightSearch` owns Amadeus communication, `FlightData` gives the app a stable internal deal object, and `NotificationManager` owns delivery. The orchestration loop stays readable because each service handles one responsibility cleanly.

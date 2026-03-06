# Day 40 - User-Based Flight Alerts and End-to-End Notification Flow

Day 40 takes the flight deal system from a personal automation into a user-aware alert service. The deal-finding core still matters, but the architectural focus shifts. Now the application has to think about recipients, message fan-out, and routing the same deal information through multiple channels.

That is a different kind of complexity from Day 39. The hard part is no longer only “find a cheap flight.” It is “find a cheap flight and deliver the right alert to the right set of users.”

## 1. Extending the Data Model from Destinations to Users

`DataManager` now has two endpoints:

```python
self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
```

The new method is:

```python
def get_customer_emails(self):
    response = requests.get(url=self.users_endpoint, headers=self.headers)
    data = response.json()
    self.customer_data = data["users"]
    return self.customer_data
```

This is the key structural change in the project. In Day 39, the configuration was about destinations and target prices. In Day 40, the application also needs user records. That means the data layer is now responsible for two related but distinct datasets:

- what deals are worth monitoring
- who should hear about them

Once a system supports multiple users, that separation becomes essential.

## 2. Keeping Deal Detection Independent from Recipient Handling

The main search loop remains familiar:

```python
for destination in sheet_data:
    flights = flight_search.check_flights(...)
    cheapest_flight = find_best_price(flights)
```

That is a good design choice. The logic that determines whether a flight is interesting should not depend on how many users exist or whether the final delivery method is WhatsApp or email.

Only after a qualifying deal is found does the code build the outbound message:

```python
message_body = (
    f"Low price alert! Only £{cheapest_flight.price} to fly from "
    f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
)
```

That separation is important. Deal evaluation is one concern. Recipient routing is another.

## 3. Adding Fan-Out Through Email Lists

The project introduces email delivery for multiple recipients:

```python
customer_email_list = ["[EMAIL_ADDRESS]", "[EMAIL_ADDRESS]", "[EMAIL_ADDRESS]"]
...
notification_manager.send_emails(email_list=customer_email_list, email_body=message_body)
```

The manager’s email method loops through every address:

```python
for email in email_list:
    self.connection.sendmail(
        from_addr=self.email,
        to_addrs=email,
        msg=f'Subject:Flight Club Alert - New Low Price Flight!\\n\\n{email_body}'.encode('utf-8')
    )
```

This is the real multi-user jump. The system is no longer producing a single side effect. One detected event can now produce many outbound messages.

That is a critical scaling concept for alerting systems.

## 4. Supporting More Than One Delivery Channel

The same deal can also go through WhatsApp:

```python
notification_manager.send_whatsapp(message_body)
notification_manager.send_emails(email_list=customer_email_list, email_body=message_body)
```

This is where the project starts to resemble a real notification service. The same event can be delivered differently depending on the audience and the integration layer available.

The important design lesson is that the deal message is built once, then handed to whichever channels are appropriate. That keeps the delivery logic modular instead of rebuilding message content separately for every channel.

## 5. Why Day 40 Feels More Like a Product System

The full end-to-end flow now looks like this:

1. load destination pricing rules
2. load customer recipients
3. search for current flights
4. select the cheapest qualifying result
5. build a standardized alert
6. fan that alert out to multiple channels and recipients

That is a much more product-like architecture than a one-user script. Even though the implementation is still small, the system now has the shape of a service that can support actual users.

## How to Run the Project

1. Open a terminal in this folder.
2. Configure the required environment variables for Sheety, Amadeus, Twilio, and SMTP email.
3. Run:

```bash
python main.py
```

4. Verify that when a destination beats its target price, the script builds one alert message and routes it through the configured notification channels.

## Summary

Day 40 extends the flight deal finder into a multi-user notification pipeline. The app now manages both destination rules and user recipients, keeps deal evaluation separate from recipient routing, and fans one qualifying event out through email and messaging channels. The lesson is about system shape: how a personal automation becomes a user-facing alert service.

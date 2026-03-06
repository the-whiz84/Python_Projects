# Day 40 - Flight Deals Finder 2.0: Multi-User Notifications

Today we're extending the Flight Deals Finder into a multi-user system. In Day 39, you built a deal alert system for yourself. Now, we'll extend it to support multiple users, each with their own preferences, getting notified when deals match their interests.

This lesson explores multi-user system design, scaling automation pipelines, and building notification systems that serve multiple recipients.

## The Multi-User Challenge

The transition from single-user to multi-user introduces several new considerations:

1. **User Data**: Where do we store user preferences and contact information?
2. **Customization**: Different users want different destinations and price points
3. **Notification Routing**: How do we send the right message to the right person?
4. **Scalability**: The system must handle growing user bases efficiently

Let's see how we solve each of these.

## Expanding the Data Model

We need to extend our Google Sheets to include user data. A second sheet (or table) tracks users:

| Email | Name | Phone | Active |
|-------|------|-------|--------|
| alice@example.com | Alice | +1234567890 | TRUE |
| bob@example.com | Bob | +1987654321 | TRUE |

And our prices sheet gains a column to track which users care about which destinations, or we assume all users want notifications for all deals (simpler to start):

```python
# In data_manager.py - New method for fetching users
def get_customer_emails(self):
    """Fetch user data from the users sheet"""
    headers = {"Authorization": f"Bearer {self.token}"}
    
    # Different endpoint for users sheet
    users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
    response = requests.get(users_endpoint, headers=headers)
    
    return response.json()["users"]
```

The key insight: we use the same Google Sheet infrastructure, just with different endpoints.

## Implementing Multi-User Notifications

Here's how NotificationManager extends to handle multiple recipients:

```python
class NotificationManager:
    def __init__(self):
        self.twilio_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.twilio_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = None
        if self.twilio_sid:
            from twilio.rest import Client
            self.client = Client(self.twilio_sid, self.twilio_token)
    
    def send_whatsapp(self, message_body):
        """Send to a single user"""
        if not self.client:
            return
        
        to_number = os.environ.get("MY_PHONE_NUMBER")
        
        message = self.client.messages.create(
            body=message_body,
            from_=f"whatsapp:{os.environ.get('TWILIO_PHONE_NUMBER')}",
            to=f"whatsapp:{to_number}"
        )
    
    def send_emails(self, email_list, email_body):
        """Send emails to multiple users"""
        # In production, you'd use SendGrid, AWS SES, or similar
        # For now, we'll simulate with print statements
        
        for email in email_list:
            print(f"Would send email to: {email}")
            print(f"Subject: Low Price Alert!")
            print(f"Body: {email_body}")
            print("-" * 40)
        
        # Real implementation would look like:
        """
        from email.mime.text import MIMEText
        import smtplib
        
        for email in email_list:
            msg = MIMEText(email_body)
            msg['Subject'] = 'Low Price Alert!'
            msg['From'] = os.environ.get("MY_EMAIL")
            msg['To'] = email
            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.environ.get("MY_EMAIL"), os.environ.get("MY_PASSWORD"))
                server.send_message(msg)
        """
```

## The Updated Main Loop

The orchestration now includes user management:

```python
def main():
    # Initialize services
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    
    # Get configuration
    sheet_data = data_manager.get_destination_data()
    
    # Get user list - KEY ADDITION
    customer_data = data_manager.get_customer_emails()
    customer_email_list = [row["email"] for row in customer_data if row.get("active") == "TRUE"]
    
    print(f"Checking deals for {len(customer_email_list)} users...")
    
    # Set up date parameters
    current_date = datetime.date.today()
    departure_date = (current_date + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    
    # Check each destination
    for destination in sheet_data:
        city = destination["city"]
        iata_code = destination["iataCode"]
        lowest_price = destination["lowestPrice"]
        
        print(f"\nChecking flights to {city}...")
        
        # Search flights
        flights = flight_search.check_flights(
            origin_city_code="LON",
            destination_city_code=iata_code,
            from_date=departure_date,
            duration="3,20"
        )
        
        # Check for deals
        if flights and "data" in flights:
            cheapest = FlightData(flights["data"][0])
            
            if cheapest.price != "N/A" and cheapest.price < lowest_price:
                print(f"  ✓ DEAL FOUND: £{cheapest.price} (target: £{lowest_price})")
                
                # Format the message
                message_body = (
                    f"Low price alert! £{cheapest.price} to fly "
                    f"from {cheapest.origin_airport} to {cheapest.destination_airport}, "
                    f"on {cheapest.out_date} until {cheapest.return_date}."
                )
                
                # Send to all users - KEY CHANGE
                notification_manager.send_whatsapp(message_body)
                notification_manager.send_emails(customer_email_list, message_body)
        
        # Rate limiting
        time.sleep(2)
    
    print(f"\nDeal check complete!")
```

## Notification Channel Strategy

Modern notification systems use multiple channels based on urgency and user preference:

### 1. Push (Immediate, High Priority)
- SMS/WhatsApp for time-sensitive deals
- Push notifications for mobile apps

### 2. Email (Medium Priority)
- Good for summaries and less urgent alerts
- Can include more detail than SMS

### 3. Dashboard (Low Priority)
- Log all deals to a shared sheet
- Users check when convenient

```python
def notify_all_channels(deal, user_list):
    # Channel 1: SMS/WhatsApp for premium users
    for user in premium_users:
        if user.sms_enabled:
            send_sms(user.phone, deal)
    
    # Channel 2: Email for everyone
    for user in user_list:
        if user.email_enabled:
            send_email(user.email, deal)
    
    # Channel 3: Log to shared sheet
    log_to_sheet(deal)
```

## Scalability Considerations

When building multi-user systems, think about these factors:

### 1. API Rate Limits
```python
# A naive approach hits rate limits fast:
for user in users:  # 1000 users
    send_notification(user)  # 1000 API calls
```

Solution: Batch notifications or use message queues

### 2. Cost Management
- Twilio charges per message
- Email services have quotas
- Track usage and set alerts

### 3. Error Handling
```python
def notify_users(deal, user_list):
    errors = []
    
    for user in user_list:
        try:
            send_notification(user, deal)
        except Exception as e:
            errors.append({"user": user.id, "error": str(e)})
    
    # Report errors but don't fail completely
    if errors:
        log_errors(errors)
        notify_admin(f"Failed to notify {len(errors)} users")
```

### 4. User Preference Management
```python
class User:
    def __init__(self, data):
        self.email = data["email"]
        self.phone = data["phone"]
        self.name = data["name"]
        self.active = data.get("active", "TRUE") == "TRUE"
        self.preferred_destinations = data.get("destinations", "").split(",")
        self.max_price = float(data.get("max_price", 9999))
    
    def wants_notification_for(self, destination, price):
        if not self.active:
            return False
        
        # Check destination preference
        if self.preferred_destinations and destination not in self.preferred_destinations:
            return False
        
        # Check price preference
        if price > self.max_price:
            return False
        
        return True
```

## Production Enhancements

For a real production system, you'd add:

### 1. Scheduling
Run the deal checker on a schedule using cron or cloud scheduler:
```bash
# Run every 6 hours
0 */6 * * * python main.py
```

### 2. Caching
Cache IATA codes and flight search results to reduce API calls:
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_iata_code(city_name):
    # Expensive API call - cached for 24 hours
    return api.lookup_city(city_name)
```

### 3. Logging
```python
import logging

logging.basicConfig(
    filename='flight_deals.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Usage
logger.info(f"Checking {city}...")
logger.info(f"Deal found: £{price}")
logger.warning(f"Rate limit approached")
```

### 4. Metrics
Track what matters:
- Deals found per run
- Notifications sent
- API costs
- User growth

## Try It Yourself

```bash
python "main.py"
```

The system now:
1. Reads user emails from Google Sheets
2. Checks flight deals for all configured destinations
3. Sends WhatsApp + Email notifications to every user when deals are found

Set up a users sheet with email addresses to see the multi-user functionality in action.

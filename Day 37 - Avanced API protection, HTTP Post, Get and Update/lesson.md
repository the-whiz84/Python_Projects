# Day 37 - Advanced API Protection, HTTP Methods, and Authentication

Today we're diving deep into how the web actually works at the protocol level. You've been making GET requests throughout this course, but now you'll learn about POST, PUT, and DELETE—the other HTTP methods that let you create, update, and delete data through APIs.

We'll also explore HTTP headers for authentication, which is a more secure alternative to API keys in query parameters. Finally, you'll see how to format dates properly for API requests using the datetime module.

This knowledge is essential for working with any modern web service, from habit trackers to flight search engines.

## Understanding HTTP Methods

HTTP (Hypertext Transfer Protocol) defines several "methods" or "verbs" that tell the server what kind of action you want to take. Each method has a specific purpose:

### GET - Reading Data

GET is what you've been using so far. It requests data from a specified resource. GET requests should only retrieve data and have no other effect on the server.

```python
import requests

# This is a GET request
response = requests.get("https://api.example.com/users")
users = response.json()
```

GET requests:
- Are cached by browsers and servers
- Can be bookmarked
- Remain in browser history
- Should never modify server state
- Have length limitations (URLs have a max length)

### POST - Creating Data

POST sends data to the server to create a new resource. It's like submitting a form—the data goes in the request body, not the URL.

```python
# Creating a new user
new_user = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

response = requests.post(
    "https://api.example.com/users",
    json=new_user  # Automatically serializes to JSON and sets Content-Type
)

# Check the response
if response.status_code == 201:
    created_user = response.json()
    print(f"Created user with ID: {created_user['id']}")
```

POST requests:
- Send data in the request body (not URL)
- Don't get cached
- Don't remain in browser history
- Can send any amount of data
- Typically return 201 (Created) on success

### PUT - Updating Data (Complete)

PUT replaces an existing resource entirely. If you PUT to `/users/123` with new user data, it replaces whatever was at that ID.

```python
# Updating a user completely
updated_user = {
    "name": "John Smith",
    "email": "john.smith@example.com",
    "age": 31
}

response = requests.put(
    "https://api.example.com/users/123",
    json=updated_user
)

if response.status_code == 200:
    print("User updated successfully")
```

### PATCH - Updating Data (Partial)

PATCH modifies specific fields of an existing resource without replacing everything:

```python
# Just updating the email, keeping other fields unchanged
patch_data = {
    "email": "newemail@example.com"
}

response = requests.patch(
    "https://api.example.com/users/123",
    json=patch_data
)
```

### DELETE - Removing Data

DELETE removes a resource entirely:

```python
response = requests.delete("https://api.example.com/users/123")

if response.status_code == 204:
    print("User deleted successfully")
```

## Understanding HTTP Headers

HTTP headers provide additional information about the request or response. They're key-value pairs that travel with the request but aren't part of the URL or body.

### Common Request Headers

```python
headers = {
    "Content-Type": "application/json",  # What we're sending
    "Accept": "application/json",         # What we want back
    "Authorization": "Bearer token123",   # Authentication
    "User-Agent": "MyApp/1.0",          # Client identification
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### Authentication Headers

There are several ways to authenticate with APIs:

**1. API Key in Header**
```python
headers = {
    "X-API-Key": "your_api_key_here"
}
response = requests.get(url, headers=headers)
```

**2. Bearer Token (OAuth, JWT)**
```python
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
response = requests.get(url, headers=headers)
```

**3. Basic Authentication**
```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    url,
    auth=HTTPBasicAuth('username', 'password')
)
```

The Authorization header is more secure than API keys in URLs because:
- It's not logged in server access logs (URLs often are)
- It can be sent over SSL/TLS (encrypted connection)
- It supports expiration and refresh tokens

## Real-World Example: Pixela Habit Tracker

Pixela is a habit-tracking API that lets you create graphs and log pixel data. It demonstrates all four HTTP methods:

### Creating a Graph (POST)

```python
import requests
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": "myusername",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(PIXELA_ENDPOINT, json=user_params)
print(response.json())
```

### Adding a Pixel (POST)

```python
graph_endpoint = "https://pixe.la/v1/users/myusername/graphs"

pixel_config = {
    "date": "20240315",
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": os.environ.get("PIXELA_TOKEN")
}

response = requests.post(graph_endpoint, json=pixel_config, headers=headers)
```

Notice we're using `X-USER-TOKEN` in the headers rather than in the URL. This is the authentication method Pixela uses.

### Getting Data (GET)

```python
# Get all pixels from a graph
response = requests.get(graph_endpoint, headers=headers)
pixels = response.json()

# Get a specific date
specific_date = "https://pixe.la/v1/users/myusername/graphs/default/20240315"
response = requests.get(specific_date, headers=headers)
```

### Updating a Pixel (PUT)

```python
update_endpoint = "https://pixe.la/v1/users/myusername/graphs/default/20240315"

update_config = {
    "quantity": "2"  # Changing from 1 to 2
}

response = requests.put(update_endpoint, json=update_config, headers=headers)
```

### Deleting a Pixel (DELETE)

```python
delete_endpoint = "https://pixe.la/v1/users/myusername/graphs/default/20240315"

response = requests.delete(delete_endpoint, headers=headers)
```

## Formatting Dates for APIs

APIs almost always expect dates in specific formats. The ISO 8601 format is the most common: `YYYY-MM-DD`.

Python's datetime module makes this straightforward:

```python
from datetime import datetime, timedelta

# Today's date in ISO format
today = datetime.now()
print(today.strftime("%Y-%m-%d"))
# Output: 2024-03-15

# A specific date
specific = datetime(year=2024, month=9, day=2)
print(specific.strftime("%Y-%m-%d"))
# Output: 2024-09-02

# Calculate a date in the future
future_date = today + timedelta(days=30)
print(future_date.strftime("%Y-%m-%d"))
# Output: 2024-04-14
```

The `strftime` method (string format time) converts datetime objects to strings using format codes:

| Code | Meaning | Example |
|------|---------|---------|
| %Y | 4-digit year | 2024 |
| %m | 2-digit month | 03 |
| %d | 2-digit day | 15 |
| %H | Hour (24-hour) | 14 |
| %M | Minute | 30 |
| %S | Second | 45 |

Common format strings:
- `"%Y-%m-%d"` → "2024-03-15"
- `"%Y%m%d"` → "20240315" (Pixela uses this)
- `"%d/%m/%Y"` → "15/03/2024" (European format)
- `"%Y-%m-%dT%H:%M:%S"` → "2024-03-15T14:30:45" (ISO 8601 with time)

## Status Codes Reference

Understanding HTTP status codes is crucial for debugging API issues:

**2xx - Success**
- 200: OK - Request succeeded
- 201: Created - Resource successfully created
- 204: No Content - Success, no content to return

**4xx - Client Errors**
- 400: Bad Request - Invalid syntax
- 401: Unauthorized - Authentication required
- 403: Forbidden - Access denied
- 404: Not Found - Resource doesn't exist
- 429: Too Many Requests - Rate limited

**5xx - Server Errors**
- 500: Internal Server Error - Server crashed
- 503: Service Unavailable - Server overloaded

## Best Practices

1. **Always check response status**: Don't assume requests succeeded
```python
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
else:
    print(f"Error: {response.status_code}")
```

2. **Use raise_for_status()** for critical failures
```python
response.raise_for_status()  # Raises exception for 4xx/5xx
```

3. **Handle rate limits**: Add delays between requests
```python
import time
for item in items:
    response = requests.get(f"url/{item}")
    time.sleep(1)  # Wait 1 second between requests
```

4. **Keep secrets in environment variables**, never in code

5. **Log requests** when debugging
```python
import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
```

## Try It Yourself

```bash
python "main.py"
```

The main.py demonstrates date formatting:
```python
from datetime import datetime

today_date = datetime.now()
print(today_date.strftime("%Y%m%d"))

any_other_day = datetime(year=2024, month=9, day=2)
print(any_other_day.strftime("%Y%m%d"))
```

Explore `habit_tracker.py` to see how the full Pixela integration works with all four HTTP methods.

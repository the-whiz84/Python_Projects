# Day 37 - REST Operations, Headers, and Date Formatting

Day 37 is where API work stops being read-only. Until now, most network examples in the course have been `GET` requests: ask a service for data, parse the response, and use it locally. This lesson is different because it introduces the full set of common HTTP operations used by real APIs. That matters because the moment your program starts creating, updating, or deleting remote records, you are no longer just consuming a service. You are participating in the service’s state changes.

The Pixela habit-tracker examples in this folder are a good vehicle for that lesson because they make the API feel almost like a remote spreadsheet. You define a user, create a graph, post a pixel for a specific date, update it, and remove it when needed.

## 1. Thinking of HTTP Methods as Intent, Not Syntax

The notes in `main.py` lay out the common methods:

```python
# GET - requests.get()
# POST - requests.post()
# PUT - requests.put()
# DELETE - requests.delete()
```

Those four lines look simple, but they represent one of the most important ideas in web development: the request method communicates intent.

- `GET` asks for data without changing the server state
- `POST` creates a new record
- `PUT` replaces or updates an existing record
- `DELETE` removes a record

This is why REST-style APIs feel predictable when they are designed well. Once you know the endpoint and the method, you can often infer what the request is supposed to do before even reading the documentation in detail.

That mental model is much more useful than memorizing function names in `requests`.

## 2. Why `POST`, `PUT`, and `DELETE` Feel Different from `GET`

With a `GET` request, you usually care about the response body. With the write-oriented methods, the response often matters less than the side effect:

- did the graph get created?
- did the pixel update succeed?
- was the record deleted?

That difference changes how you think about API code. Instead of “fetch and inspect,” the workflow becomes “send a well-formed request, check whether the remote system accepted the change, and continue only if it did.”

That is the transition from data retrieval to remote state management.

## 3. Using Headers for Authentication and API Context

The folder notes introduce a token header:

```python
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=coding_graph_endpoint, headers=headers, json=pixel_config)
```

This is an important step beyond putting credentials directly into a URL. Headers are request metadata. They let your client provide secrets or context without mixing those details into the endpoint path itself.

There are two reasons that matters:

1. It separates authentication from resource location.
2. It matches how many modern APIs expect tokens to be sent.

In practice, once you start working with more APIs, you will see the same pattern repeatedly:

- an auth header
- a JSON body
- a status code that tells you whether the operation succeeded

That recurring structure is part of what makes HTTP APIs learnable.

## 4. Formatting Data to Match an External Contract

The `datetime` examples in `main.py` show this:

```python
from datetime import datetime

today_date = datetime.now()
print(today_date.strftime("%Y%m%d"))

any_other_day = datetime(year=2024, month=9, day=2)
print(any_other_day.strftime("%Y%m%d"))
```

This is more than a date-formatting trick. It is a concrete example of a broader rule: external systems usually require data in a very specific format.

Inside Python, you may hold a `datetime` object. But the remote API does not want your local Python object. It wants a serialized string that follows its contract exactly.

That is a recurring integration lesson:

- keep rich local objects for your own logic
- convert them into exact strings or JSON fields when talking to the API

If you skip that conversion step or get it slightly wrong, the request is rejected even though your local data may be perfectly valid.

## 5. How This Fits the Pixela Habit Tracker Workflow

Even though `main.py` mostly contains notes and smaller examples, the folder is preparing you for the habit tracker pattern:

1. create a remote resource
2. authenticate each write request
3. serialize dates correctly
4. use the correct method for each change

That is what makes the lesson more important than it first appears. It is not just introducing extra functions from `requests`. It is teaching the shape of CRUD-style API interaction.

Once you understand that shape, a lot of later projects become easier:

- spreadsheets exposed as APIs
- REST services with bearer tokens
- apps that update server-side resources over time

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Confirm that the `strftime("%Y%m%d")` output matches the compact date format many APIs expect.
4. Review `habit_tracker.py` in the same folder and map each remote action to its intended HTTP method.

## Summary

Day 37 is the point where API usage becomes two-way. You move from reading remote data to managing remote resources with `POST`, `PUT`, and `DELETE`, learn why auth headers are a safer and cleaner pattern than query-string secrets, and practice converting local data into the exact serialized format an API expects. The main lesson is not the syntax of `requests`, but the contract between your code and a remote service.

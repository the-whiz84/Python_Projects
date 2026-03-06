# Day 54 - Introduction to Web Development with Flask

Today marks a huge transition in your journey as a developer. We are moving from being the "client" who scrapes and controls other people's websites to being the "server" that actually builds and delivers the website.

To do this, we are starting our journey with **Flask**, one of the most popular web frameworks for Python. But before we can build complex, database-backed web applications, we need to understand the underlying theory of the Client-Server model and the "magic" that makes Flask routing work: **Python Decorators.**

## What is a Web Framework?

When you type `google.com` into your browser, your computer sends an HTTP Request across the internet to one of Google's servers. That server runs code to figure out what you want, and sends back an HTTP Response containing HTML, CSS, and JavaScript.

Writing a web server entirely from scratch in raw Python is brutal. You'd have to manually parse the HTTP headers, manage socket connections, and handle raw binary data.

A **web framework** like Flask handles all the networking plumbing (often standardized via a spec called WSGI) so you only have to focus on the business logic. Flask is considered a "micro-framework" because it is minimalist and unopinionated, meaning it doesn't force a specific folder structure or database on you.

## The First "Hello World" App

Creating a web server in Flask is remarkably elegant:

```python
from flask import Flask

# Initialize the Flask application
# __name__ is a special Python variable that evaluates to the name of the current module.
# This helps Flask know where to look for templates and static files later.
app = Flask(__name__)

# The Routing Decorator
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# Run the server only if the script is run directly
if __name__ == "__main__":
    app.run()
```

When you hit "run", Flask binds to localhost port `5000`. If you visit `http://127.0.0.1:5000/`, your browser sends a GET request to your Python script. The Flask router sees the `/` path, finds the `hello_world()` function associated with it, executes the function, and packages the returned physical string into an HTTP Response.

## The Magic Under the Hood: Decorators

You've noticed the `@app.route("/")` line. That `@` symbol signifies a **Decorator.** To understand what it does, we have to look closely at Python's architecture.

In Python, functions are "first-class objects," meaning we can treat a function exactly like a variable. We can pass it into another function, assign it to a name, or return it from a function.

A **decorator** is just a function that wraps _another_ function to give it extra behavior without ever modifying the core code of the original function.

Let's build a decorator from scratch:

```python
import time

# 1. We define a decorator that takes a function as an argument
def delay_decorator(function):

    # 2. We define the "wrapper" inside. This is a closure.
    def wrapper_function():
        time.sleep(2) # We add our extra behavior (delay)
        function()    # We execute the original function that was passed in
        # We could add more behavior here after execution!

    # 3. We return the wrapper. We are NOT executing it yet.
    return wrapper_function

# 4. We apply the decorator using syntactic sugar
@delay_decorator
def say_hello():
    print("Hello!")
```

When you eventually call `say_hello()`, Python doesn't actually run your original `say_hello()`. It runs the `wrapper_function()` returned by the decorator!

This is exactly how Flask routing works. The `@app.route` decorator essentially says: "Take the function right below me, and instead of just letting it sit there, register it inside Flask's internal routing dictionary so that when a web request comes in for this path, I can execute it and return the result to the browser."

## Running your Flask Server

1. Make sure you have Flask installed:
   ```bash
   pip install flask
   ```
2. Run your server script:
   ```bash
   python "hello.py"
   ```
3. Open your browser and visit `http://127.0.0.1:5000/`.
4. Try visiting `http://127.0.0.1:5000/bye` to see your other route in action!

## Summary

Today we swapped our "scraper" hat for an "architect" hat. You learned the fundamentals of the Client-Server request lifecycle, set up a basic Flask server, and peeled back the curtain on Decorators—the functional programming concept that makes Flask's routing so clean.

Tomorrow, we're going to dive deeper into routing. We'll learn how to pass variables directly through the URL and how to render dynamic HTML content!

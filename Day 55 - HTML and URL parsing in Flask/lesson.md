# Day 55 - HTML and URL Parsing in Flask: The Higher/Lower Game

Yesterday we set up a basic Flask server and returned a static string. Today, we're building an interactive game out of URL paths. We are creating a "Higher/Lower" number guessing game entirely driven by the URL the user visits.

This project introduces two foundational backend engineering concepts: **Dynamic URL Routing** and **Server-Side Rendered (SSR) HTML**.

## Dynamic URL Routing

In a modern web application, you don't create a new Python function for every single user profile page (e.g., `/user/1`, `/user/2`, etc.). Instead, you define dynamic routes that extract variables directly from the URL path.

Flask handles this beautifully with angle brackets `<>` in the route decorator:

```python
# The <int:guess> tells Flask: "Expect a variable here in the URL, and cast it to an integer."
@app.route("/<int:guess>")
def guess_number(guess):
    # 'guess' is now available inside our function!
    if guess < chosen_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"
```

When a user visits `http://127.0.0.1:5000/7`, Flask's routing engine extracts the `7`, asserts that it is an integer, and passes it as the `guess` argument into our `guess_number()` function. This is the bedrock of building RESTful APIs and dynamic web apps.

## Server-Side Rendered (SSR) HTML

In our `return` statements, we aren't just sending back plain text strings anymore; we are sending back raw HTML strings containing CSS styles and `<img>` tags.

```python
return '<div style="text-align: center"><h1 style="color: blue">Too high, try again!</h1><img src="https://media.giphy.com/media/TZBED1pP5m8N2/giphy.gif" /></div>'
```

When the browser receives this string in the HTTP Response, it parses the string into a Document Object Model (DOM) tree and renders it visually.

Because we are constructing this HTML string inside Python before sending it, we are performing **Server-Side Rendering**. The content is generated dynamically based on the state of the backend (in this case, whether the `guess` matches the `chosen_number`).

## Understanding State in a Minimal Backend

Take a look at how `chosen_number` is initialized:

```python
from random import randint

# We generate the secret number ONCE when the server boots up.
chosen_number = randint(0, 9)

app = Flask(__name__)
# ...
```

Because `chosen_number` is defined globally outside the request context, it persists across multiple page loads. Until the server is restarted, `chosen_number` stays exactly the same, allowing the user to repeatedly guess by visiting different URLs (like `/3`, then `/8`, then `/5`).

## Advanced Decorators (from `main.py`)

In `main.py`, we continued our deep dive into decorators. We built custom decorators to alter the HTML string returned by a function:

```python
def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"
```

When you stack decorators, they execute from the innermost (closest to the function) to the outermost. `bye()` returns `"Bye!"`, `make_underline` wraps it in `<u>`, `make_italic` wraps it in `<em>`, and `make_bold` wraps it in `<b>`. The final output sent to the browser is `<b><em><u>Bye!</u></em></b>`.

## Running the Higher/Lower Game

1. Make sure you have Flask installed in your environment:
   ```bash
   pip install flask
   ```
2. Run the game server:
   ```bash
   python "higher_lower.py"
   ```
3. Open your browser and visit `http://127.0.0.1:5000/`.
4. Play the game by appending numbers to the URL, for example: `http://127.0.0.1:5000/4`.

## Summary

Today you evolved your Flask server from a static text responder into an interactive, stateful application. You learned how to parse dynamic integers directly out of the URL path and how to construct HTML dynamically on the server and deliver it to the browser for rendering.

Tomorrow, we replace sending messy strings of HTML with actual template files, learning how to properly separate our Backend logic from our Frontend layout!

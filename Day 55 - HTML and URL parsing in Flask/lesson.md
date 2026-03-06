# Day 55 - Dynamic Routes and HTML Responses in Flask

Day 55 extends the first Flask lesson by making the response depend on the URL itself. Instead of returning the same page every time, the app reads values out of the path, passes them into Python functions, and builds different HTML responses based on those values.

This is another place where a little theory helps. Dynamic routes, path converters, and server-side HTML generation are foundational Flask ideas. They are simple in the code, but they explain how a web application can feel interactive before we even introduce templates.

## 1. Routes Can Capture Values from the URL

The first project file shows a small example of dynamic routing:

```python
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name}! You are {number} years old.</p>"
```

This route teaches two important ideas:

- parts of the URL can be treated as variables
- Flask can convert those values into Python types before passing them into the function

So if the browser visits `/username/Ana/25`, Flask extracts `"Ana"` as `name` and `25` as an integer `number`.

That feature is one of the reasons Flask feels expressive. The URL itself becomes part of the program's input.

## 2. Path Converters Add Validation as Well as Convenience

The `<int:number>` syntax does more than save a conversion step. It also constrains the route. Flask will match the route only when that segment looks like an integer.

That is worth understanding because it means the route is doing two jobs at once:

- parsing data from the path
- validating the expected shape of the data

This becomes especially useful later when routes need IDs, slugs, or other typed parameters.

## 3. Returning HTML Strings Is a Simple Form of Server-Side Rendering

The home route in `main.py` returns a raw HTML string:

```python
@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>This is a paragraph</p><img src='https://i.giphy.com/media/.../giphy.gif' />"
```

That is still valid Flask. When the browser receives the response, it parses the HTML and renders it normally.

This is worth calling out because it introduces server-side rendering in its simplest form. The server constructs the response content first, and the browser displays whatever the server returns. Later we will switch to templates because writing large HTML strings directly in Python becomes messy very quickly, but the core idea is already here.

## 4. Decorators Can Change the Returned HTML

The same file also revisits decorators, but now in a more visual way:

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
    return "<h2>Bye!</h2>"
```

This is a nice bridge between pure Python theory and Flask. Each decorator wraps the returned HTML in another tag. By the time the browser receives the response, the original function output has been modified several times.

That makes decorators feel less abstract. Instead of talking about wrappers in the air, you can actually see the transformed HTML.

## 5. The Higher-Lower App Uses the URL as Game Input

The more interesting Flask example lives in [higher_lower.py](/Users/wizard/Developer/Python_Projects/Day%2055%20-%20HTML%20and%20URL%20parsing%20in%20Flask/higher_lower.py). It creates a random secret number once and then evaluates guesses based on the URL:

```python
chosen_number = randint(0, 9)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < chosen_number:
        return '<div style="text-align: center"><h1 style="color: red">Too low, try again!</h1>...</div>'
    elif guess > chosen_number:
        return '<div style="text-align: center"><h1 style="color: blue">Too high, try again!</h1>...</div>'
    else:
        return '<div style="text-align: center"><h1 style="color: green">You found me!</h1>...</div>'
```

This is a great teaching project because it shows how little code is needed for a genuinely interactive web app. The user changes the URL, Flask passes the number into the route, Python compares it to the secret value, and the response changes.

## 6. Global State Persists While the Server Is Running

One subtle but important concept in this file is where the random number is created:

```python
chosen_number = randint(0, 9)
```

Because that line runs when the server starts, the value stays the same across multiple requests until the app restarts. That is why the user can keep guessing different URLs against the same hidden number.

This is a helpful early lesson about state in web applications. Not every value is recreated for every request. Values defined at module level can persist as long as the process is alive.

It is a simple example, but it introduces the idea that request handling and application state are related, not identical.

## 7. The Response Is Built from Python Logic

The higher-lower game also reinforces the request-response model from Day 54. The browser is not "running the game logic" itself. It sends a request to a route such as `/7`, and the Flask function decides which HTML string to send back.

That means the app is already dynamic even without forms, JavaScript, or a database. The Python code on the server is enough to change what the user sees.

This is one reason Flask is such a good teaching framework. Small examples still reveal the real shape of server-side programming.

## 8. Why Templates Are the Next Step

This lesson intentionally uses inline HTML strings so you can focus on routing and response behavior. But it also exposes a limitation: large strings with inline CSS and image tags become hard to read and hard to maintain.

That is exactly why templates come next. Once the route logic makes sense, the natural improvement is to move the HTML into separate files and let Python pass data into them more cleanly.

So Day 55 is both a lesson in dynamic routes and a setup for better frontend-backend separation.

## How to Run the Project

Install Flask if needed:

```bash
pip install flask
```

Run the route and decorator example:

```bash
python main.py
```

Try these URLs:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/bye`
- `http://127.0.0.1:5000/username/Ana/25`

Run the higher-lower game:

```bash
python higher_lower.py
```

Then visit `http://127.0.0.1:5000/` and try guesses by appending numbers such as `/3` or `/8`.

## Summary

Day 55 shows how Flask turns URL paths into real program input. Dynamic routes capture variables, path converters validate and cast them, and route functions generate different HTML responses based on Python logic. The higher-lower game makes those ideas concrete, while the decorator examples continue building the Python concepts that help Flask feel understandable instead of magical.

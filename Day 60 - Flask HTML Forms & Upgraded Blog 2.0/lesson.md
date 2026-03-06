# Day 60 - Flask HTML Forms: Enabling User Input

For the past few days, the communication between the browser and our server has been entirely one-way. A user types our URL (a `GET` request), and our server sends back HTML. The user consumes it passively.

Today, we bring bidirectional communication to our Upgraded Blog. We created a Contact Form that allows the user to construct a payload of data (their name, email, and message) and send it _back_ to our Python server to be processed (an HTTP `POST` request).

## The HTML Form Architecture

To send data to a server, we must construct an HTML `<form>`. A form requires three critical architectures:

1. **The `action`**: Where should this data be sent? (Usually an endpoint URL).
2. **The `method`**: How should the data be sent? (Usually `POST`).
3. **The `name` attributes**: How do we label the data so the backend can identify it?

```html
<!-- The action points to our /contact route, using the POST method -->
<form action="{{ url_for('contact') }}" method="POST">
  <!-- The 'name' attribute is the key that Python will use to extract this value -->
  <input type="text" name="user_name" placeholder="Your Name" />
  <input type="email" name="user_email" placeholder="Your Email" />
  <textarea name="user_message" placeholder="Your Message"></textarea>

  <button type="submit">Send</button>
</form>
```

When the user clicks the Submit button, the browser packages the input fields into a hidden payload that looks like a key-value dictionary:
`{"user_name": "Radu", "user_email": "radu@example.com", "user_message": "Hello!"}`

## Handling POST Requests in Flask

By default, Flask routes _only_ accept `GET` requests for security reasons. If we try to submit our form to `/contact`, Flask will reject it. We must explicitly authorize the route to accept `POST` requests inside the decorator.

```python
from flask import request

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # We must check the method Type to determine the logic branch
    if request.method == "POST":
        # Extract the payload dictionary sent by the browser
        data = request.form

        # Access the specific fields using the 'name' attributes from the HTML
        name = data["user_name"]
        email = data["user_email"]
        message = data["user_message"]

        # Do something with the data (e.g., send an email)
        print(f"{name} sent you a message: {message}")

        return "<h1>Successfully sent your message!</h1>"

    # If it's a normal GET request, just render the blank form
    return render_template("contact.html")
```

### The Global `request` Object

Notice that we imported `request` from `flask`. This is a magical global object provided by the framework. Whenever a browser hits an `@app.route`, Flask secretly fills this `request` object with all the metadata about that specific HTTP request (the headers, the IP address, the HTTP method, and any Form payloads).

## Integrating with SMTP

In `main_upgraded_blog_2_0.py`, we didn't just print the user's message; we orchestrated our backend architecture. We took the extracted form data and immediately piped it into the `smtplib` module we learned back in Day 32. Or backend server dynamically acts as an email client, forwarding the contact form entry straight to our personal Gmail inbox!

## Running the Contact Form

1. Ensure your environment has the required environment variables used by `smtplib`:
   - `MY_EMAIL` (Your sender email)
   - `MY_EMAIL_PASSWD` (Your email App Password)
2. Run the server:
   ```bash
   python "main_upgraded_blog_2_0.py"
   ```
3. Visit `http://127.0.0.1:5000/contact`.
4. Fill out the form and hit "Send". Check your email inbox to see the server's automated response!

## Summary

Today you unlocked the final piece of the Web Development triad: Server-to-Client Delivery (GET), Frontend Layout (HTML/CSS), and Client-to-Server Data Flow (POST). You successfully built an HTML form, authorized a Flask route to accept POST payloads, extracted the user data via the `request.form` dictionary, and integrated it into a backend email automation pipeline.

Tomorrow, we address a glaring issue with raw HTML forms: lack of security and validation. If a user types random letters instead of an email address into our form, our backend will crash. Enter **Flask-WTF**!

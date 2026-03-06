# Day 97 - E-Commerce Website Structure and UI Composition

This project is more about website structure than backend complexity. The Flask app is small, but it establishes the page layout of an e-commerce site: home, shop, about, and contact. That makes the lesson a good one about composition, routing, and frontend organization rather than data processing.

The value here is building a believable site skeleton that can later support real products, carts, and checkout logic.

## 1. Use Flask Routes to Define the Store Structure

The app starts with a very small route layer:

```python
app = Flask(__name__)
bootstrap = Bootstrap5(app)
```

Then defines the main pages:

```python
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")
```

Along with:

```python
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
```

This is the right level of complexity for a storefront scaffold. The app establishes the navigation model first. It does not prematurely add carts, databases, or payment flows before the page structure exists.

## 2. Use Bootstrap to Accelerate Layout Work

The project enables Bootstrap immediately:

```python
bootstrap = Bootstrap5(app)
```

That is a practical choice for a site like this. E-commerce pages depend heavily on consistent spacing, cards, grids, navigation, and forms. Bootstrap gives the project a predictable visual system without forcing the app to invent all of that from scratch.

This is one of those cases where a CSS framework is not just convenience. It is a way to keep the layout work proportional to the project scope.

## 3. Treat the App as a Frontend Foundation

Right now the routes are simple because the point of the project is page composition. That is still valuable. A real storefront needs:

- a landing page
- a shop page
- informational pages
- a contact path

This project establishes those building blocks so later iterations could attach actual product data and business logic.

In other words, the current app is intentionally more scaffold than engine. That is fine. Good software often grows from a solid information architecture rather than from premature backend complexity.

## How to Run the E-Commerce Site

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   python main.py
   ```
3. Open the local site and verify:
   - `/` renders the home page
   - `/shop` renders the storefront page
   - `/about` and `/contact` render the supporting pages

## Summary

Today, you built the structural shell of an e-commerce site. The Flask routes define the page map, Bootstrap provides the layout system, and the app creates a foundation that future product, cart, and checkout features could plug into. The lesson is that site architecture comes first, even when the business logic is still minimal.

# Day 15 - Local Development Workflow and Procedural App Design

Today we're building a virtual Coffee Machine. This machine needs to hold ingredients (water, milk, coffee beans), accept coins, make drinks, give change, and ensure it actually has enough ingredients before it takes your money.

This is the first project where we aren't just making a quick game or a math script — we are building a stateful application. This means the program has to remember things over time (like how much water is left) and make decisions based on that memory.

## Managing State with Dictionaries

In `data.py`, we store the machine's initial inventory and the recipes for the drinks:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

Every time someone buys a coffee, those numbers need to go down. Notice how we do this in `main.py`:

```python
def serve_coffee(order_ingredients, inventory):
    for item in order_ingredients:
        inventory[item] -= order_ingredients[item]
```

This is a great example of modifying state. We loop through the ingredients required for the specific drink (e.g., `"water"`, `"coffee"`) and subtract those amounts directly from the machine's `inventory` dictionary. Because dictionaries are mutable in Python, those changes are permanent for the rest of the program's run time.

We also track the machine's profit using a global variable:

```python
money = 0

def transaction_successful(money_inserted, drink_price):
    if money_inserted >= drink_price:
        # ...
        global money
        money += drink_price
        return True
```

Normally we try to avoid `global` variables, but for a simple machine-wide state like total profit, it gets the job done without having to pass a `profit` variable into every single function.

## The Check-Then-Act Pattern

A huge part of application design is making sure you don't do something stupid — like taking the user's money when you don't have enough water to make their espresso.

Look at how the main loop is structured:

```python
if order in ("espresso", "latte", "cappuccino"):
    drink = MENU[order]

    # 1. Check resources FIRST
    if check_resources(drink["ingredients"]):

        # 2. THEN ask for money
        amount = insert_coins()

        # 3. Check if the payment was enough
        if transaction_successful(amount, drink["cost"]):

            # 4. ONLY THEN make the coffee
            serve_coffee(drink["ingredients"], resources)
            print(f"Here is your ☕{order}. Enjoy!")
```

This is called defensive programming. We establish a series of gates (`if check_resources`, `if transaction_successful`). Only if the user successfully passes through all the gates do we actually modify the inventory and print the success message.

## Hidden Commands

Applications often have "admin" or "developer" features that regular users don't see. If you run the program and type `report` instead of a coffee name, the machine prints out its current inventory and profit. If you type `off`, it shuts down entirely. These aren't listed on the main menu prompt, but they exist in the code to give us control over the machine.

## Try it yourself

```bash
python "main.py"
```

Try ordering a few lattes in a row. Eventually, the machine will run out of water or milk and refuse to serve you!

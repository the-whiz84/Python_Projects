# Day 15 - Local Development Workflow and Procedural App Design

Today we're building a virtual coffee machine. The program has inventory, prices, hidden admin commands, payment handling, and drink preparation rules. That makes it the first beginner project that behaves more like a small application than a short exercise. The main lesson is procedural design: break the workflow into named steps and guard each step before changing the machine state.

## 1. Representing Machine State with Dictionaries and Shared Variables

The machine data starts in `data.py` and `main.py`:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
```

`resources` stores the remaining ingredients, and `money` stores the profit. These values need to survive across multiple customer orders, which is why the program treats them as shared machine state rather than local variables inside one function.

That is a useful shift in thinking. The program is no longer solving one calculation and ending. It is modeling an object that changes over time.

## 2. Checking Resources Before Taking Payment

The main loop follows a sensible order of operations:

```python
elif order in ("espresso", "latte", "cappuccino"):
    drink = MENU[order]
    if check_resources(drink["ingredients"]):
        amount = insert_coins()
        if transaction_successful(amount, drink["cost"]):
            serve_coffee(drink["ingredients"], resources)
```

This is the right design because the machine should not ask for money if it cannot make the drink. `check_resources()` acts as the first gate. Only if the ingredients are available does the program move on to payment.

That pattern is worth remembering: validate first, then take action.

## 3. Separating Payment Logic from Serving Logic

The payment code lives in its own function:

```python
def transaction_successful(money_inserted, drink_price):
    if money_inserted >= drink_price:
        change = round(money_inserted - drink_price, 2)
        global money
        money += drink_price
        print(f"Here is ${change} in change.")
        return True
```

And the inventory update lives elsewhere:

```python
def serve_coffee(order_ingredients, inventory):
    for item in order_ingredients:
        inventory[item] -= order_ingredients[item]
```

This separation keeps the program easier to follow. Payment decides whether the order is allowed to proceed. Serving changes the machine inventory only after payment succeeds.

Even in procedural code, that kind of function boundary prevents unrelated logic from getting tangled together.

## 4. Supporting Operator Commands

The coffee machine also includes control commands:

```python
if order == "off":
    power_on = False
elif order == "report":
    print(report())
```

These are small, but they make the app feel more complete. `report` gives the operator a snapshot of the remaining resources, and `off` stops the machine loop entirely.

This is the kind of detail that moves a project from toy script toward simple application behavior.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Order `espresso`, `latte`, or `cappuccino`.
4. Use `report` to inspect the machine state and confirm that successful orders reduce ingredients and increase the stored money total.

## Summary

Day 15 teaches how to structure a small stateful application procedurally. The coffee machine stores shared resources, validates an order before accepting payment, updates profit and inventory in separate functions, and supports operator commands for reporting and shutdown. It is an important step toward application-style program design.

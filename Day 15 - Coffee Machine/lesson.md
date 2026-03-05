# Day 15 - Local Development Workflow and Procedural App Design
Day 15 is a procedural console application that combines inventory checks, payment flow, and command handling.

## Goal

Simulate a coffee machine that can:
- accept drink orders
- check available resources
- process coin input and payment
- update inventory and money balance
- print machine reports

## Day-Specific Logic

`main.py` breaks the process into focused functions:
- `check_resources()` for ingredient sufficiency
- `insert_coins()` for cash input
- `transaction_successful()` for payment validation/change
- `serve_coffee()` for inventory updates

`data.py` provides menu configuration and starting resources.

## Code Reference

From `main.py`:

```python
if order in ("espresso", "latte", "cappuccino"):
    drink = MENU[order]
    if check_resources(drink["ingredients"]):
        cls()
        amount = insert_coins()
        if transaction_successful(amount, drink["cost"]):
            serve_coffee(drink["ingredients"], resources)
            print(f"Here is your ☕{order}. Enjoy!")
```

## Run

```bash
python "main.py"
```

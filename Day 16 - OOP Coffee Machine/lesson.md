# Day 16 - Object-Oriented Programming Fundamentals

Yesterday, we built a Coffee Machine using procedural programming—lots of functions, dictionaries, and global variables. It worked, but keeping track of which function modified which dictionary got a little messy as the program grew.

Today, we are rebuilding that exact same Coffee Machine, but we're shifting our thinking to **Object-Oriented Programming (OOP)**. Instead of thinking about "functions" and "variables," we think about **Objects** that have their own data (**Attributes**) and their own capabilities (**Methods**).

## Blueprints and objects

In our procedural version, all the code lived in `main.py`. Today, look at the project files: we have `menu.py`, `coffee_maker.py`, and `money_machine.py`. Each of these files contains a **Class**. Think of a Class as a blueprint. It describes what an object will know and what it will do.

In `main.py`, the first thing we do is build our actual objects from those blueprints. This is the moment where the "blueprint" becomes a real, usable machine in our memory:

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()
```

Now, `coffee_machine` is a real, functional object. It internally keeps track of its own water, coffee, and milk. We don't have to manage a `resources` dictionary in our main file anymore!

## Calling methods on objects

In yesterday's version, when the user typed "report," we called a standalone `report()` function and passed around variables. Today, the `coffee_machine` object knows how to print its own report. We just ask it to do so using the dot notation (`object.method()`):

```python
if order == "report":
    coffee_machine.report()
    coin_machine.report()
```

We are commanding the objects to perform their built-in tasks. The `MoneyMachine` handles the cash report, and the `CoffeeMaker` handles the ingredient inventory.

## The logic flow in main.py

If a user orders a latte, look at how clean the code reads once the heavy lifting is moved into those classes:

```python
drink = drink_menu.find_drink(order)

if coffee_machine.is_resource_sufficient(drink):
    if coin_machine.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)
```

Notice the conversation happening here:
1. We ask the `drink_menu` object to find the specified drink. It hands us back a `MenuItem` object.
2. We ask the `coffee_machine` if it has enough resources for that specific `MenuItem`.
3. We ask the `coin_machine` to handle the payment. It prompts the user for coins, checks the total, and gives change.
4. If everything passes, we command the `coffee_machine` to actually brew the coffee.

## Why this shift matters

The `main.py` is now incredibly short—just 25 lines. All the complex, messy logic about counting coins or subtracting water amounts is hidden away inside the classes. As the programmer writing the main loop, you just plug the objects together and let them do all the work.

This is the power of OOP: it lets us build much larger, more complex systems without our "main" logic becoming an unreadable mess.

## Try it yourself

```bash
python "main.py"
```

Play with it just like yesterday. Functionally, it's identical to the user, but architecturally, it's totally different—and much more robust.

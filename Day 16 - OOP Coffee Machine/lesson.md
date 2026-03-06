# Day 16 - Object-Oriented Programming Fundamentals

Day 16 rebuilds the coffee machine from the previous lesson, but the architecture changes completely. Instead of keeping the whole workflow in one file with shared dictionaries and standalone functions, the program now creates objects that carry their own data and behavior. That shift is the real lesson: object-oriented programming is not about making code look fancier. It is about assigning responsibility to the right part of the program.

## 1. Moving from Procedures to Objects

The main file starts by creating the three objects the app needs:

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()
```

Each object represents a distinct responsibility:

- `Menu` knows which drinks exist
- `CoffeeMaker` knows the machine resources and brewing logic
- `MoneyMachine` knows how payment works

That division is the core OOP idea. Instead of one file managing everything directly, each object owns part of the system.

## 2. Calling Methods Instead of Passing Shared State Everywhere

When the user asks for a report, the program does not call one big helper function. It asks each object to report on itself:

```python
if order == "report":
    coffee_machine.report()
    coin_machine.report()
```

This is a cleaner interface than passing the resources dictionary and profit total into standalone functions. The object already has the state it needs, so the caller only needs to request the action.

That is an important design improvement from Day 15. The main loop no longer needs to know how reporting works internally.

## 3. Reading the Main Workflow Like a Conversation

The drink order flow is compact because each object does one job:

```python
drink = drink_menu.find_drink(order)

if coffee_machine.is_resource_sufficient(drink):
    if coin_machine.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)
```

This reads almost like a conversation:

1. get the requested drink from the menu
2. ask the coffee machine if it has enough ingredients
3. ask the money machine to handle payment
4. tell the coffee machine to brew the drink

That readability is one of the main practical benefits of OOP. Good object design keeps the top-level workflow short and expressive.

## 4. Why the Main File Gets Smaller as the System Gets Smarter

The strongest sign that the refactor worked is how little `main.py` needs to know. It does not calculate coin totals itself, subtract ingredients itself, or manage recipe details itself. Those rules live in the classes where they belong.

This is the key design takeaway from the day: as programs grow, the main file should describe orchestration, not every internal detail.

The old deleted `lesson.py` in git history only contained small `turtle` and `prettytable` experiments, so the current lesson source is the real teaching material here.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Order drinks, request a `report`, and compare the behavior to the procedural coffee machine from Day 15.
4. Notice that the user experience is similar even though the internal structure is now object-oriented.

## Summary

Day 16 introduces object-oriented design by rebuilding an existing app with classes. `Menu`, `CoffeeMaker`, and `MoneyMachine` each own part of the logic, which keeps `main.py` focused on orchestration instead of low-level details. The lesson is less about syntax and more about assigning responsibility to the right object.

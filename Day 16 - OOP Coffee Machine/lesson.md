# Day 16 - Object-Oriented Programming Fundamentals
Day 16 introduces OOP by moving from one-file procedural logic to collaborating classes with clear responsibilities.

## What You Learn

- Why classes are useful for organizing real programs.
- How objects collaborate (`Menu`, `CoffeeMaker`, `MoneyMachine`).
- How method calls replace long conditional/procedural blocks.

## Recovered Historical Notes (From Git)

The deleted `lesson.py` from this day included exploratory OOP practice and object usage examples:
- creating objects (`Turtle`, `PrettyTable`)
- calling object methods (`shape`, `color`, `add_column`)
- seeing how objects package both data and behavior

That historical context is important: Day 16 is where the course shifts from syntax exercises to **designing with objects**.

## Day-Specific Architecture

`main.py` does orchestration only. Core logic is delegated to classes in separate modules:

- `menu.py`
  - `MenuItem`: encapsulates one drink (ingredients + cost)
  - `Menu`: exposes available items and lookup by name
- `coffee_maker.py`
  - tracks machine resources
  - validates ingredient sufficiency
  - updates inventory after serving
- `money_machine.py`
  - processes coin input
  - verifies payment
  - computes change and tracks profit

This is the main OOP takeaway: each class owns one domain concern.

## Code Reference

From `main.py`:

```python
drink_menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()

while is_machine_on:
    order = input(f"What would you like? ({drink_menu.get_items()}): ")
    if order == "report":
        coffee_machine.report()
        coin_machine.report()
    elif order == "off":
        is_machine_on = False
    else:
        drink = drink_menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if coin_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
```

From recovered `lesson.py` history:

```python
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", column=["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", column=["Electric", "Water", "Fire"])
print(table)
```

## Run

```bash
python "main.py"
```

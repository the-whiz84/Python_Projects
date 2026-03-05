# Day 03 - Control Flow, Conditionals, and Logical Branching
Day 03 combines two conditional-logic projects: one numeric classifier and one branching story game.

## Goal

Build and understand two scripts:
1. `bmi_calculator.py` for BMI computation and category output.
2. `treasure_island.py` for a nested `if/elif/else` adventure game.

## Historical Lesson Direction

Recovered from the deleted Day 03 lesson notes in git history:
- Use conditionals to shape the full story path.
- Make user answers case-insensitive.
- Treat this as a "Choose Your Own Adventure" exercise where every branch matters.

## Day-Specific Logic

- **BMI calculator**: convert string input to numbers, compute `weight / (height ** 2)`, then classify by threshold.
- **Treasure Island**: normalize input with `.lower()` and branch in stages (`left/right`, then `boat/swim`, then door choice).

## Code References

From `bmi_calculator.py`:

```python
height = float(input("Please enter your height in m. (Eg. 1.85) m: "))
weight = float(input("Please enter your weight in kg: "))
bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
```

From `treasure_island.py`:

```python
decision1 = input("Which way do you go? Type 'left' or 'right': ").lower()

if decision1 == "left":
    decision2 = input("Type 'boat' or 'swim': ").lower()
    if decision2 == "boat":
        decision3 = input("Type 'red', 'yellow' or 'blue': ").lower()
```

## Run

```bash
python "bmi_calculator.py"
```

```bash
python "treasure_island.py"
```

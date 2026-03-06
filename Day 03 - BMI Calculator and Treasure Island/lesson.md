# Day 03 - Control Flow, Conditionals, and Logical Branching

Today we've got two projects: a BMI Calculator and a text-based adventure game called Treasure Island. Both are about the same core idea — making your program do different things depending on what the user tells it.

The BMI Calculator is a quick if/elif chain. Treasure Island takes it further with deeply nested decisions that create branching paths. By the end of this day, you'll be comfortable writing code that makes choices.

## BMI Calculator

This one lives in `bmi_calculator.py`. It asks for height and weight, does the math, and tells you which category you fall into.

```python
height = float(input("Please enter your height in m. (Eg. 1.85) m: "))
weight = float(input("Please enter your weight in kg: "))
bmi = round(weight / (height ** 2))
```

Notice that we're doing the type conversion right inside the `input()` call — wrapping it in `float()` immediately. That's cleaner than converting later.

The `**` operator is Python's exponent — `height ** 2` means "height squared." And `round()` gives us a clean whole number.

Then we use an **if/elif/else chain** to decide what message to print:

```python
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
```

The order matters here. Python checks each condition from top to bottom and runs the **first** one that's true. If you put `bmi < 30` before `bmi < 25`, a BMI of 22 would match `< 30` first and give the wrong category. When you're writing elif chains, always go from the most restrictive condition to the least.

## Treasure Island

`treasure_island.py` is a choose-your-own-adventure game. You make three decisions (left or right, boat or swim, which door), and each combination leads to a different outcome — most of them involve dying in creative ways.

The structure is **nested if/else blocks**:

```python
decision1 = input("Which way do you go? Type 'left' or 'right': ").lower()

if decision1 == "left":
    decision2 = input("... Type 'boat' or 'swim': ").lower()
    if decision2 == "boat":
        decision3 = input("... Type 'red', 'yellow' or 'blue': ").lower()
        if decision3 == "yellow":
            print("Congratulations, you found the treasure chest!")
        # ... other doors
    else:
        print("... alligators ... GAME OVER!")
else:
    print("... bear attack ... GAME OVER!")
```

Each `if` block opens up a new level of decision. The `.lower()` at the end of each `input()` call converts whatever the user types to lowercase — so "Left", "LEFT", and "left" all work. That's a good habit for any time you compare user input to a specific string.

The fun part here is the ASCII art — skulls, fire, treasure, and bears. It makes the terminal output feel like an actual game instead of a boring script.

## Try it yourself

```bash
python "bmi_calculator.py"
python "treasure_island.py"
```

For Treasure Island, try all the paths. There's only one way to win (left → boat → yellow), but the death scenes are worth seeing.

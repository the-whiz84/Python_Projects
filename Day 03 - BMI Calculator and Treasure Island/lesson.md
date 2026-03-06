# Day 03 - Control Flow, Conditionals, and Logical Branching

Day 03 pairs two projects that teach the same core skill from different angles. The BMI calculator is a short numeric example: calculate a value, then classify it with conditions. Treasure Island turns that same idea into a branching text adventure where each answer sends the player down a different path. Together they introduce control flow: code that does not always run the same way.

## 1. Using Conditions to Classify a Result

The BMI script starts by reading height and weight, then calculating body mass index:

```python
height = float(input("Please enter your height in m. (Eg. 1.85) m: "))
weight = float(input("Please enter your weight in kg: "))
bmi = round(weight / (height ** 2))
```

There are three useful ideas in that short block:

- `float()` converts user input into numbers you can divide
- `** 2` squares the height value
- `round()` keeps the result simple enough to classify cleanly

After the calculation, the script uses an `if` / `elif` / `else` chain:

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

The important lesson is that order matters. Python checks these conditions from top to bottom and stops at the first match. When you build a decision chain, you need to arrange the ranges so each value lands in the right branch.

## 2. Building Branching Paths in Treasure Island

`treasure_island.py` uses the same condition logic, but now the decisions are nested:

```python
decision1 = input("Which way do you go? Type 'left' or 'right': ").lower()

if decision1 == "left":
    decision2 = input("... Type 'boat' or 'swim': ").lower()
    if decision2 == "boat":
        decision3 = input("... Type 'red', 'yellow' or 'blue': ").lower()
        if decision3 == "yellow":
            print("Congratulations, you found the treasure chest!")
```

This structure creates a game tree. One answer opens the next question, and the wrong answer ends the game.

The `.lower()` call is doing practical work here. It normalizes user input so `"Left"` and `"LEFT"` are treated the same as `"left"`. That is a simple habit, but it makes command-line programs much more forgiving.

## 3. Control Flow Changes the User Experience

What makes Treasure Island more interesting than the BMI calculator is not new syntax. It is the way conditionals shape the experience:

- one branch continues the story
- another branch ends the game
- another branch reveals the winning path

That is the real jump on Day 03. Conditionals stop being only about math categories and start becoming a way to control narrative, state, and outcomes.

By the time you finish both files, you have already used the same tool for two different program styles: a calculator and a game.

## How to Run the Projects

1. Open a terminal in this folder.
2. Run the BMI calculator:

```bash
python bmi_calculator.py
```

3. Run the Treasure Island game:

```bash
python treasure_island.py
```

4. For Treasure Island, try multiple paths and confirm that different answers lead to different branches.

## Summary

Day 03 introduces control flow. In the BMI project, you use conditions to classify a number. In Treasure Island, you use nested conditions to build branching outcomes. The syntax is the same, but the second project shows how powerful even basic `if` statements become once they start shaping the full program flow.

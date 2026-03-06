# Day 02 - Data Types, Numbers, and Type Conversion

Today we're building a Tip Calculator. The program asks for a bill amount, a tip percentage, and the number of people splitting the cost. Then it calculates how much each person should pay. The calculation is simple, but the lesson introduces a bigger idea: user input arrives as text, so you need type conversion before Python can do any real math.

## 1. Why `input()` Is Not Enough on Its Own

The first lines of `main.py` collect all the data the program needs:

```python
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? €")
tip = input("How much tip would you like to give? 10, 12 or 15 percent? ")
people = input("How many people to split the bill? ")
```

At this point, all three variables are strings. That matters because `input()` always returns text, even when the user types something that looks like a number.

If you tried to divide `total_bill` by `people` immediately, Python would raise a `TypeError`. So this lesson is really about learning when to turn text into numbers.

## 2. Converting Strings into the Right Numeric Types

The calculation block shows the difference between integers and floating-point numbers:

```python
tip_amount = float(total_bill) * (int(tip) / 100)
bill_with_tip = float(total_bill) + float(tip_amount)
split_bill = float(bill_with_tip) / int(people)
```

There are two key choices here:

- `float()` is used for the bill because money can include decimals.
- `int()` is used for the tip percentage and number of people because those are whole numbers in this project.

That distinction is worth noticing early. Choosing the right data type makes the math easier to reason about and prevents bugs later when programs become more complex.

## 3. Formatting the Result for Real Users

Once the math is done, the program prints the final amount:

```python
print(f"Each person should pay: €{split_bill:.2f}")
```

This line introduces two useful ideas at once:

- an f-string lets you insert variables directly into a string
- `:.2f` formats the number to two decimal places

Without that formatting, Python might print something like `33.6` instead of `33.60`. For money, that difference matters. Even simple programs should present results in a way that matches how people expect to read them.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Enter a bill amount, a tip percentage, and the number of people.
4. Verify that the final output is rounded to two decimal places.

## Summary

Day 02 teaches the first real bridge between user input and computation. You collect text with `input()`, convert it into numbers with `int()` and `float()`, perform the tip calculation, and format the result with an f-string. That pattern shows up constantly in practical Python programs.

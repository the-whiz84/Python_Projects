# Day 02 - Data Types, Numbers, and Type Conversion

Today we're building a Tip Calculator — you enter the bill, pick a tip percentage, say how many people are splitting it, and the script tells everyone what they owe.

Simple idea, but this is where you first run into one of Python's quirks: `input()` always gives you a string, even when you type a number. So you have to learn how to convert between types to do any math at all.

## The project

Everything is in `main.py`. The flow goes like this:

1. Ask for the total bill.
2. Ask for the tip percentage (10, 12, or 15).
3. Ask how many people are splitting.
4. Calculate the tip, add it to the bill, divide by the number of people.
5. Print each person's share, formatted to two decimal places.

## Let's walk through the code

```python
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? €")
tip = input("How much tip would you like to give? 10, 12 or 15 percent? ")
people = input("How many people to split the bill? ")
```

Right off the bat — `total_bill`, `tip`, and `people` are all strings at this point. If you tried to do `total_bill / people` without converting, Python would throw a `TypeError`. That's the whole reason type conversion exists.

```python
tip_amount = float(total_bill) * (int(tip) / 100)
bill_with_tip = float(total_bill) + float(tip_amount)
split_bill = float(bill_with_tip) / int(people)

print(f"Each person should pay: €{split_bill:.2f}")
```

Here's what's happening with the conversions:

- **`float()`** turns a string into a decimal number. We use it for the bill because money has cents.
- **`int()`** turns a string into a whole number. Tip percentage and number of people don't need decimals.
- **`:.2f`** inside the f-string formats the final number to exactly two decimal places — so you get `€33.60` instead of `€33.6`.

The commented-out code at the bottom of the file shows an alternative approach where you convert the inputs right when you receive them. That's actually cleaner — you deal with the type conversion once and then forget about it. Both styles work, but converting early is the habit you'll want to build.

## Try it yourself

```bash
python "main.py"
```

Try a €150 bill, 12% tip, split 5 ways — you should get €33.60 per person.

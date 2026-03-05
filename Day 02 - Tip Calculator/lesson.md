# Day 02 - Data Types, Numbers, and Type Conversion
This lesson combines the original Day 02 instructions (recovered from git history) with the current `main.py` implementation.

## Goal

You build a CLI **Tip Calculator** that:
1. Reads total bill amount.
2. Reads tip percentage.
3. Reads number of people splitting the bill.
4. Computes and formats each person’s final payment to 2 decimal places.

Primary entrypoint: `main.py`.

## Original Requirement (From History)

- Example formula: `(bill / people) * 1.12` for a 12% tip.
- Output must always be formatted to 2 decimals.

## Implementation Notes

- Convert user input strings before arithmetic.
- Compute tip amount first, then total bill with tip, then split by people.
- Format output with `:.2f`.

1. Collect bill, tip percent, and people count from the terminal.
2. Convert inputs into numbers and calculate `tip_amount`.
3. Add tip to the bill to produce `bill_with_tip`.
4. Divide by people count and print the result with two decimals.

## Code Reference

Excerpt from `main.py`:
```python
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? €")
tip = input("How much tip would you like to give? 10, 12 or 15 percent? ")
people = input("How many people to split the bill? ")
tip_amount = float(total_bill) * (int(tip) / 100)

bill_with_tip = float(total_bill) + float(tip_amount)

split_bill = float(bill_with_tip) / int(people) 

print(f"Each person should pay: €{split_bill:.2f}")
```

## Run

```bash
python "main.py"
```

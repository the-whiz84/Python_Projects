# Day 05 - Loops and Iteration Patterns
Day 05 focuses on building structured output by iterating over multiple character groups and combining them safely.

## Goal

Generate a random password using user-defined counts for:
- letters
- symbols
- numbers

## Day-Specific Logic

`main.py` uses two approaches:
- **Easy level** (commented): append in predictable order.
- **Hard level** (active): collect characters in a list, shuffle, then join into final password.

This day is mainly about loop-based construction and controlled randomization.

## Code Reference

From `main.py`:

```python
password = []

for item in range(0, nr_letters):
    password.append(random.choice(letters))

for item in range(0, nr_symbols):
    password.append(random.choice(symbols))

for item in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

final_passwd = ""
for num in range(0, len(password)):
    final_passwd += password[num]
```

## Run

```bash
python "main.py"
```

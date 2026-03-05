# Day 01 - Working with Variables, Strings, and Input/Output
Day 01 is a pure input/output exercise: collect two strings and produce one formatted result.

## Goal

Build a CLI band name generator from two user prompts:
- city they grew up in
- first pet name

## How This Day Works

`band_name.py` does the whole flow in one place:
1. Print welcome text.
2. Read `CITY` and `PET` with `input()`.
3. Concatenate them into `BAND_NAME`.
4. Print the result.

## Code Reference

From `band_name.py`:

```python
print("Welcome to the Band Name Generator!\n")

CITY = input("What is the name of the city you grew in?\n")
PET = input("What is the name of your first pet?\n")

BAND_NAME = CITY + " " + PET
print("Your band name could be:\n" + BAND_NAME)
```

## Run

```bash
python "band_name.py"
```

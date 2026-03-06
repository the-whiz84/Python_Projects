# Day 01 - Working with Variables, Strings, and Input/Output

Today we're building a Band Name Generator: a tiny script that asks two questions and combines the answers into a simple result. It is small on purpose. On the first day, the goal is not complexity. The goal is to get comfortable with Python reading input, storing values, and printing output back to the terminal.

## 1. The Whole Program Fits in One Screen

The project lives in `band_name.py`, and the full script is short enough to read in one pass:

```python
print("Welcome to the Band Name Generator!\n")

CITY = input("What is the name of the city you grew in?\n")
PET = input("What is the name of your first pet?\n")

BAND_NAME = CITY + " " + PET
print("Your band name could be:\n" + BAND_NAME)
```

That compact size is useful for a first lesson. You can see the complete flow from top to bottom:

1. print a greeting
2. collect two pieces of user input
3. combine those strings
4. print the final result

There are no functions or imports yet. The point is to learn how Python executes statements in order.

## 2. Reading Input and Saving It in Variables

The two `input()` calls are the most important part of the lesson:

```python
CITY = input("What is the name of the city you grew in?\n")
PET = input("What is the name of your first pet?\n")
```

`input()` pauses the program and waits for the user to type. Whatever the user types comes back as a string. We then assign that string to a variable so the program can use it later.

This is your first exposure to a core programming pattern:

- ask for data
- store the data
- reuse the data later in the program

Without variables, the answers would disappear as soon as the user typed them. With variables, the program can remember those values and build something from them.

## 3. Building Output from Smaller Pieces

Once the city and pet name are stored, the script combines them into one new string:

```python
BAND_NAME = CITY + " " + PET
print("Your band name could be:\n" + BAND_NAME)
```

The `+` operator joins strings together. That process is called string concatenation. The extra `" "` in the middle matters because it inserts a space between the two words.

This is also a good place to notice `print()`. It sends text to the terminal, and `\n` adds a line break. Even in a simple script, formatting output clearly makes the program easier to read.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python band_name.py
```

3. Type a city name and a pet name when the prompts appear.
4. Check that the script prints a combined band name at the end.

## Summary

Day 01 teaches the basic input-output loop of a Python program. You print text, collect input, store it in variables, and combine strings into a final result. The script is tiny, but the pattern is foundational and shows up in almost every program you write later.

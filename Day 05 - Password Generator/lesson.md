# Day 05 - Loops and Iteration Patterns

Today we're building a password generator. The script asks how many letters, symbols, and numbers the user wants, then creates a random password from those character pools. It is a good first loop project because the same pattern repeats several times: do an action `n` times, collect the results, then turn those results into something useful.

## 1. Repeating Work with `for` Loops

The script starts by collecting the password requirements:

```python
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
```

Those values control how many times each loop should run. For example, the letters loop looks like this:

```python
for item in range(0, nr_letters):
    password.append(random.choice(letters))
```

This is the main loop idea of the day: `range(0, nr_letters)` creates the right number of iterations, and the loop body repeats the same action each time. Instead of writing ten separate lines to add ten characters, the loop handles the repetition for you.

## 2. Building the Password in Pieces

The stronger version of the project stores characters in a list:

```python
password = []

for item in range(0, nr_letters):
    password.append(random.choice(letters))

for item in range(0, nr_symbols):
    password.append(random.choice(symbols))

for item in range(0, nr_numbers):
    password.append(random.choice(numbers))
```

This design is better than building the final string immediately because the list is easy to shuffle and easy to inspect. Each call to `random.choice()` picks one character from the right source list, and `.append()` adds it to the growing password.

The code also includes an easier version in comments that builds the string directly. That version works, but it always places letters first, then symbols, then numbers. The order becomes predictable, which weakens the result.

## 3. Randomizing the Final Order

The hard version fixes that predictable structure with `random.shuffle()`:

```python
random.shuffle(password)

final_passwd = ""
for num in range(0, len(password)):
    final_passwd += password[num]
```

`random.shuffle()` rearranges the list in place. That is the key security improvement in the whole project. The password still contains the requested mix of characters, but the final order is no longer grouped by type.

The final loop joins the characters into a string one by one. Later you will learn faster ways to do this, such as `"".join(password)`, but the explicit loop is useful here because it makes the transformation easy to follow.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Enter the number of letters, symbols, and numbers you want.
4. Run the script a few times with the same inputs and confirm that the character counts stay consistent while the order changes.

## Summary

Day 05 teaches loops as a tool for controlled repetition. You use `for` loops to build a password piece by piece, store characters in a list, shuffle that list to remove predictable ordering, and then combine the result into the final string. It is a simple project, but it shows how iteration and randomness work together in real code.

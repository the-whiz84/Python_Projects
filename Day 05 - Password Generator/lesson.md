# Day 05 - Loops and Iteration Patterns

Today we're building a Password Generator. You tell it how many letters, symbols, and numbers you want, and it spits out a randomised password.

This is your first real encounter with **for loops** — repeating an action a specific number of times. We also see `random.choice()` for picking items from a list, and `random.shuffle()` for mixing things up. The project actually shows two approaches: an easy version and a hard version, and the difference between them teaches you something important about how order affects security.

## The project

Everything is in `main.py`. It starts by defining three character pools:

```python
letters = ['a', 'b', 'c', ..., 'X', 'Y', 'Z']
numbers = ['0', '1', '2', ..., '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
```

Then it asks how many of each you want:

```python
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
```

## Easy version vs hard version

The easy version (commented out in the code) builds the password by adding all the letters first, then all the symbols, then all the numbers:

```python
password = ""
for item in range(1, nr_letters + 1):
    password += random.choice(letters)
for item in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for item in range(1, nr_numbers + 1):
    password += random.choice(numbers)
```

This works, but the password always has a predictable structure — letters in front, symbols in the middle, numbers at the end. Not great for security.

The hard version fixes this by building a list first, then shuffling it:

```python
password = []

for item in range(0, nr_letters):
    password.append(random.choice(letters))
for item in range(0, nr_symbols):
    password.append(random.choice(symbols))
for item in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
```

**`random.shuffle()`** rearranges the list in place — it doesn't return a new list, it scrambles the one you give it. After shuffling, we join everything into a string:

```python
final_passwd = ""
for num in range(0, len(password)):
    final_passwd += password[num]
```

A quicker way to do this same thing is `"".join(password)`, but the loop version makes it clear what's happening — you're walking through the list one character at a time and gluing them together.

## The key loop concepts

- **`range(0, n)`** generates numbers from 0 to n-1. That's n iterations total.
- **`random.choice(some_list)`** picks a random item from a list.
- **`.append()`** adds an item to the end of a list.
- **`random.shuffle()`** scrambles a list in place — watch out, it doesn't return anything.

## Try it yourself

```bash
python "main.py"
```

Ask for 5 letters, 3 symbols, and 2 numbers. Run it a few times — you'll get a different result each time because of the randomisation and shuffling.

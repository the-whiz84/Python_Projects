# Day 01 - Working with Variables, Strings, and Input/Output

Today we're building a Band Name Generator — a tiny script that asks you two questions and mashes the answers together into a (sometimes hilarious) band name.

It's a simple project, but it covers three things you'll use in every single Python program: printing text to the screen, getting input from the user, and storing values in variables.

## The project

The entire program lives in `band_name.py`, and it's only about ten lines long. Here's the idea:

1. Greet the user.
2. Ask them what city they grew up in.
3. Ask them the name of their first pet.
4. Stick the two answers together and print it as their band name.

That's it. No imports, no classes, no functions — just raw Python basics.

## Let's walk through the code

```python
print("Welcome to the Band Name Generator!\n")

CITY = input("What is the name of the city you grew in?\n")
PET = input("What is the name of your first pet?\n")

BAND_NAME = CITY + " " + PET
print("Your band name could be:\n" + BAND_NAME)
```

A few things to notice:

- **`print()`** sends text to the terminal. The `\n` inside the string adds a line break — it's how you tell Python "go to the next line here."

- **`input()`** pauses the program and waits for the user to type something. Whatever they type gets returned as a string, and we save it into a variable (`CITY`, `PET`).

- **String concatenation** with `+` joins strings together. We add a space `" "` between the city and pet so the band name doesn't smash the words together like `"DallasRex"`.

- **Variable naming**: this script uses `UPPER_CASE` names. In Python, that convention usually signals a constant, but at this stage you're just getting a feel for giving your data a name. The important thing is that the name tells you what's inside.

## Try it yourself

```bash
python "band_name.py"
```

Run it a few times with different answers. You'll get results like "London Whiskers" or "Cairo Buddy" — the sillier the better.

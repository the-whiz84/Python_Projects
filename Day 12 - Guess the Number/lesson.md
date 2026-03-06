# Day 12 - Variable Scope and Number Guessing Logic

Today we're building a Number Guessing Game. The computer thinks of a number between 1 and 100, and you have to guess it. If you choose "easy" mode you get 10 tries; if you choose "hard" mode you get 5.

While you're building this, you're going to bump into a concept called **Variable Scope**. It determines where a variable can be seen and modified in your code, and it's one of the biggest sources of bugs for beginners.

## Local vs Global Scope

Look at how the chosen number is defined in `main.py`:

```python
chosen_number = random.randint(1, 100)

def check_number(guessed_number, lives):
    if guessed_number > chosen_number:
        print("Too high")
        # ...
```

`chosen_number` is sitting out in the open, outside of any functions. That makes it a **Global Variable**. Any function in the file can read it.

But look at `lives`:

```python
def check_number(guessed_number, lives):
    # ...
    elif guessed_number > chosen_number:
        print("Too high")
        return lives - 1
```

`lives` is passed in as a parameter. It is a **Local Variable**. It only exists inside `check_number()`. If you tried to `print(lives)` at the very bottom of the file outside the function, Python would crash with a `NameError`.

## Why returning is better than modifying globals

If `lives` is just a number that counts down, why don't we just make it a global variable and do `lives -= 1` inside the function?

You _can_ do that in Python (using the `global` keyword), but you really, really shouldn't. If you have five different functions all modifying the same global variable, tracking down bugs becomes a nightmare.

Instead, look at what we did:

```python
        return lives - 1
```

The function takes the current `lives`, subtracts 1, and **returns** the new number. Then, down in our game loop, we overwrite the old variable with the new returned value:

```python
    while turns_remaining > 0:
        player_guess = int(input("Guess the number: "))
        turns_remaining = check_number(player_guess, turns_remaining)
```

This pattern — pass a value in, get a modified value out, and save it — is much safer. The function isn't secretly messing with variables outside its walls. It's completely self-contained.

## Constants

At the bottom of the file (in the commented-out instructor solution), you might notice variables written in all caps:

```python
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
```

These are **Constants**. Python doesn't actually prevent you from changing them, but the all-caps naming is an agreement among programmers: "This value is set once and never changes." It's perfect for things like difficulty settings or the value of Pi.

## Try it yourself

```bash
python "main.py"
```

Try playing on hard mode. The `check_number` function will tell you if you're too high or too low, but with only 5 tries, you'll need to use binary search (always guessing the middle of the remaining range) to win consistently.

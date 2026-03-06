# Day 12 - Variable Scope and Number Guessing Logic

Today we're building a number guessing game. The computer chooses a number between `1` and `100`, the player selects a difficulty, and each guess reduces the remaining turns until the answer is found or the attempts run out. The project is a good setting for learning variable scope because the game needs both shared state and function-local state to work cleanly.

## 1. Understanding Which Variables Live Where

The chosen number is created outside the helper functions:

```python
chosen_number = random.randint(1, 100)
```

That makes it available to `check_number()` and `numbers_game()` without passing it around directly. In contrast, the remaining lives are managed as a parameter:

```python
def check_number(guessed_number, lives):
    elif guessed_number > chosen_number:
        print("Too high")
        return lives - 1
```

This is the key scope lesson:

- `chosen_number` is shared at the file level
- `lives` exists only inside the function call unless you pass it back out

Once you understand that boundary, it becomes much easier to predict how state moves through the program.

## 2. Returning Updated State Instead of Mutating It Everywhere

The best design choice in the project is that `check_number()` returns the new life count:

```python
return lives - 1
```

Then the caller stores that result:

```python
while turns_remaining > 0:
    player_guess = int(input("Guess the number: "))
    turns_remaining = check_number(player_guess, turns_remaining)
```

This pattern is safer than hiding the update inside a global variable. The function receives the current value, computes a new one, and hands it back. That makes the function easier to reason about because its effect is visible where it is called.

## 3. Using Difficulty to Control the Game Loop

The difficulty setting determines how many turns the player gets:

```python
difficulty = input("Choose your difficulty. Type 'normal' or 'hard': ")

if difficulty == "normal":
    turns_remaining = 10
elif difficulty == "hard":
    turns_remaining = 5
```

That value then controls the main guessing loop. This is a small but important design move: input from one part of the program changes the rules of the rest of the run.

The loop continues until the player either guesses correctly or uses every attempt:

```python
while turns_remaining > 0:
    player_guess = int(input("Guess the number: "))
    turns_remaining = check_number(player_guess, turns_remaining)
```

This ties together user input, comparison logic, and game state in a clean cycle.

## 4. Restarting the Game Cleanly

At the end, the script offers a replay option:

```python
play_again = input("Do you want to play again? Type 'y' or 'n': ")
if play_again == "y":
    clear()
    numbers_game()
```

Like Day 10, this uses a function call to restart the workflow. It is a simple approach, but it keeps the restart behavior contained inside the game function rather than scattering it across the file.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Choose `normal` or `hard`, then start guessing numbers from `1` to `100`.
4. Confirm that wrong guesses reduce the remaining turns and that the game ends when the answer is found or the attempts reach zero.

## Summary

Day 12 uses a guessing game to teach how state moves through functions. The chosen number is shared, the remaining lives are passed in and returned, and the difficulty setting controls the main loop length. It is a practical lesson in scope, return values, and keeping game logic predictable.

# Day 12 - Variable Scope and Number Guessing Logic
Day 12 focuses on state management across attempts, difficulty modes, and repeated game sessions.

## Goal

Build a number guessing game that:
- chooses a random number between 1 and 100
- supports difficulty levels with different attempt counts
- gives high/low feedback and tracks remaining turns
- allows replay

## Day-Specific Logic

`main.py` centralizes target-number checks in `check_number()` and controls round flow in `numbers_game()`.

Key state variables:
- `chosen_number` (random target)
- `turns_remaining` (attempt budget)
- `difficulty` (normal/hard)

## Code Reference

From `main.py`:

```python
def check_number(guessed_number, lives):
    if guessed_number > 100:
        print("Invalid option, try again")
        return lives
    elif guessed_number > chosen_number:
        print("Too high")
        return lives - 1
    elif guessed_number < chosen_number:
        print("Too low")
        return lives - 1
    elif guessed_number == chosen_number:
        print(f"You got it! The chosen number was {chosen_number}")
        return 0
```

## Run

```bash
python "main.py"
```

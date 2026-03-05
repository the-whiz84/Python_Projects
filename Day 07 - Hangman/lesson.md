# Day 07 - Hangman Logic and State Tracking
Day 07 is about managing game state across repeated guesses until a win or loss condition is reached.

## Goal

Build a terminal Hangman game with:
- random word selection
- live word progress display
- life tracking and game-over conditions

## Day-Specific Logic

`main.py` keeps three moving states in sync:
1. `display` list for guessed letters and underscores.
2. `lives` counter for incorrect guesses.
3. `end_of_game` flag to stop the loop when solved or failed.

The script also prevents repeated guesses and updates ASCII stages from `hangman_art.py`.

## Code Reference

From `main.py`:

```python
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You already guessed {guess}. Please choose another letter: ")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
```

## Run

```bash
python "main.py"
```

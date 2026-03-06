# Day 04 - Randomisation and Python Lists

Today we're building Rock Paper Scissors against the computer. The game is simple, but it introduces two important ideas that show up everywhere in Python: generating random values and storing related items in a list. This project is also useful because the folder contains two solutions, which makes it easier to compare a more repetitive style with a cleaner one.

## 1. Letting the Computer Make an Unpredictable Choice

The first version in `main.py` starts with the computer move:

```python
import random

player_choice = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
ai_choice = random.randint(0, 2)
```

`random.randint(0, 2)` returns a whole number between `0` and `2`, inclusive. That number becomes the computer's move.

That matters because the game now behaves differently every time you run it. Randomness is what turns a fixed script into something that feels interactive.

The rest of `main.py` uses `if` / `elif` chains to print the correct ASCII art for each move. It works, but it is repetitive. Repetition is usually the first sign that a better data structure might help.

## 2. Replacing Repetition with a List

The cleaner version in `rps.py` stores the hand shapes in a list:

```python
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3 or player_choice < 0:
    print("You chose an invalid option, please try again!")
else:
    print(game_images[player_choice])
    ai_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[ai_choice])
```

This is the big idea of the day: a list lets you use a numeric index to fetch the right item. `game_images[0]` is rock, `game_images[1]` is paper, and `game_images[2]` is scissors. Instead of writing separate branches for each display case, the program can look up the correct artwork directly.

The validation check matters too. If the user types a number outside the valid range, Python would raise an `IndexError` when trying to access the list. Guarding against bad input is already becoming part of writing stable programs.

## 3. Handling the Game Rules in the Right Order

Once both moves exist, the program decides the winner:

```python
if player_choice == ai_choice:
    print("It's a draw, try again!")
elif player_choice == 0 and ai_choice == 2:
    print("You win!")
elif player_choice == 2 and ai_choice == 0:
    print("You lose!")
elif player_choice < ai_choice:
    print("You lose!")
else:
    print("You win!")
```

The wrap-around cases come first because they break the simple numeric ordering:

- rock (`0`) beats scissors (`2`)
- scissors (`2`) loses to rock (`0`)

If you skipped those special cases and only relied on `<`, the logic would be wrong at the edges. This is a useful lesson beyond games: when your data has an exception to the general rule, handle that exception explicitly.

## How to Run the Projects

1. Open a terminal in this folder.
2. Run the first version:

```bash
python main.py
```

3. Run the list-based version:

```bash
python rps.py
```

4. Try a few valid moves and one invalid move to confirm the input check works.

## Summary

Day 04 introduces randomisation and lists through a small game. `random.randint()` gives the computer an unpredictable move, and the list-based version shows how indexing can replace repetitive condition chains. By comparing the two files, you can already see how better data structures lead to cleaner code.

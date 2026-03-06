# Day 04 - Randomisation and Python Lists

Today we're building Rock Paper Scissors against the computer. You pick a move, the computer picks a random one, and the code figures out who wins.

This is where you get introduced to two important tools: **lists** (storing multiple things in one variable) and **randomisation** (making the computer pick something unpredictable). You'll also see two different ways to solve the same problem — one verbose, one clean — and understand why lists make your code so much better.

## The project

There are two files here: `main.py` and `rps.py`. Both do the same thing — Rock Paper Scissors — but they approach it differently.

`main.py` maps each choice using if/elif blocks. `rps.py` puts the three hand gestures into a list and uses the player's number directly as an index. Let's look at both.

## The if/elif approach (`main.py`)

```python
import random

player_choice = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
ai_choice = random.randint(0, 2)
```

`random.randint(0, 2)` picks a random integer between 0 and 2 (inclusive). That's our computer opponent.

Then the code uses separate if/elif chains to convert the number into ASCII art — one chain for the player, another for the computer. It works, but it's repetitive. If you had 10 options instead of 3, you'd need 10 elif branches for each side.

## The list approach (`rps.py`)

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

This is the big idea: **a list lets you use a number to grab the right item**. `game_images[0]` is rock, `game_images[1]` is paper, `game_images[2]` is scissors. No if/elif needed — the player's input _is_ the index.

The validation check `player_choice >= 3 or player_choice < 0` catches bad input before we try to use it as an index. Without it, typing `5` would crash the program with an `IndexError`.

## Deciding the winner

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

The win logic handles the wrap-around cases first (rock beats scissors, scissors lose to rock), then uses a simple comparison for everything else. The order of these checks matters — if you don't handle the wrap-arounds first, the `<` comparison would give wrong results for those edge cases.

## Try it yourself

```bash
python "main.py"
python "rps.py"
```

Play a few rounds. Compare the two approaches — you'll see why `rps.py` is cleaner and why lists are one of the most useful things in Python.

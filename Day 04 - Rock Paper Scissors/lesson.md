# Day 04 - Randomisation and Python Lists
Day 04 introduces random computer choices and decision mapping using indexed options.

## Goal

Build a playable Rock-Paper-Scissors CLI game where:
- player picks `0`, `1`, or `2`
- computer picks randomly
- winner is determined with branch logic

## Historical Lesson Direction

Recovered from deleted Day 04 notes in git history:
- store user choice cleanly
- generate random computer choice
- compare both choices and return win/lose/draw feedback

## Day-Specific Logic

`main.py` keeps all game assets and logic together:
1. ASCII art strings for rock, paper, scissors.
2. `random.randint(0, 2)` for computer move.
3. Choice-to-art mapping via `if/elif`.
4. Special-case winner conditions (`0 vs 2`, `2 vs 0`) plus normal comparisons.

## Code Reference

From `main.py`:

```python
player_choice = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissors: "))
ai_choice = random.randint(0, 2)

if player_choice == 0 and ai_choice == 2:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nYou win!")
elif player_choice == 2 and ai_choice == 0:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nComputer wins!")
elif player_choice > ai_choice:
    print(f"You chose: {player_response}\nComputer draws: {ai_response}\nYou win!")
```

## Run

```bash
python "main.py"
```

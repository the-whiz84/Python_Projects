# Day 14 - Algorithmic Comparison and Game Rounds
Day 14 teaches repeated comparison logic using random candidates, score persistence, and round-based elimination.

## Goal

Build a Higher-Lower game where players guess which profile has more followers.

## Day-Specific Logic

`main.py` runs a loop that:
1. Picks two distinct entries from `game_data`.
2. Displays profile summaries (without follower counts).
3. Compares player guess (`A`/`B`) against hidden follower counts.
4. Increments score on correct guess and ends game on wrong answer.

The script keeps continuity by carrying the winning option forward to the next round.

## Code Reference

From `main.py`:

```python
selection1 = random.choice(data)

while not game_over:
    selection2 = random.choice(data)
    while selection1 == selection2:
        selection2 = random.choice(data)

    followers_a = int(selection1['follower_count'])
    followers_b = int(selection2['follower_count'])

    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if player_choice == "a" and followers_a > followers_b:
        score += 1
    elif player_choice == "b" and followers_b > followers_a:
        score += 1
        selection1 = selection2
    else:
        game_over = True
```

## Run

```bash
python "main.py"
```

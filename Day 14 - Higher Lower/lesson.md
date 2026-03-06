# Day 14 - Algorithmic Comparison and Game Rounds

Today we're building Higher Lower. The player sees two accounts, guesses which one has more followers, and keeps going until a guess is wrong. The project is a good lesson in round-based state because one choice survives into the next round while the other is replaced.

## 1. Working with a List of Dictionaries

The source data comes from `game_data.py`, where each entry looks like this:

```python
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
```

Each item is a dictionary, and all of them live inside one list. That means the game can pick a random account like this:

```python
selection1 = random.choice(data)
selection2 = random.choice(data)
```

Once a dictionary is selected, the program pulls out the pieces it needs for display and comparison. This is a useful structure because each record keeps related fields together instead of spreading them across multiple lists.

## 2. Separating Display Data from Comparison Data

The program prepares a readable version of each choice:

```python
compare_a = [selection1[key] for key in ('name', 'description', 'country')]
compare_b = [selection2[key] for key in ("name", "description", "country")]
followers_a = int(selection1['follower_count'])
followers_b = int(selection2['follower_count'])
```

This is a nice design step. The game uses one set of values for printing and another for the actual comparison. That keeps the output friendly while still preserving the numeric field needed to decide the winner.

It also reinforces an important lesson: the data you show to users is not always the same as the data you compute with.

## 3. Carrying the Winner into the Next Round

The most important game mechanic is how the next round is built:

```python
selection1 = random.choice(data)

while not game_over:
    selection2 = random.choice(data)
    while selection1 == selection2:
        selection2 = random.choice(data)
```

Then, when the player guesses correctly and `B` has more followers, the script does this:

```python
selection1 = selection2
```

That single assignment is what makes the game feel continuous. Instead of throwing both choices away, the winning account becomes the next `A` entry. The loop then pulls in only one fresh challenger.

This is the main state-management idea of the project: one variable persists across rounds and changes only when the game rules say it should.

## 4. Ending the Game on a Wrong Guess

The comparison logic controls the score and stop condition:

```python
if player_choice == "a" and followers_a > followers_b:
    score += 1
elif player_choice == "b" and followers_b > followers_a:
    score += 1
    selection1 = selection2
else:
    print(f"Sorry, that's wrong! Final score: {score}")
    game_over = True
```

This keeps the round logic simple:

- correct guess: score increases
- wrong guess: game ends

That clarity is what makes the loop easy to follow even though the game is effectively running the same structure again and again.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Compare the two presented accounts and type `A` or `B`.
4. Confirm that correct guesses increase the score and that one account carries forward into the next round.

## Summary

Day 14 uses a simple comparison game to teach how state survives across rounds. You pull structured records from a list of dictionaries, separate display values from numeric comparisons, and carry the current winner into the next round. The game feels dynamic because the loop preserves just enough state from one turn to the next.

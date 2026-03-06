# Day 14 - Algorithmic Comparison and Game Rounds

Today we're building Higher Lower. The game shows you two Instagram accounts and asks who has more followers. If you guess right, your score goes up, the second account becomes the first account, and a new challenger appears.

This project is all about managing state across multiple rounds of a game. We'll be working heavily with a list of dictionaries (the `data` list from `game_data.py`) and passing variables forward through a `while` loop.

## Working with lists of dictionaries

Inside `game_data.py`, we have a massive list full of dictionaries that look like this:

```python
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
```

To pick an account for the game, we use `random.choice(data)`. This grabs one entire dictionary out of the list.

```python
selection1 = random.choice(data)
```

Now `selection1` holds the Instagram dictionary. To get specific pieces out of it, we use the dictionary keys. Notice how we use a list comprehension in `main.py` just to grab the nice, printable parts for the user:

```python
compare_a = [selection1[key] for key in ('name', 'description', 'country')]
print(f"Compare A: {compare_a[0]}, a {compare_a[1]} from {compare_a[2]}")
```

And we grab the actual follower count as an integer so we can do math with it:

```python
followers_a = int(selection1['follower_count'])
```

## The Game Loop and Swapping State

Here is the trickiest part of the logic: when the player wins a round, the account from spot "B" slides over into spot "A" for the next round.

To make this work, we generate `selection1` _before_ the while loop starts. Then, inside the loop, we generate `selection2`.

```python
selection1 = random.choice(data)

while not game_over:
    selection2 = random.choice(data)

    # Make sure we didn't randomly pick the exact same account twice
    while selection1 == selection2:
        selection2 = random.choice(data)
```

If the user guesses correctly, they get a point. But here's the magic line:

```python
    elif player_choice == "b" and followers_b > followers_a:
        score += 1
        print(f"You are correct! Current score: {score}")
        selection1 = selection2
```

`selection1 = selection2`.

That one line takes the winner (which was in slot B) and makes it slot A. When the while loop circles back to the top, it generates a brand new `selection2`. This is how you create a continuous chain of rounds without writing the same code over and over again.

## Try it yourself

```bash
python "main.py"
```

Play a few rounds. Notice how the screen clears out the old text after every guess so the terminal doesn't fill up with endless scrolling text.

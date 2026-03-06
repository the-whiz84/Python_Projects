# Day 11 - Blackjack Capstone and Multi-Function Program Design

Today is our first Capstone Project: Blackjack (also known as 21).

Until now, we've mostly written code top-to-bottom, maybe with one or two functions. But Blackjack is too complex to write entirely in one giant loop. You have deck management, score calculation (with tricky Ace rules), win/loss comparison, and the dealer's automatic turns.

To handle that complexity, we break the game down into small, single-purpose functions.

## Breaking the problem down

If you look at `main.py`, you'll see the logic is split into distinct pieces:

1. **`deal_card()`**: Its only job is to pick a random card from the deck and hand it back.
2. **`calculate_score(card_list)`**: It looks at a hand of cards, adds them up, and handles special rules.
3. **`compare(u_score, c_score)`**: It purely looks at two numbers and returns a string saying who won.
4. **`play_game()`**: The orchestrator. It calls the other functions to actually run the game.

By isolating these jobs, we make the code way easier to test and fix when things break.

## The tricky part: Scoring the Ace

In Blackjack, an Ace is worth 11, unless adding 11 would bust your hand — then it's worth 1. Also, a two-card 21 (an Ace and a 10) is a "Blackjack" and wins instantly.

Here's how we handle that in `calculate_score`:

```python
score = sum(card_list)

# Check for a natural Blackjack
if score == 21 and len(card_list) == 2:
    return 0  # We use 0 as a special flag for Blackjack

# Handle the Ace rule
if score > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
```

First, we check for a natural Blackjack using `score == 21 and len(card_list) == 2`. We `return 0` instead of 21, which acts as a secret signal to the rest of our code that a natural Blackjack occurred.

Then, we handle the Ace. If the hand is over 21 _and_ there's an `11` in the list, we physically remove the `11` and swap it for a `1`.

## The Dealer's turn

When the player is done hitting, the dealer (computer) has to take its turn. House rules say the dealer must keep hitting until their score is 17 or higher. We use a simple while loop for this:

```python
while pc_score != 0 and pc_score < 17:
    pc_hand.append(deal_card())
    pc_score = calculate_score(pc_hand)
```

The dealer keeps drawing cards, and we keep recalculating their score, right up until they hit 17 or bust.

## Try it yourself

```bash
python "main.py"
```

Play a few hands. Watch how the game asks you to hit or stand, and notice how the dealer's logic automatically kicks in as soon as you stop drawing.

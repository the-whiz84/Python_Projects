# Day 11 - Blackjack Capstone and Multi-Function Program Design

Day 11 is the first capstone project, and the scale changes immediately. Blackjack has enough moving parts that a single top-to-bottom script would become hard to read and harder to debug. The lesson is not only about card rules. It is about splitting a larger problem into functions that each handle one clear responsibility.

## 1. Breaking the Game into Focused Functions

`main.py` organizes the game around four helper functions:

```python
def deal_card():
    """Returns a random card from the deck."""

def calculate_score(card_list):
    """Takes a list of cards and returns the score calculated."""

def compare(u_score, c_score):
    """Get the score of user and computer and return the winner"""

def play_game():
```

This structure matters because each function solves a different part of the program:

- `deal_card()` handles card selection
- `calculate_score()` knows the scoring rules
- `compare()` decides the final outcome
- `play_game()` runs the turn-by-turn flow

That separation is what makes the project manageable. Larger programs stay readable when each function has one job.

## 2. Encoding Blackjack Rules in `calculate_score()`

The scoring function handles the two trickiest Blackjack rules:

```python
score = sum(card_list)
if score == 21 and len(card_list) == 2:
    return 0

if score > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
```

The first rule is a natural Blackjack. Instead of returning `21`, the function returns `0` as a special signal value. That lets the rest of the game detect Blackjack quickly.

The second rule handles aces. If the hand would bust and contains an `11`, the code converts one ace from `11` to `1`. This is a good example of translating a real game rule into state changes inside the data structure.

## 3. Managing the Player and Dealer Turns

The player turn happens inside a loop:

```python
while not end_game:
    user_score = calculate_score(user_hand)
    pc_score = calculate_score(pc_hand)

    if pc_score == 0 or user_score == 0 or user_score > 21:
        end_game = True
    else:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
```

This section keeps recalculating the scores after each move. That repeated recalculation is important because the state changes every time a card is drawn.

After the player stops, the dealer follows house rules:

```python
while pc_score != 0 and pc_score < 17:
    pc_hand.append(deal_card())
    pc_score = calculate_score(pc_hand)
```

The dealer logic is automatic and deterministic. That creates a useful contrast: the player chooses, but the dealer follows strict rules.

## 4. Using a Comparison Function to Keep Endgame Logic Clean

At the end, the script calls `compare()`:

```python
print(compare(user_score, pc_score))
```

That is cleaner than mixing all the win-loss rules into `play_game()`. The comparison function becomes a dedicated decision layer for the final result.

This is one of the main design lessons of the capstone: once a program has enough branches and edge cases, moving decision logic into named functions makes the main workflow much easier to follow.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Start a game, choose whether to draw or pass, and watch how the dealer keeps drawing until the score reaches at least `17`.
4. Play a few rounds to confirm that Blackjack, busts, and ace conversion all behave correctly.

## Summary

Day 11 is the first project that really benefits from function design. Blackjack splits the logic into card dealing, scoring, comparison, and game flow, which keeps the code understandable even as the rules become more complex. The capstone teaches both game logic and program structure at the same time.

# Day 11 - Blackjack Capstone and Multi-Function Program Design
Day 11 combines multiple helper functions into a full game loop with score rules and dealer behavior.

## Goal

Implement a terminal Blackjack game with:
- random card dealing
- score calculation (including ace conversion)
- user hit/stand choices
- dealer draw-until-17 logic
- final winner comparison

## Day-Specific Logic

`main.py` separates game responsibilities into reusable functions:
- `deal_card()` for random draws
- `calculate_score()` for blackjack/ace handling
- `compare()` for winner resolution
- `play_game()` for one complete round

The program loops rounds using `while input(...) == "y"`.

## Code Reference

From `main.py`:

```python
def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)

    return score

while pc_score != 0 and pc_score < 17:
    pc_hand.append(deal_card())
    pc_score = calculate_score(pc_hand)
```

## Run

```bash
python "main.py"
```

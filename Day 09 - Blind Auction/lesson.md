# Day 09 - Dictionaries, Nesting, and Data Modeling

Today we're building a secret auction program. Each bidder enters a name and a bid, the screen clears between turns, and the program announces the winner at the end. The main lesson is data modeling: choosing the right structure to represent the relationship between a person and their bid.

## 1. Why a Dictionary Fits This Problem

The program stores bids in a dictionary:

```python
bid_list = {}

while add_user == True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid amount?\n$"))
    bid_list[name] = bid
```

This is the correct structure because each bidder name maps directly to one value. A dictionary is built for exactly that pattern: key to value.

In this project:

- the key is the bidder's name
- the value is the bid amount

If you tried to solve this with separate lists for names and bids, you would have to keep those lists perfectly aligned. A dictionary removes that bookkeeping and makes the relationship explicit.

## 2. Collecting Entries Until the Auction Ends

The auction continues inside a `while` loop:

```python
check = input("Do you want to add other bidders? Type 'yes' or 'no'\n").lower()
if check == "yes":
    clear()
else:
    add_user = False
    clear()
```

This structure lets the program keep accepting new entries until the operator decides to stop. The `clear()` call is also part of the lesson. It is not just cosmetic. In a blind auction, the next bidder should not see the previous bid, so the terminal is cleared after each turn.

That is a good reminder that some code exists to support the workflow, not only the calculation.

## 3. Finding the Highest Bidder from the Dictionary

At the end, the script computes the winner:

```python
highest_bid = max(bid_list, key=bid_list.get)
winning_bid = bid_list[highest_bid]
print(f"The winner with the highest bid is {highest_bid} with a bid of {winning_bid}!")
```

This line is worth understanding carefully. `max()` usually returns the largest item from a sequence. When you give it a dictionary, it normally looks at keys. But `key=bid_list.get` changes the comparison so `max()` evaluates each name by its stored bid amount instead.

So the program asks: which key has the highest associated value? That is a neat example of using a built-in function with a custom rule.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Enter multiple bidders and different bid amounts.
4. Confirm that the screen clears between bidders and that the final winner matches the highest bid entered.

## Summary

Day 09 introduces dictionaries as a way to model linked data cleanly. The program maps names to bids, uses a loop to keep collecting entries, and applies `max(..., key=bid_list.get)` to recover the winning bidder. It is a small project, but it teaches an important habit: choose the data structure that matches the relationship in the problem.

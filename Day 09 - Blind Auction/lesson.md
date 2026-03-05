# Day 09 - Dictionaries, Nesting, and Data Modeling
Day 09 introduces dictionary-based state management by storing and comparing bidder data.

## Goal

Build a secret auction CLI where multiple bidders can submit bids and the script reveals only the highest bidder at the end.

## Day-Specific Logic

`main.py` models bids with a dictionary:
- key: bidder name
- value: bid amount

During input rounds, each new bid overwrites or adds by bidder name. After collection finishes, winner selection is done with `max(..., key=bid_list.get)`.

## Code Reference

From `main.py`:

```python
bid_list = {}

while add_user == True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid amount?\n$"))
    bid_list[name] = bid
    check = input("Do you want to add other bidders? Type 'yes' or 'no'\n").lower()

highest_bid = max(bid_list, key=bid_list.get)
winning_bid = bid_list[highest_bid]
print(f"The winner with the highest bid is {highest_bid} with a bid of {winning_bid}!")
```

## Run

```bash
python "main.py"
```

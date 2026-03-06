# Day 09 - Dictionaries, Nesting, and Data Modeling

Today we're building a Secret Auction program. If you've ever been to a silent auction, you know how it works: people write down their names and bids, and at the very end, we find out who bid the highest.

To build this, we need a way to link a person's name directly to their bid. A list won't work well for this — we'd have to keep a list of names and a list of bids and try to keep them perfectly synced up. Instead, we're going to use a **dictionary**.

## How Dictionaries Work

Dictionaries in Python are just like real dictionaries. You have a "word" (the **key**), and you look it up to find the "definition" (the **value**).

In our project, the key is the bidder's name, and the value is their bid amount.

```python
bid_list = {}

while add_user == True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid amount?\n$"))

    bid_list[name] = bid
```

That line `bid_list[name] = bid` is the magic. It says: "Go into the `bid_list` dictionary. Find the page for this `name`, and write down this `bid`."

If the dictionary was empty, it adds a new entry. If that person already existed, it overwrites their old bid with the new one. So at the end of the loop, our dictionary looks something like this behind the scenes:

```python
{"Alice": 150, "Bob": 100, "Charlie": 200}
```

## Finding the highest bidder

After everyone has entered their bids (and we've cleared the screen between each person so nobody can cheat), we need to find the winner.

```python
highest_bid = max(bid_list, key=bid_list.get)
winning_bid = bid_list[highest_bid]

print(f"The winner with the highest bid is {highest_bid} with a bid of {winning_bid}!")
```

Normally, `max()` just looks for the highest number in a list. But when you give it a dictionary, it doesn't know what to look at — the keys (the names) or the values (the bids).

By passing `key=bid_list.get`, we're telling `max()`: "Please look at the _values_ to figure out the highest number, but tell me which _key_ it belongs to." So it finds that 200 is the highest bid, and returns `"Charlie"`.

Once we have `"Charlie"` saved in `highest_bid`, we can look up his actual bid amount by doing `bid_list[highest_bid]`.

## Try it yourself

```bash
python "main.py"
```

Add a few users with different bids. The screen clears after each entry to keep it a secret. Try putting in the exact same name twice — notice how the second bid overwrites the first one because dictionary keys must be unique!

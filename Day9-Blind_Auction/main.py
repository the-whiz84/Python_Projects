import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction")
add_user = True
bid_list = {}

while add_user == True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid amount?\n$"))
    bid_list[name] = bid
    check = input("Do you want to add other bidders? Type 'yes' or 'no'\n").lower()
    if check == "yes":
        clear()
    else:
        add_user = False
        clear()

highest_bid = max(bid_list, key=bid_list.get)
winning_bid = bid_list[highest_bid]
print(f"The winner with the highest bid is {highest_bid} with a bid of {winning_bid}!")




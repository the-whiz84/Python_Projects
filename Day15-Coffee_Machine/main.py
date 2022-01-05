import os
from data import LOGO, MENU, resources


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# now, to clear the screen
# cls()

money = 0

def report():
    """Prints a report of the available resources in the coffee machine"""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: €{money}")


def check_resources(order_ingredients):
    """Checks if there are suficient resources for the selected drink and returns True if enough
    resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def insert_coins():
    """Returns the total value of the amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many coins of 1 Euro?: ")) * 1
    total += int(input("How many coins of 50 cents?: ")) * 0.5
    total += int(input("How many coins of 20 cents?: ")) * 0.2
    total += int(input("How many coins of 10 cents?: ")) * 0.1
    return total


def is_transaction_succesful(coins_inserted, drink):
    """Checks if enough money was inserted and returns True, provides change and adds the money
    to the resources"""
    global money
    coins_needed = float(drink["cost"])
    if coins_inserted < coins_needed:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins_inserted == coins_needed:
        money += coins_inserted
        return True
    else:
        change = coins_inserted - coins_needed
        money += coins_inserted - change
        print(f"Here is your change: €{change:.2f}")
        return True

def serve_coffee(order_ingredients, inventory):
    """Subtracts the drink resources from the total inventory"""
    for item in order_ingredients:
        inventory[item] -= order_ingredients[item]


power_on = True


while power_on:
    print(LOGO)
    print("What would you like?\nEspresso is €1.00\nLatte is €1.50\nCappuccino is €2.00")
    order = input("Type your coffee choice: ").lower()
    if order == "off":
        power_on = False
    elif order == "report":
        print(report())
    elif order in ("espresso", "latte", "cappuccino"):
    # elif order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            cls()
            amount = insert_coins()
            if is_transaction_succesful(amount, drink):
                serve_coffee(drink["ingredients"], resources)
                print(f"Here is your ☕{order}. Enjoy!")
    else:
        print("Invalid selection. Please try again!")

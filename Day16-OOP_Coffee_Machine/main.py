import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import LOGO


coffee_menu = Menu()
coffee_machine = CoffeeMaker()
coffee_atm = MoneyMachine()


def clear():
    os.system('clear' if os.name == 'nt' else 'clear')


power_on = True


while power_on:
    print(LOGO)
    order = input(f"What would you like? Select from {coffee_menu.get_items()}: ").lower()
    if order == "report":
        clear()
        coffee_machine.report()
        coffee_atm.report()
    elif order == "off":
        print("Powering off")
        power_on = False    
    elif order in ("latte", "espresso", "cappuccino"):
        drink = coffee_menu.find_drink(order)
        drink_name = (drink.name).title()
        print(f"{drink_name} is €{drink.cost}")
        if coffee_machine.is_resource_sufficient(drink) and coffee_atm.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
        else:
            power_on = False
            print("Please contact the vendor to refill the machine.")
    else:
        clear()
        drink = coffee_menu.find_drink(order)

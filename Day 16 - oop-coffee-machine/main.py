from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:

    order = input(f"What would you like? ({drink_menu.get_items()}): ")
    if order == "report":
        coffee_machine.report()
        coin_machine.report()
    elif order == "off":
        print("Machine turning off.")
        is_machine_on = False
    else:
        drink = drink_menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if coin_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

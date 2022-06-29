from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_card = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
not_turn_off = 'n'
while not_turn_off != 'y':
    print("The list of items available to order: ", menu_card.get_items())
    order = input("Please enter your choice of order ").lower()
    item = menu_card.find_drink(order)
    print(item, item.cost)
    if item is not None:
        if coffee_machine.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                coffee_machine.make_coffee(item)
                coffee_machine.report()
                money.report()
    not_turn_off = input("input 'y' to turn off and 'n' to continue: ").lower()

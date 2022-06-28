from art import logo
from resources import MENU, resources


def not_enough_resources(order_no):
    """ check the resources to make coffee; takes the order no"""
    if order_no == 1:
        if resources['water'] < 50 or resources['coffee'] < 18:
            return True
    elif order_no == 2:
        if resources['water'] < 200 or resources['milk'] < 150 or  resources['coffee'] < 24:
            return True
    else:
        if resources['water'] < 250 or resources['milk'] < 100 or resources['coffee'] < 24:
            return True
        if MENU[order_no - 1]['ingredients']['water'] < 250 or MENU[order_no - 1]['ingredients']['milk'] < 100 or MENU[order_no - 1]['ingredients']['coffee'] < 24:
            return True
    return False


def not_enough_cash(order_no):
    """ Checking the cash for sufficient payment for the order; takes order no"""
    penny, nickel, dime, quarter = 0.0, 0.0, 0.0, 0.0
    amount_payed, change = 0, 0.0

    penny = 0.01 * int(input("Enter the number of pennies: "))
    nickel = 0.05 * int(input("Enter the number of nickels: "))
    dime = 0.10 * int(input("Enter the number of dime: "))
    quarter = 0.25 * int(input("Enter the number of quarter: "))

    amount_payed = penny + nickel + dime + quarter

    if amount_payed >= MENU[order_no-1]['cost']:
        change = amount_payed - MENU[order_no-1]['cost']
        print(f"Order Received\t The change amount is ${change}")
        return False
    return True


def report():
    print("The available resources are: ")
    print(f"Water: {resources['water']}, Milk: {resources['milk']}, Coffee: {resources['coffee']}")


print(logo)
run = 'on'

while run != 'off':
    order = int(input("Enter 1. Expresso\t2.Latte\t3.Cappuccino"))
    if not_enough_resources(order):
        print("Sorry! Not enough resources to make coffee")
        run = 'off'
    elif not_enough_cash(order):
        print("Amount Insufficient! Please pay sufficient amount")
    else:
        resources['water'] = resources['water'] - MENU[order - 1]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[order - 1]['ingredients']['coffee']
        if order != 1:
            resources['milk'] = resources['milk'] - MENU[order - 1]['ingredients']['milk']
        print('Order Served!☕️')
        run = input("Enter 'off' to stop the machine or 'report' to see the resources: ")
        if run == 'report':
            report()



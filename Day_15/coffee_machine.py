from art import logo
from resources import MENU, resources

orders = ['espresso', 'latte', 'cappuccino']


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
    return False


def not_enough_cash(order_name):
    """ Checking the cash for sufficient payment for the order; takes order no"""
    penny, nickel, dime, quarter = 0.0, 0.0, 0.0, 0.0
    amount_payed, change = 0.0, 0.0

    penny = int(input("Enter the number of pennies: ")) * 0.01
    nickel = int(input("Enter the number of nickels: ")) * 0.05
    dime = int(input("Enter the number of dime: ")) * 0.10
    quarter = int(input("Enter the number of quarter: ")) * 0.25

    amount_payed = float("{:.2f}".format(penny + nickel + dime + quarter))
    print("Total amount payed: $", amount_payed,)

    if amount_payed >= MENU[order_name]['cost']:
        change = "{:.2f}".format(amount_payed - MENU[order_name]['cost'])
        print(f"Order Received\t The change amount is ${change}")
        return False
    return True


def report():
    print("The available resources are: ")
    print(f"Water: {resources['water']}, Milk: {resources['milk']}, Coffee: {resources['coffee']}")


print(logo)
run = 'on'

while run != 'off':
    order = int(input("Enter 1.Expresso\t2.Latte\t3.Cappuccino "))
    ordered = orders[order-1]
    if not_enough_resources(order):
        print("Sorry! Not enough resources to make coffee")
        run = 'off'
    elif not_enough_cash(ordered):
        print("Amount Insufficient! Please pay sufficient amount")
    else:
        resources['water'] = resources['water'] - MENU[ordered]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[ordered]['ingredients']['coffee']
        if order != 1:
            resources['milk'] = resources['milk'] - MENU[ordered]['ingredients']['milk']
        print('Order Served!☕️')
        run = input("Enter 'off' to stop the machine or 'report' to see the resources: ")
        if run == 'report':
            report()


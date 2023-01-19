MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit" : 0
}


def get_order():
    options = ['espresso', 'latte', 'cappuccino', 'off', 'report']
    order = input(" What would you like to order?: ").lower()
    while order not in options:
        order = input("Type a correct order: ").lower()
    return order


def print_resources():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def has_enough_resources(order):
    for resource in MENU[order]['ingredients']:
        if resources[resource] < MENU[order]['ingredients'][resource]:
            print(f"Sorry, not enough {resource}")
            return False
    return True


def get_money():
    print("Insert coins")
    quarter = round(int(input("How many quarter do you want to put in the machine?: ")) * 25 / 100, 2)
    dimes = round(int(input("How many dimes do you want to put in the machine?: ")) * 10 / 100, 2)
    nickels = round(int(input("How many nickels do you want to put in the machine?: ")) * 5 / 100, 2)
    pennies = round(int(input("How many pennies do you want to put in the machine?: ")) / 100, 2)
    return quarter + dimes + nickels + pennies


def has_enough_money(order, money):
    if money < MENU[order]['cost']:
        return False
    return True


def deduct_resources(order):
    for resource in MENU[order]['ingredients']:
        resources[resource] -= MENU[order]['ingredients'][resource]
    resources['profit'] += MENU[order]['cost']


def make_coffee(order, money):
    deduct_resources(order)
    change = round(money - MENU[order]['cost'], 2)
    print(f"Here is {change} in change.")
    print(f"Enjoy your {order}!")


def use_coffee_machine():
    while True:
        order = get_order()
        if order == 'off':
            break
        if order == 'report':
            print_resources()
            continue
        if not has_enough_resources(order):
            continue
        money = get_money()
        if not has_enough_money(order, money):
            print("You do not have enough money for this. Refund has been applied.")
            continue
        make_coffee(order, money)


use_coffee_machine()

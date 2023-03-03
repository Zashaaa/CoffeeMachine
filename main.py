menu = {
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
    "coffee": 100
}


def print_report():
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")
        # TODO: print juiste eenheid
        # print(f"Milk: {resources['milk']}ml")
        # print(f"Coffee: {resources['coffee']}gr")


def check_resources(coffee_order):
    ingredients_needed = menu[coffee_order]["ingredients"]
    for ingredient in ingredients_needed:
        amount_needed = menu[coffee_order]["ingredients"][ingredient]
        amount_resource = resources[ingredient]
        if amount_needed > amount_resource:
            print(f"There's not enough {ingredient} to make {coffee_order}.")
            return False
    print("Ok")
    return True


def handle_order(coffee_order, price):
    print(f"{coffee_order.title()} costs {price}. Please insert money")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many quarters? "))
    pennys = int(input("How many penny's? "))
    money_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennys * 0.01)
    if money_inserted >= price:
        make_coffee(coffee_order)
        change = money_inserted - price
        print(f"Your change is {change}")
        # TODO: Append money to existing money in resources
        resources["money"] = price
        print(f"Please enjoy your {coffee_order}")
    else:
        print("Not enough money inserted.")
        print(f"${money_inserted} is being refunded")


def make_coffee(coffee_order):
    ingredients_needed = menu[coffee_order]["ingredients"]
    for ingredient in ingredients_needed:
        amount_needed = menu[coffee_order]["ingredients"][ingredient]
        resources[ingredient] -= amount_needed


def coffee_machine():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print_report()
        coffee_machine()
    else:
        enough_resources = check_resources(order)
        if enough_resources:
            handle_order(order, menu[order]["cost"])
            coffee_machine()
        else:
            coffee_machine()


coffee_machine()

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
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")


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
            make_coffee(order)
            coffee_machine()
        else:
            coffee_machine()


coffee_machine()


# TODO 1: Print resources report
# TODO 2: get order
## TODO 2a: check resources per order
### TODO 2a1 Fail en report when resources not enough
### TODO 2a2 Ask for money to insert when enough
# TODO 3: make coffee
# TODO 4: refund 2 much paid money
# TODO 5: decrease resources
# TODO 6: add money
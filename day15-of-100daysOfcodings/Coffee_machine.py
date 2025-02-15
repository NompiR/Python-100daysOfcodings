MENU = {
    'espresso': {
        'ingredients': {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee":24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

profit = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients, resources):
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            is_enough = False
    return is_enough


def process_coin():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for items in order_ingredients:
        resource[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕")



is_coffee_machine_on = True

while is_coffee_machine_on:
    select = input("What would you like? (espresso/ latte/ cappuccino): ")

    if select == "off":
        is_coffee_machine_on = False
    elif select == 'report':
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[select]
        if is_resources_sufficient(drink['ingredients'], resource):
            payment = process_coin()
            if is_transaction_success(payment, drink['cost']):
                make_coffee(select, drink['ingredients'])


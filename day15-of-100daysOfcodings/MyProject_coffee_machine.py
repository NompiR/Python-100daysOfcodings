MENU = {
    'espresso': {
        'ingredients': {
            "water": 100,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee":20,
        },
        "cost": 10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30
    }
}

profit = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 80,
}


def is_resource_sufficient(available_resource, resources):
    is_coffee_true = True
    for resource_items in available_resource:
        if not available_resource[resource_items] <= resources[resource_items]:
            print(f"Sorry there is not enough {resource_items}.")
            is_coffee_true = False
    return is_coffee_true


def is_resource_deducted(reduce_resource):
    for deduced_items in reduce_resource:
        resource[deduced_items] -= reduce_resource[deduced_items]


def is_amount_sufficient(menu_amount, user_amount):
    global profit
    if menu_amount <= user_amount:
        changes = user_amount - menu_amount
        profit += menu_amount
        if changes != 0:
            print(f"Here is {changes} in changes.")
        return True
    else:
        print("There is not enough amount")
        print(f"You can get refund amount of {user_amount}")


is_coffee_on = True

while is_coffee_on:

    select = input("What would you like? (espresso/ latte/ cappuccino): ")
    if select == 'off':
        is_coffee_on = False
    elif select == 'report':
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: Rs{profit}")
    else:
        drink = MENU[select]
        drink_ingredient = drink['ingredients']
        drink_cost = drink['cost']

        if is_resource_sufficient(drink_ingredient, resource):
            is_coffee_on = True
            is_resource_deducted(drink_ingredient)
            amount = int(input(f"Enter amount for {select}: "))
            if is_amount_sufficient(drink_cost, amount):
                print(f"Enjoy drink your {select}! ")

        else:
            is_coffee_on = False




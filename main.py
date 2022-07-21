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
    "money": 0
}


def coffee_machine():

    def print_report():
        r = resources
        print(f"Water: {r['water']}ml\nMilk: {r['milk']}ml\nCoffee: {r['coffee']}g\nMoney: ${r['money']}")

    drink_type = input("What would you like? (espresso/latte/cappuccino): ")

    def drink_order():
        if drink_type == "off":
            return
        elif drink_type == "report":
            print_report()
        else:
            check_resources(drink_type)

    def check_resources(order):
        for option in MENU:
            if option == order:
                prep = MENU[option]['ingredients']
                for item in prep:
                    if resources[item] - prep[item] <= 0:
                        print(f"Sorry there is not enough {item}.")
                        return
                count_coins(MENU[option]["cost"])

    def count_coins(cost):
        print(f"Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        coins_input = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

        if coins_input < cost:
            print("Not enough funds. Money refunded.")
        if coins_input >= cost:
            resources["money"] += cost
            print(resources["money"])
            if coins_input > cost:
                change = round(coins_input - cost, 2)
                print(f"Here is ${change} in change.")
            make_coffee()

    def make_coffee():
        ingredients = MENU[drink_type]["ingredients"]
        for item in ingredients:
            resources[item] -= ingredients[item]
        print(f"Here is your {drink_type}! Enjoy! ☕️")
        coffee_machine()

    drink_order()


coffee_machine()

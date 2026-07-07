from platform import machine

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
}

money = 0

is_on = True
while is_on:

    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if user_order == "off":
            is_on = False
    elif user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
         def check_resources(drink_name):
             drink_ingredients = MENU[drink_name]['ingredients']

             for item in drink_ingredients:
                 if drink_ingredients[item] > resources[item]:
                     print(f"sorry there is no enough {item}")
                     return False
             return True


         if check_resources(user_order):
             quarters = float(input("Please insert coins.\nhow many quarters?: "))
             dimes = float(input("how many dimes?: "))
             nickles = float(input("how many nickles?: "))
             pennies = float(input("how many pennies?: "))

         total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

         drink_cost = MENU[user_order]['cost']

         if total_coins >= drink_cost:
             chang = round(total_coins - drink_cost, 2)
             print(f"Here is ${chang} in change.")

             money += drink_cost
             drink_ingredients = MENU[user_order]['ingredients']
             for item in drink_ingredients:
                 resources[item] -= drink_ingredients[item]
             print(f"Here is your {user_order} ☕. Enjoy!")
         else:
             print("Sorry that's not enough money. Money refunded.")








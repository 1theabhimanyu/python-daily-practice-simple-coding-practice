resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

profit = 0
#machine code
is_on = True

while is_on:
    choice = input("What would you like? espresso/latte/cappuccino:  ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources["water"] < drink["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < drink["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < drink["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            total = quarters + dimes + nickels + pennies

            if total <= drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(total - drink["cost"], 2)
                profit += drink["cost"]
                resources["water"] -= drink["ingredients"]["water"]
                resources["milk"] -= drink["ingredients"]["milk"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy!")
    



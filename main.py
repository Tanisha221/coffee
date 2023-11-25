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
    "coffee": 100
}

profit = 0
money = 0


def transaction(cost):
    global profit
    global money
    print("Please enter the coins")
    quarters = int(input("how many quarters ? :"))
    dimes = int(input("how many dimes ? :"))
    nickels = int(input("how many nickels ? :"))
    pennies = int(input("how many pennies ? :"))
    money += (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    profit += cost


while True:
    response = input("What would you like? (espresso/latte/cappuccino):")
    if response == "off":
        exit()
    elif response == "report":
        for i in resources:
            count = 0
            if count < 2:
                print(i + " : " + str(resources[i]) + "ml")
            elif count == 2:
                print(i + " : " + str(resources[i]) + "g")
            count += 1
        print("money : $" + str(profit))

    elif response == "espresso":
        if resources["water"] < 50:
            print("sorry there is not enough water")
        elif resources["coffee"] < 18:
            print("sorry there is not enough coffee")
        else:
            transaction(1.5)
            if money >= 1.5:
                resources["water"] -= 50
                resources["coffee"] -= 18
                change = money - 1.5
                print("Here is $ " + str(change) + " in change.")
                print("Here is your ☕espresso. Enjoy!")
                change = 0
                money = 0

    elif response == "latte":
        if resources["water"] < 200:
            print("sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("sorry there is not enough coffee")
        elif resources["milk"] < 150:
            print("sorry there is not enough milk")
        else:
            transaction(2.5)
            if money >= 2.5:
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
                change = money - 2.5
                print("Here is $ " + str(change) + " in change.")
                print("Here is your ☕latte. Enjoy!")
                change = 0
                money = 0

    elif response == "cappuccino":
        if resources["water"] < 250:
            print("sorry there is not enough water")
        elif resources["coffee"] < 24:
            print("sorry there is not enough coffee")
        elif resources["milk"] < 100:
            print("sorry there is not enough milk")
        else:
            transaction(3.0)
            if money >= 3.0:
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
                change = money - 3.5
                print("Here is $ " + str(change) + " in change.")
                print("Here is your ☕espresso. Enjoy!")
                change = 0
                money = 0

#100 days of code: The copmplete Python Pro Bootcamp

#Coffee machine - day 15 project

import menu
from collections import Counter

profit = 0

def input_data(subtracted_resources):
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == 'off':
            exit()
        elif coffee_type == 'report':
            water = subtracted_resources['water']
            milk = subtracted_resources['milk']
            coffee = subtracted_resources['coffee']
            global profit
            money = profit
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}$")
        else:
            return coffee_type


def payment(coffee_type, subtracted_resources):
    if coffee_type == 'espresso':
        cost = menu.MENU['espresso']['cost']
    elif coffee_type == 'latte':
        cost = menu.MENU['latte']['cost']
    elif coffee_type == 'cappuccino':
        cost = menu.MENU['cappuccino']['cost']

    print(f"You have to pay {cost}$. Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    change = sum - cost

    if sum >= cost:
        print(f"Here is your {round(change, 2)}$ in change")
        global profit
        profit += cost
        paid = True
        return  paid
    elif sum < cost:
        print("Not enough. Money refunded.")
        paid = False
        return paid


def check_resources(coffee_type, subtracted_resources):
    do_not_calculate = False
    for item in subtracted_resources:
        if menu.MENU[coffee_type]['ingredients'][item] >= subtracted_resources[item]:
            print(f"Sorry, there is not enough {item}.")
            do_not_calculate = True
    if do_not_calculate == True:
        print("Type 'off' to turn off the machine.")
    return do_not_calculate
        

def initial_resources():
    resources = menu.resources
    subtracted_resources = resources
    return subtracted_resources

    
def calculate_next_resources(coffee_type, subtracted_resources):
    ingredients = Counter(menu.MENU[coffee_type]['ingredients'])
    resources = Counter(subtracted_resources)
    subtracted_resources = resources - ingredients
    return subtracted_resources

    

def main():
        subtracted_resources = initial_resources()
        while True:
            coffee_type = input_data(subtracted_resources)
            do_not_calculate = check_resources(coffee_type, subtracted_resources)
            if do_not_calculate == False:
                paid = payment(coffee_type, subtracted_resources)
                if paid == True:
                    subtracted_resources = calculate_next_resources(coffee_type, subtracted_resources)
                    print(f"Here is your {coffee_type}. Enjoy!")

main()

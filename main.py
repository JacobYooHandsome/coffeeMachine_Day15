from data import MENU, resources
print("Hello world")
coffee_machine_on = True


def check_water(coffee_type, machine_resources):
    if coffee_type['water'] > machine_resources['water']:
        return False
    else:
        return True


def check_milk(coffee_type, machine_resources):
    if coffee_type['milk'] > machine_resources['milk']:
        return False
    else:
        return True


def check_coffee(coffee_type, machine_resources):
    if coffee_type['coffee'] > machine_resources['coffee']:
        return False
    else:
        return True


def check_resources(coffee_ask, machine_resources):
    if check_water(MENU[f'{coffee_ask}']['ingredients'], machine_resources):
        if check_coffee(MENU[f'{coffee_ask}']['ingredients'], machine_resources):
            if coffee_ask != 'espresso':
                if check_milk(MENU[f'{coffee_ask}']['ingredients'], machine_resources):
                    return MENU[f'{coffee_ask}']['cost']
                else:
                    print("Sorry there is not enough milk.")
                    return 0

            else:
                return MENU[f'{coffee_ask}']['cost']
        else:
            print("Sorry there is not enough coffee.")
            return 0
    else:
        print("Sorry there is not enough water.")
        return 0


def calculate_transaction(cost):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    if total >= cost:
        return total - cost
    else:
        return -1


while coffee_machine_on:
    coffee_ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_ask == "off":
        coffee_machine_on = False
    elif coffee_ask == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        coffee_cost = check_resources(coffee_ask, resources)
        if coffee_cost > 0:
            print(f"Your total is: {coffee_cost}")
            print("Please insert coins:")
            change = calculate_transaction(coffee_cost)
            if change >= 0:
                print(f"Here is ${change} in change.")
                print(f"Here is your {coffee_ask}. Enjoy!")
                if coffee_ask != "espresso":
                    resources['milk'] -= MENU[f'{coffee_ask}']['ingredients']['milk']
                resources['water'] -= MENU[f'{coffee_ask}']['ingredients']['water']
                resources['coffee'] -= MENU[f'{coffee_ask}']['ingredients']['coffee']
                resources['money'] += coffee_cost
            else:
                print("Not enough money. Money refunded.")

        else:
            continue






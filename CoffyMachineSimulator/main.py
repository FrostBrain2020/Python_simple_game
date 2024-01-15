from data import resources, MENU, money_counter, coffe_machine

profit = 0


def print_report():
    print(f"Watter: {resources["water"]}ml\n"
          f"Milk: {resources["milk"]}ml\n"
          f"Coffe: {resources["coffee"]}g\n"
          f"Money: ${profit}")


def enough_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"The machine does not have enough {item}.")
            return False
    return True


def reset_money_counter():
    for coin in money_counter:
        money_counter[coin] = 0


def calculate(counter, price):
    """Penny - 1 cent, Nickel - 5 cent, Dime - 10 cent, Quarter - 25 cent"""
    return price - (int(counter["quarters"]) * 0.25 +
                    int(counter["dimes"]) * 0.1 +
                    int(counter["nickles"]) * 0.05 +
                    int(counter["pennies"]) * 0.01)


def use_resources(ingredients):
    for item in resources:
        resources[item] -= ingredients[item]


def start_order(order):
    global profit
    if enough_resources(MENU[order]["ingredients"]):
        money_counter["dimes"] = input("How many dimes?: ")
        money_counter["nickles"] = input("How many nickles?: ")
        money_counter["pennies"] = input("How many pennies?: ")
        money_counter["quarters"] = input("How many quarters?: ")
        can_buy = calculate(money_counter, MENU[order]["cost"])
        if can_buy > 0:
            print("Sorry that's not enough money. Money refunded.")
            machine_turn_on()
        else:
            print(f"Here is ${round(-1 * can_buy, 2)} in change.")
            use_resources(MENU[order]["ingredients"])
            profit += float(MENU[order]["cost"])
            print(f"Here is your {order} ☕ Enjoy!")
    else:
        machine_turn_on()


def machine_turn_on():
    is_on = True
    while is_on:
        reset_money_counter()
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            is_on = False
        elif order == "report":
            print_report()
        elif order == "espresso":
            start_order("espresso")
        elif order == "latte":
            start_order("latte")
        elif order == "cappuccino":
            start_order("cappuccino")
        else:
            print("You click wrong button. Try again")


machine_turn_on()

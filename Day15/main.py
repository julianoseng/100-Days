from data import MENU, MACHINE
MACHINE_ON = True


def report():
    machine_water = MACHINE['ingredients']['water']
    machine_milk = MACHINE['ingredients']['milk']
    machine_coffee = MACHINE['ingredients']['coffee']
    machine_money = MACHINE['money']
    return (
        f"Water: {machine_water}ml\n"
        f"Milk: {machine_milk}ml\n"
        f"Coffee: {machine_coffee}g\n"
        f"Money: ${machine_money}"
    )


def check_resources(drink):
    global MACHINE_ON
    if MACHINE['ingredients']['water'] < MENU[drink]['ingredients']['water']:
        print('Sorry, there is not enough water.')
        make_coffee()
    elif MACHINE['ingredients']['coffee'] < MENU[drink]['ingredients']['coffee']:
        print('Sorry, there is not enough coffee beans.')
        make_coffee()

    for ingredient in MENU[drink]['ingredients']:
        if ingredient == "milk":
            if MACHINE['ingredients']['milk'] < MENU[drink]['ingredients']['milk']:
                print('Sorry, there is not enough milk.')
                make_coffee()


def process_coins(quarters_ins, dimes_ins, nickels_ins, pennies_ins):
    quarter_amount = quarters_ins * .25
    dime_amount = dimes_ins * .10
    nickel_amount = nickels_ins * .05
    penny_amount = pennies_ins * .01
    total_coins_inserted = quarter_amount + dime_amount + nickel_amount + penny_amount
    return total_coins_inserted


def subtract_ingredients(drink):
    MACHINE['ingredients']['water'] -= MENU[drink]['ingredients']['water']
    MACHINE['ingredients']['coffee'] -= MENU[drink]['ingredients']['coffee']
    for ingredient in MENU[drink]['ingredients']:
        if ingredient == "milk":
            MACHINE['ingredients']['milk'] -= MENU[drink]['ingredients']['milk']


def make_coffee():
    global MACHINE_ON
    while MACHINE_ON:
        drink_select = input("What would you like? Espresso/Latte/Cappuccino").lower()

        if drink_select == "off":
            MACHINE_ON = False
        elif drink_select == "report":
            print(report())
            make_coffee()

        check_resources(drink_select)

        print("Please insert coins.")
        quarters = int(input("How many quarters? :"))
        dimes = int(input("How many dimes? :"))
        nickels = int(input("How many nickels? :"))
        pennies = int(input("How many pennies? :"))
        coins_given = process_coins(quarters, dimes, nickels, pennies)

        if coins_given < MENU[drink_select]['cost']:
            print("Sorry, that's not enough money. Money refunded.")
            make_coffee()
        else:
            change = coins_given - MENU[drink_select]['cost']
            change = "{:.2f}".format(change)
            subtract_ingredients(drink_select)
            print(f"Enjoy your {drink_select}! Your change is ${change}")
        MACHINE["money"] += MENU[drink_select]['cost']


make_coffee()

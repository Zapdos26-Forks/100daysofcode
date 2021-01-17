from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice in options.split('/'):
            drink = menu.find_drink(choice)
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            is_payment_successful = money_machine.makePayment(drink.cost)
            if is_enough_ingredients and is_payment_successful:
                coffee_maker.make_coffee(drink)
        else:
            print('Invalid input.')

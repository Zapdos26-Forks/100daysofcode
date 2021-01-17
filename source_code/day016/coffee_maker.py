

class CoffeeMaker:
    def __init__(self):
        self.__resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.__resources['water']}ml")
        print(f"Milk: {self.__resources['milk']}ml")
        print(f"Coffee: {self.__resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.__resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.__resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

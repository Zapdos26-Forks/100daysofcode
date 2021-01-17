class MoneyMachine:
    def __init__(self, currency="$", coins={
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }):
        self.__currency = currency
        self.__coins = coins
        self.__profit = 0
        self.__money_received = 0

    def report(self):
        print(f"Money: {self.__currency}{self.__profit}")

    def processCoins(self):
        print("Please insert coins.")
        for coin in self.__coins:
            self.__money_received += int(
                input(f"How many {coin}? ")) * self.__coins[coin]
        return self.__money_received

    def makePayment(self, cost):
        self.processCoins()
        if self.__money_received >= cost:
            change = round(self.__money_received - cost, 2)
            print(f"Here is {self.__currency}{change} in change.")
            self.__profit += cost
            self.__money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.__money_received = 0
            return False

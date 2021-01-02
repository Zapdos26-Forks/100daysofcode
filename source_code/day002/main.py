if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    bill = float(input("What is the total bill? $"))
    tip_percentage = int(input(
        "What percentage tip would you like to give? 10, 12, 15? "))
    people = int(input("How many people to split the bill? "))
    print(
        f'Each person should pay: ${round(bill/people * (1 + tip_percentage/100),2)}')

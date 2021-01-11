#from art import logo

from replit import clear
import sys

# Calculator
# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2


3

# Divide


def divide(n1, n2):
    return n1 / n2


# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    # print(logo)

    num1 = float(input("What is the first number?\n"))
    for symbol in operations:
        print(symbol)

    repeat = True

    while repeat:
        operation_symbol = (input("Pick an operation:\n"))

        num2 = float(input("What is the next number?\n"))

        calc_function = operations[operation_symbol]

        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        while True:
            x = input(
                f"Type 'y' to continue calculating with {answer}, type 'n' to restart calculator, and type 'exit' to exit.\n").lower()
            if x == "y":
                num1 = answer
                break
            elif x == 'n':
                repeat = False
                clear()
                calculator()
            elif x == 'exit':
                print('Exiting')
                sys.exit()
            else:
                print('Not a valid option')


calculator()

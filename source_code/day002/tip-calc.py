# Get the total bill
bill = float(input("What's the total bill?: "))

#How much would you like to tip?
tip = float(input("What percentage tip would you like to give? 10, 12, or 15: "))

#How many ways should the bill be split?
split = int(input("How many ways do you want to split the bill?: "))

pay = (bill * (1 + (tip / 100))) / split 

pay_rounded = round(pay, 2)

print(f"Each person should pay: ${pay_rounded}")
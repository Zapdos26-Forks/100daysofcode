from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    maximum = max(bidding_record, key=bidding_record.get)
    print(f"The winner is {maximum} with a bid of ${bidding_record[maximum]}")


while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        break
    elif should_continue == "yes":
        clear()
find_highest_bidder(bids)

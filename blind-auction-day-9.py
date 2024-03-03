#100 days of code: The copmplete Python Pro Bootcamp

#Blind auction - day 9 project

import os

print("Welcome to the blind auction")

bidding = {}

while True:
    bidder_name = input("What is your name?: ")
    bid_price = float(input("What's your bid?: $"))

    bidding[bidder_name] = bid_price

    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if continue_auction == "yes":
        os.system('clear')
    elif continue_auction == "no":
        os.system('clear')
        highest_bid = max(bidding, key=bidding.get)
        print(f"The winner is {highest_bid} with a bid of ${bidding[highest_bid]}")
        break
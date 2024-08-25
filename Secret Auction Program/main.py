from os import system
from art import logo

print(logo)
auction = {}
auction_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not auction_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid price?\n"))
    auction[name] = price
    rest_user = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if rest_user == 'no':
        auction_finished = True
        find_highest_bidder(auction)
    elif rest_user == 'yes':
        system('cls')

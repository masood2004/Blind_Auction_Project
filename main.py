# TODO-1: Ask the user for input
import os

print("Welcome to the secret aution program.")


# TODO-2: Save data into dictionary {name: price}

bid_info = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: PKR"))
    bid_info[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls')
    if continue_bid == 'no':
        break

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary



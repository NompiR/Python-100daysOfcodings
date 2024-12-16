my_bid_dict = {}

def find_highest_bidder(bidding_record):
    highest = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")



is_bidder = True
while is_bidder:

    print("Welcome to the secret auction program.")
    name = input("What is your name?: ").capitalize()
    my_bid = int(input("What\'s your bid?: $ "))
    if name not in my_bid_dict:
        my_bid_dict[name] = my_bid
    else:
        print("already exist..")

    is_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if is_other_bidder == 'no':
        find_highest_bidder(my_bid_dict)
        is_bidder = False
    else:
        print("\n"*20)


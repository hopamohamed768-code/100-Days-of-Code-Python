import art
print(art.logo)

def blind_auction():
    owners = {}
    add_bid = True

    while add_bid:
        name_of_owners = input("What is your name?\n")
        owners[name_of_owners] = int(input("What is your bid?\n"))
        owners_bid = input("Are there any other bidders? Type 'yes or 'no'.").lower()

        if owners_bid == "yes":
            print("\n" * 100)
        else:
            add_bid = False


    max_bid_name = max(owners, key=owners.get)
    max_bid_num = owners[max_bid_name]
    print(f"The winner is {max_bid_name} with a bid of ${max_bid_num}")

blind_auction()
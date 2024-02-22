
def auction(name, amount):
    secret_auction_dict[name] = amount
    return secret_auction_dict


secret_auction_dict={}
end_of_auction = False
while not end_of_auction:
    name = input("Name: ")
    amount = input("bid amount: $")
    auction(name, amount)
    more_bidders = input("Are there more bidders?(yes or no) ")
    if more_bidders == 'no':
        end_of_auction = True
secret_auction = auction(name, amount)
max_value = max(secret_auction.values())
max_key = max(secret_auction, key=auction.get)


print(f"The winner is {max_key} with a bid of ${max_value}")


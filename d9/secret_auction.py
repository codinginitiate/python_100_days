
def auction(name, amount):
    auction_dict[name] = amount
    return auction_dict


auction_dict={}
end_of_auction = False
while not end_of_auction:
    name = input("Name: ")
    amount = input("bid amount: $")
    auction(name, amount)
    more_bidders = input("Are there more bidders?(yes or no) ")
    if more_bidders == 'no':
        end_of_auction = True
max_value = max(auction(name, amount).values())
max_key = max(auction(name,amount), key=auction(name,amount).get)


print(f"The winner id {max_key}, with a bid of ${max_value}")

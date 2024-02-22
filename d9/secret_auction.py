
def auction(name, amount):
    auction_dict[name] = amount
    return auction_dict



end_of_auction = False
while not end_of_auction:
    name = input("Name: ")
    amount = input("bid amount: ")
    more_bidders = input("Are there more bidders?(yes or no) ")
    if more_bidders == 'no':
        end_of_auction = True
print(auction(name, amount))



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
for key in auctio_dict:
    if 


print(auction(name, amount))


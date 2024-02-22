
def auction(name, amount):
    auction_dict[name] = amount
    return auction_dict


auction_dict = {}
name = input("Name: ")
amount = input("bid amount: ")
print(auction(name, amount))


import os
os.system('clear')
from art import logo
print(logo)

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
    if more_bidders.lower() == 'no':
        end_of_auction = True
    else:
        os.system('clear')
    print(logo)
max_value = max(auction(name, amount).values())
max_key = max(auction(name,amount), key=auction(name,amount).get)


print(f"The winner is {max_key}, with a bid of ${max_value}")

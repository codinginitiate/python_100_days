import random
#input("Would you like to play a game? ('y'or'n'):  ")

card_list= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    card_list= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    i = 2
    while i > 0:
        player_cards.append(random.choice(card_list))
    print(player_cards)

deal_cards()

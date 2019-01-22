from random import shuffle

SUITS = ('hearts', 'clubs', 'diamonds', 'spades')
CARDS = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
players = []

num_players = 0


def get_new_deck():
    deck = []
    for suit in SUITS:
        for card, value in CARDS.items():
            deck.append({'suit': suit, 'card': card, 'value': value})
    return deck


def shuffle_deck(deck):
    return shuffle(deck)


def get_card():
    global card_deck
    if len(card_deck) > 0:
        return card_deck.pop(0)
    else:
        return False


def deal_one_card(player):
    player.append(get_card())


def deal_cards():
    global num_players
    global card_deck
    while not num_players > 0 and num_players < 6:
        try:
            num_players = int(input("How many players? "))
        except ValueError:
            print('Please try again: ')
        else:
            print('Got it!')

    global players
    for i in range(num_players):
        players.append([])

    for i in range(2):
        for player in players:
            deal_one_card(player)


def get_hand_value(player):
    hand_value = 0
    for card in player:
        if card['card'] == 'A':
            hand_value += 11
        else:
            hand_value += card['value']
        for card in player:
            if hand_value > 21 and card['card'] == 'A':
                hand_value -= 10
    return hand_value


card_deck = get_new_deck()
shuffle_deck(card_deck)

deal_cards()
for player in players:
    print(get_hand_value(player))

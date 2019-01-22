from random import shuffle

suits = ['spades', 'clubs', 'hearts', 'diamonds']
faces = ['J', 'K', 'Q', 'A', '10', '9', '8', '7', '6', '5', '4', '3', '2']
deck = []

for suit in suits:
    for face in faces:
        deck.append((suit, face))

print(deck)

'''shuffle(deck)
for card in deck:
    print(card[1], ' of ', card[0])
    
def deal_card():
    global deck
    return deck.pop()
'''

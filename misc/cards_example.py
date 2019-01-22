from random import shuffle

suits = ['diamonds', 'hearts', 'clubs', 'spades']
faces = ['A', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J']

deck = []
for suit in suits:
    for face in faces:
        deck.append((suit, face))

print(len(deck))
shuffle(deck)
for card in deck:
    print(card[0], ' ', card[1])

# Deck of cards

# Task is develop a program to define deck of cards.

# Deck is collection of Card objects. Cards are stored in deck's attribute called cards which is a list.

# Card object has suit (in case you want to use UTF-8 characters I'll list unicode codes):

# Spades: "♠" or "\u2660"
# Hearts "♥" or "\u2665"
# Diamonds: "♦" or "\u2666"
# Clubs: "♣" or "\u2663"
# and value: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.

# As a additional (optional) task - define a Joker card (empty suit but with value "JOKER").

# You should be able to:

# create new deck (initially sorted)
# shuffle deck it using its shuffle() method
# get last card (by default) or with the given index via pop(index=-1) method
# get random card via get_random() method
# get specific card's position via index() method
# You can realize additional stuff you want - like .pop() moving seen card to the bottom of the deck etc. You can design another deck- or card-related methods.

# Basic recommendations:

# add __repr__ methods so you easy print out the contents of card or deck objects.

import random

class Card:
    suits = {
        'Spades': "\u2660",
        'Hearts': "\u2665",
        'Diamonds': "\u2666",
        'Clubs': "\u2663"
    }

    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __init__(self, suit='Spades', value='Q'):
        self.suit = suit
        self.value = int(value)  # Convert the value to an integer

    def __str__(self):
        return f'{self.values[self.value]} {self.suits[self.suit]}'

    def __repr__(self):
        return str(self)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, str(value)) for suit in Card.suits for value in range(len(Card.values))]

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self, index=-1):
        return self.cards.pop(index)

    def get_random(self):
        return random.choice(self.cards)

    def index(self, card):
        return self.cards.index(card)

def run_some_tests():
    deck = Deck()
    deck.shuffle()
    print(deck.pop())
    print(deck.pop())
    print(deck.pop(23))
    print([str(deck.get_random()) for _ in range(5)])

run_some_tests()
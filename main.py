# Welcome to Poker witht the bros dource code.
import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
    def show(self):
        print('{} of {}'.format(self.rank, self.suit)) # method that is used on a single card to identify
# card = Card('card', 5) ---> card instanciation test
# card.show()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Hearts', 'Clubs', 'Diamonds']: # loop to assign suits to cards
            for r in range(1,14): # nested loop assigning rank to cards
                self.cards.append(Card(s, r)) # card class objects imstanciated insife of deck class 
    def show(self):
        for c in self.cards:
            c.show()
# test_deck = Deck()
# test_deck.show()
class Player:
    pass
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
    def schuffle(self):
        for i in range(len(self.cards) - 1, 0, -1): # assigns i to every card in deck
            r = random.randint(0, i) # assigns random int in range of total cards in deck to card 
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] # switches index with random index 

# test_deck = Deck()
# test_deck.show()
class Player:
    pass
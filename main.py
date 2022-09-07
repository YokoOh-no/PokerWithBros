class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def show(self):
        print(f'{rank} of {suit}')

card = Card('card', 6)
card.show
class Deck:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass
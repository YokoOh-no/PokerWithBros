class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
    def show(self):
        print('{} of {}'.format(self.rank, self.suit)) # method that is used on a single card to identify
# card = Card('card', 5)
# card.show()


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Hearts', 'Clubs', 'Diamonds']:
            for r in range(1,14):
                self.cards.append(Card(s, r))
    def show(self):
        for c in self.cards:
            print(c)
class Player:
    pass
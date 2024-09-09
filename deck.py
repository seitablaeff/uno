# deck.py
import random
from cards import NumberCard, SpecialColorCard, SpecialCard

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.discard_pile = []
        self.shuffle()

    def __str__(self):
        return f'Колода содержит {len(self.cards)} карт.'

    def shuffle(self):
        random.shuffle(self.cards)
        print("Колода перемешана.")

    def deal(self, num_cards):
        if len(self.cards) < num_cards:
            self.cards.extend(self.discard_pile)
            self.discard_pile.clear()
            self.shuffle()
        
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

    def discard(self, cards):
        self.discard_pile.extend(cards)

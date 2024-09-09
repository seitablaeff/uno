# utils.py
from cards import NumberCard, SpecialColorCard, SpecialCard

def create_number_cards(colors):
    cards = []
    for value in range(10):
        for color in colors:
            points = value if value != 0 else 0
            cards.append(NumberCard(color, value, points))
            if value != 0:
                cards.append(NumberCard(color, value, points))
    return cards

def create_special_color_cards(colors):
    special_types = ["Skip", "Reverse", "+2"]
    cards = []
    for effect in special_types:
        for color in colors:
            for _ in range(2):
                cards.append(SpecialColorCard(color, effect))
    return cards

def create_special_cards():
    cards = []
    for effect in ["Смена цвета", "+4"]:
        for _ in range(4):
            cards.append(SpecialCard(effect))
    return cards

def create_deck():
    colors = ["red", "green", "yellow", "blue"]
    cards = create_number_cards(colors)
    cards += create_special_color_cards(colors)
    cards += create_special_cards()
    return cards

def get_initial_card(deck):
    while True:
        initial_card = deck.deal(1)[0]
        if isinstance(initial_card, NumberCard):
            return initial_card
        else:
            deck.discard([initial_card])

# game.py
from player import Player
from deck import Deck
from cards import NumberCard, SpecialColorCard, SpecialCard
from prettytable import PrettyTable

class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.current_player_index = 0
        self.direction = 1
        self.current_card = None

    def next_player(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)
        return self.players[self.current_player_index]

def print_player_table(game, current_player):
    players_table = PrettyTable()
    current_card_table = PrettyTable()
    player_cards = PrettyTable()

    players_table.field_names = ["Игроки", "Кол-во карт", "Направление"]

    current_card = "Нет карты" if not game.current_card else str(game.current_card)
    direction = "Вправо" if game.direction == 1 else "Влево"
    
    direction_strings = []
    for i, player in enumerate(game.players):
        next_player = game.players[(i + game.direction) % len(game.players)]
        if direction == "Вправо":
            direction_strings.append(f"{player.name} -> {next_player.name}")
        else:
            direction_strings.append(f"{player.name} <- {next_player.name}")

    for player, direction_string in zip(game.players, direction_strings):
        players_table.add_row([player.name, len(player.cards), direction_string])

    current_card_table.field_names = ["Карта", "Цвет"]
    if game.current_card:
        if isinstance(game.current_card, NumberCard):
            current_card_table.add_row([str(game.current_card.value), game.current_card.color])
        elif isinstance(game.current_card, SpecialColorCard):
            current_card_table.add_row([game.current_card.effect, game.current_card.color])
        elif isinstance(game.current_card, SpecialCard):
            current_card_table.add_row([game.current_card.effect, "Нет цвета"])

    player_cards.field_names = [str(i) for i in range(1, len(current_player.cards) + 1)]
    player_cards.add_row([str(card) for card in current_player.cards])

    print(players_table)
    print(current_card_table)
    print(f"\nСейчас ходит: {current_player.name}")
    print("\nВаши карты:")
    print(player_cards)
    print("\nВы можете:\nПоставить карту - просто нажмите её номер из списка\nВзять из колоды - введите 'draw'")

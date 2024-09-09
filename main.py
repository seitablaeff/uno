# main.py
from game import Game, print_player_table
from deck import Deck
from utils import create_deck, get_initial_card
from player import Player
from cards import NumberCard, SpecialCard, SpecialColorCard

def play_turn(game, current_player):
    isCorrect = False
    while not isCorrect:
        print_player_table(game, current_player)
        choice = input("Выберите действие: ")

        if choice.isdigit():
            card_index = int(choice) - 1
            if 0 <= card_index < len(current_player.cards):
                chosen_card = current_player.cards[card_index]
                
                # Если нет текущей карты, нельзя положить специальную карту
                if not game.current_card:
                    if isinstance(chosen_card, SpecialCard):
                        print(" ")
                        print("############ Вы не можете поставить специальную карту, когда нет текущей карты. ############")
                        print(" ")
                    else:
                        game.current_card = chosen_card
                        print(f"Вы выбрали карту: {chosen_card}")
                        current_player.cards.pop(card_index)
                        isCorrect = True
                
                # Если выбранная карта специальная
                elif isinstance(chosen_card, SpecialCard):
                    new_color = input("Выберите новый цвет (red, green, yellow, blue): ")
                    if new_color in ["red", "green", "yellow", "blue"]:
                        print(f"Вы выбрали цвет: {new_color}")
                        if chosen_card.effect == "+4":
                            next_player = game.next_player()
                            next_player.cards.extend(game.deck.deal(4))
                            print("Следующий игрок взял 4 карты.")
                        game.current_card = SpecialColorCard(new_color, chosen_card.effect)
                        print(f"Вы выбрали карту: {chosen_card}")
                        current_player.cards.pop(card_index)
                        isCorrect = True
                    else:
                        print(" ")
                        print("############ Неверный цвет. ############")
                        print(" ")
                
                # Если выбранная карта обычная
                else:
                    if isinstance(game.current_card, NumberCard):
                        if isinstance(chosen_card, NumberCard):
                            if chosen_card.color == game.current_card.color or chosen_card.value == game.current_card.value:
                                game.current_card = chosen_card
                                print(f"Вы выбрали карту: {chosen_card}")
                                current_player.cards.pop(card_index)
                                isCorrect = True
                            else:
                                print(" ")
                                print("############ Карта не подходит для текущей карты. ############")
                                print(" ")
                        elif isinstance(chosen_card, SpecialColorCard):
                            if chosen_card.color == game.current_card.color or chosen_card.effect == game.current_card.effect:
                                if chosen_card.effect == "Reverse":
                                    game.direction *= -1
                                elif chosen_card.effect == "Skip":
                                    game.next_player()
                                elif chosen_card.effect == "+2":
                                    next_player = game.next_player()
                                    next_player.cards.extend(game.deck.deal(2))
                                game.current_card = chosen_card
                                print(f"Вы выбрали карту: {chosen_card}")
                                current_player.cards.pop(card_index)
                                isCorrect = True
                            else:
                                print(" ")
                                print("############ Карта не подходит для текущей карты. ############")
                                print(" ")
                    elif isinstance(game.current_card, SpecialColorCard):
                        if isinstance(chosen_card, NumberCard):
                            if chosen_card.color == game.current_card.color or chosen_card.value == game.current_card.value:
                                game.current_card = chosen_card
                                print(f"Вы выбрали карту: {chosen_card}")
                                current_player.cards.pop(card_index)
                                isCorrect = True
                            else:
                                print(" ")
                                print("############ Карта не подходит для текущей карты. ############")
                                print(" ")
                        elif isinstance(chosen_card, SpecialColorCard) or isinstance(chosen_card, SpecialCard):
                            if chosen_card.color == game.current_card.color or chosen_card.effect == game.current_card.effect:
                                if chosen_card.effect == "Reverse":
                                    game.direction *= -1
                                elif chosen_card.effect == "Skip":
                                     game.next_player()
                                elif chosen_card.effect == "+2":
                                    next_player = game.next_player()
                                    next_player.cards.extend(game.deck.deal(2))
                                game.current_card = chosen_card
                                print(f"Вы выбрали карту: {chosen_card}")
                                current_player.cards.pop(card_index)
                                isCorrect = True
                            else:
                                print(" ")
                                print("############ Карта не подходит для текущей карты. ############")
                                print(" ")
            else:
                print(" ")
                print("############ Неверный номер карты. ############")
                print(" ")
        
        elif choice.lower() == "draw":
            new_card = game.deck.deal(1)[0]
            current_player.cards.append(new_card)
            print(f"Вы взяли карту: {new_card}")
            
            # Проверка, можно ли сыграть взятую карту
            if isinstance(game.current_card, NumberCard):
                if isinstance(new_card, NumberCard):
                    if new_card.color == game.current_card.color or new_card.value == game.current_card.value:
                        play_again = input("Вы можете сыграть только что взятую карту. Хотите это сделать? (да/нет): ")
                        if play_again.lower() == "да":
                            current_player.cards.remove(new_card)
                            game.current_card = new_card
                            isCorrect = True
                        else:
                            isCorrect = True
                    else:
                        print(" ")
                        print("############ Взятая карта не подходит для текущей карты. ############")
                        print(" ")
                        isCorrect = True
                elif isinstance(new_card, SpecialColorCard):
                    if new_card.color == game.current_card.color:
                        if isinstance(game.current_card, SpecialColorCard):
                            play_again = input("Вы можете сыграть только что взятую карту. Хотите это сделать? (да/нет): ")
                            if play_again.lower() == "да":
                                current_player.cards.remove(new_card)
                                if new_card.effect == "Reverse":
                                    game.direction *= -1
                                elif new_card.effect == "Skip":
                                    game.next_player()
                                elif new_card.effect == "+2":
                                    next_player = game.next_player()
                                    next_player.cards.extend(game.deck.deal(2))
                                game.current_card = new_card
                                isCorrect = True
                            else:
                                isCorrect = True
                        elif isinstance(game.current_card, NumberCard):
                            if new_card.color == game.current_card.color or new_card.value == game.current_card.value:
                                play_again = input("Вы можете сыграть только что взятую карту. Хотите это сделать? (да/нет): ")
                                if play_again.lower() == "да":
                                    current_player.cards.remove(new_card)
                                    game.current_card = new_card
                                    isCorrect = True
                                else:
                                    isCorrect = True
                            else:
                                print(" ")
                                print("############ Взятая карта не подходит для текущей карты. ############")
                                print(" ")
                                isCorrect = True
                    else:
                        print(" ")
                        print("############ Взятая карта не подходит для текущей карты. ############")
                        print(" ")
                        isCorrect = True
                elif isinstance(new_card, SpecialCard):
                    play_again = input("Вы можете сыграть только что взятую карту. Хотите это сделать? (да/нет): ")
                    if play_again.lower() == "да":
                        new_color = input("Выберите новый цвет (red, green, yellow, blue): ")
                        if new_color in ["red", "green", "yellow", "blue"]:
                            print(f"Вы выбрали цвет: {new_color}")
                            game.current_card = SpecialColorCard(new_color, new_card.effect)
                            current_player.cards.remove(new_card)
                            isCorrect = True
                        else:
                            print(" ")
                            print("############ Неверный цвет. ############")
                            print(" ")
                    else:
                        isCorrect = True
            else:
                isCorrect = True
        else:
            print(" ")
            print("############ Неверное действие. ############")
            print(" ")

def main():
    # Инициализация колоды и игроков
    deck = Deck(create_deck())
    num_of_players = int(input("Введите количество игроков: "))
    players = [Player(input(f"Введите имя игрока {i+1}: "), deck.deal(7)) for i in range(num_of_players)]
    
    # Установка начальной игровой карты
    initial_card = get_initial_card(deck)
    game = Game(players, deck)
    game.current_card = initial_card
    
    # Основной игровой цикл
    while True:
        current_player = game.players[game.current_player_index]
        play_turn(game, current_player)
        print("----------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------")
        
        # Проверка на победу
        if not current_player.cards:
            print(f"Игрок {current_player.name} победил!")
            return
        
        # Переход к следующему игроку
        game.next_player()

if __name__ == "__main__":
    main()

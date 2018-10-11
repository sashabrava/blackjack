import random, os
from instances.card import Card
from instances.player import Player
import viewer_console
class Playground:
    def __init__(self, player1, player2, cards=[]):
        self.player1 = player1
        self.player2 = player2
        self.cards = cards
        self.bid = 0
    def random_card(self):
        #choose a random card and remove it from the list
        chosen_card = self.cards[random.randint(0, len(self.cards)) -1]
        self.cards.remove(chosen_card)
        return chosen_card
    def game_start(self):
        self.player1.cards = []
        self.player2.cards = []
        self.player1.cards.append(self.random_card ())
        self.player1.cards.append(self.random_card ())
        self.player2.cards.append(self.random_card ())
        self.player2.cards.append(self.random_card ())
    def print_winner(self,player):
        if player == self.player1:
            self.player1.money += self.bid
        else:
            self.player1.money -= self.bid
        viewer_console.show_winner(player.name)    
    def generate_new_cards(self):
        cards =[]
        for i in range (2, 11):
            cards.append(Card(str(i), i))
        cards.append(Card("K", 10))
        cards.append(Card("D", 10))
        cards.append(Card("V", 10))
        cards.append(Card("A", 1))
        return cards
    def start_match(self):
        os.system('cls')
        viewer_console.show_introduction()
        self.cards = self.generate_new_cards()
        self.game_start()
        viewer_console.print_cards(self.player1,True)
        viewer_console.print_cards(self.player2,False)
        viewer_console.show_score(self.player1)
        viewer_console.show_help()
        manual_play = True
        game_continues = True
        show_computer_cards = True
        while (game_continues):
            if manual_play: 
                decision = input()
            else:
                decision = "n"
            if decision == "y":
                self.player1.cards.append(self.random_card())
                viewer_console.print_cards(self.player1,True)
                viewer_console.show_score(self.player1)
                if self.player1.player_sum() > 21:
                    self.print_winner(self.player2)
                    break
            elif decision == "n":
                if show_computer_cards:
                    viewer_console.print_cards(self.player2,True)
                    viewer_console.show_score(self.player2)
                    show_computer_cards = False
                manual_play = False
                game_continues = self.chech_winner(False)
                if not game_continues: break
                self.player2.cards.append(self.random_card())
                viewer_console.print_cards(self.player2,True)
                viewer_console.show_score(self.player2)
                game_continues = self.chech_winner(False)
            else:
                viewer_console.show_decision_error()
    def chech_winner(self, print_cards_bool):
        if self.player2.player_sum() == 21 == self.player1.player_sum():
            if print_cards_bool: viewer_console.print_cards(self.player2,True)
            viewer_console.show_standoff()
            return False
        elif self.player2.player_sum() == 21 or (self.player1.player_sum())<self.player2.player_sum()<21:
            if print_cards_bool: viewer_console.print_cards(self.player2,True)
            self.print_winner(self.player2)
            return False
        if self.player2.player_sum() > 21:
            if print_cards_bool: viewer_console.print_cards(self.player2,True)
            self.print_winner(self.player1)
            return False
        return True
import random, os
class Card:
    def __init__(self, sign, value):
        self.sign = sign
        self. value = value
    def __str__(self):
        return self.sign
    
class Player:
    def __init__(self, name, money=1000):
        self.money = money
        self.name = name
        self.score = 0
        self.cards = []
    def max_sum(self): # unused
        max_sum = 0
        for card in self.cards:
            max_sum += card.value
            if card.sign == "A":
                max_sum += 10
        return max_sum
    def print_cards(self, show_all):
        print ("The cards of player {}".format(self.name))
        if show_all:
            for card in self.cards:
                print (card.sign + " " , end="")
        else:
            print(self.cards[0].sign, end="")
        print ("")
    def player_sum(self):
        cards_sum = 0
        a_exists = False
        for card in self.cards:
            cards_sum +=card.value
            if card.sign == "A":
                a_exists = True
        if cards_sum <= 11 and a_exists:
            cards_sum += 10
        return cards_sum 

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
        print ("Player {} won.".format(player.name))
    

def choose_max(cards, player1, player2):
    while(True):
        player1.cards.append(random_card(cards))
        player2.cards.append(random_card(cards))
        if player1.max_sum() > player2.max_sum():
            print (player1.name + " is the first one")
            return (player1,player2)
        elif player2.max_sum() > player1.max_sum():
            print (player2.name + " is the first one")
            return (player2,player1)

 
def show_score(player):
    print ("Total score of Player {} is {}".format(player.name,str(player.player_sum())))
def generate_new_cards():
        cards =[]
        for i in range (2, 11):
            cards.append(Card(str(i), i))
        cards.append(Card("K", 10))
        cards.append(Card("D", 10))
        cards.append(Card("V", 10))
        cards.append(Card("A", 1))
        return cards

def start_match():
    os.system('cls')
    print ("Game starts")
    #print ("You have {} money".format(str(playground.player1.money)))
    playground.cards = generate_new_cards()
    playground.game_start()
    playground.player1.print_cards(True)
    playground.player2.print_cards(False)
    show_score(playground.player1)
    print ("If you want to get a new card (to hit from deck), type 'y'")
    print ("If you want to stop(to stay), type 'n' \n")


    manual_play = True
    while (True):
        
        #show_score(playground.player2)
        if manual_play: 
            decision = input()
        else:
            decision = "n"
        if decision == "y":

            playground.player1.cards.append(playground.random_card())
            playground.player1.print_cards(True)
            show_score(playground.player1)
            #print ("Total score of Player {} is {}".format(playground.player1.name,str(player_sum(playground.player1))))
            if playground.player1.player_sum() > 21:
                playground.print_winner(player2)
                break
        elif decision == "n":
            manual_play = False
            if playground.player2.player_sum() == 21 == playground.player1.player_sum():
                print ("Nobody has won, the score is equal")
                break
            if playground.player2.player_sum() == 21 or (playground.player1.player_sum())<playground.player2.player_sum()<21:
                playground.print_winner(player2)
                break
            #random_card (cards)
            playground.player2.cards.append(playground.random_card())
            playground.player2.print_cards(True)
            show_score(playground.player2)
            if playground.player2.player_sum() > 21:
                playground.print_winner(player1)
                break
        else:
            print("You specified wrong desicion.")


player1 = Player("Alex", 100)
player2 = Player("Computer")
#cards = generate_new_cards()
playground = Playground(player1,player2)

while (True):
    amount = int (input("How much money would you like to bid? Your budget is {}   ".format(playground.player1.money)))
    playground.bid = amount
    start_match()
#amount_of_steps = 0

    #amount_of_steps += 1

#random_card(cards)
#first_player,second_player = choose_max(cards, player1, player2)

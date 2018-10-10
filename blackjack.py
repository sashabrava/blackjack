import random
class Card:
    def __init__(self, sign, value):
        self.sign = sign
        self. value = value
    def __str__(self):
        return self.sign
    
class Player:
    def __init__(self, name):
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
    def print_cards(self):
        print ("The cards of player {}".format(self.name))
        for card in self.cards:
            print (card.sign + " " , end="")
        print ("")

class Playground:
    def __init__(self, player1, player2, cards):
        self.player1 = player1
        self.player2 = player2
        self.cards = cards
def random_card(cards):
    chosen_card = cards[random.randint(0, len(cards)) -1]
    cards.remove(chosen_card)
    #print(chosen_card)
    return chosen_card
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


def generate_new_cards():
    cards =[]
    for i in range (2, 11):
        cards.append(Card(str(i), i))
    cards.append(Card("K", 10))
    cards.append(Card("D", 10))
    cards.append(Card("V", 10))
    cards.append(Card("A", 1))
    return cards
def player_sum(player):
    cards_sum = 0
    a_exists = False
    for card in player.cards:
        cards_sum +=card.value
        if card.sign == "A":
            a_exists = True
    if cards_sum <= 11 and a_exists:
        cards_sum += 10
    return cards_sum    
def show_score(player):
    print ("Total score of Player {} is {}".format(player1.name,str(player_sum(player1))))
player1 = Player("Alex")
player2 = Player("Computer")
cards =generate_new_cards()
player1.cards.append(random_card (cards))
player1.cards.append(random_card (cards))
player2.cards.append(random_card (cards))
player2.cards.append(random_card (cards))
player1.print_cards()
player2.print_cards()
print ("Game starts")
print ("If you want to get a new card (to hit from deck), type 'y'")
print ("If you want to stop(to stay), type 'n' \n")
amount_of_steps = 0
manual_play = True
while (amount_of_steps < 15):
    show_score(player1)
    show_score(player2)
    if manual_play: 
        decision = input()
    else:
        decision = "n"


    if decision == "y":
        player1.cards.append(random_card (cards))
        print ("Total score of Player {} is {}".format(player1.name,str(player_sum(player1))))
        if player_sum(player1) > 21:
            print ("Player {} won. Player {} busted.".format(player2.name, player1.name))
            break
    elif decision == "n":
        manual_play = False
        if player_sum(player2) == 21 or (player_sum(player1)<player_sum(player2)<21):
            print ("Player {} won".format(player2.name))
            break
        #random_card (cards)
        player2.cards.append(random_card (cards))
        if player_sum(player2) > 21:
            print ("Player {} won".format(player1.name))
            break
    else:
        print("You specified wrong desicion.")
    amount_of_steps += 1

#random_card(cards)
#first_player,second_player = choose_max(cards, player1, player2)

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
    def max_sum(self):
        max_sum = 0
        for card in self.cards:
            max_sum += card.value
            if card.sign == "A":
                max_sum += 10
        return max_sum

class Playground:
    pass
def random_card(cards):
    chosen_card = cards[random.randint(0, len(cards))]
    print(chosen_card)
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
        
player1 = Player("Alex")
player2 = Player("Computer")

cards =generate_new_cards()

random_card(cards)
first_player,second_player = choose_max(cards, player1, player2)

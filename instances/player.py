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
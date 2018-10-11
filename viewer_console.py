import colorama
def show_score(player):
    print (colorama.Fore.CYAN +"Total score of Player {} is {}".format(player.name,str(player.player_sum())))
def show_introduction():
	print (colorama.Fore.CYAN + colorama.Style.BRIGHT + "Game starts")
def show_decision_error():
	print(colorama.Fore.RED + colorama.Style.BRIGHT + "You specified wrong desicion.")
def show_winner(name):
	print(colorama.Fore.CYAN + "Player {} won.".format(name))
def ctrl_c():
	print (colorama.Fore.RED + colorama.Style.BRIGHT + "\nYou decided to quit the game. Have a nice day.")
def show_help():
	print (colorama.Fore.CYAN + "If you want to get a new card (to hit from deck), type 'y'")
	print (colorama.Fore.CYAN + "If you want to stop(to stay), type 'n' \n")
def show_standoff():
	print (colorama.Fore.CYAN + "Nobody has won, the score is equal")
def show_money_ask(amount_money):
	print(colorama.Fore.CYAN + "How much money would you like to bid? Your budget is {}".format(amount_money))
def show_money_not_enough():
	print (colorama.Fore.RED + colorama.Style.BRIGHT +"You don't have enough money")
def show_money_exception():
	print (colorama.Fore.RED + colorama.Style.BRIGHT + "Please check entered value")
def show_money_zero():
	print (colorama.Fore.RED + colorama.Style.BRIGHT + "You ran out of money")
	print (colorama.Fore.RED + colorama.Style.BRIGHT + "GAME OVER")

def print_cards(player, show_all):
    print ("The cards of player {}".format(player.name))
    if show_all:
        for card in player.cards:
            print (card.sign + " " , end="")
    else:
        print(player.cards[0].sign, end="")
    print ("")
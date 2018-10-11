from instances.card import Card
from instances.player import Player
from instances.playground import Playground
import colorama
import viewer_console
colorama.init(autoreset=True)
player1 = Player("Alex", 100)
player2 = Player("Computer")
playground = Playground(player1,player2)

while (True):
    if playground.player1.money == 0:
        viewer_console.show_money_zero()
        break
    viewer_console.show_money_ask(playground.player1.money)
    try:
        amount = int (input())
        if amount > playground.player1.money:
            viewer_console.show_money_not_enough()
            continue
        playground.bid = amount
        playground.start_match()
    except KeyboardInterrupt:
        viewer_console.ctrl_c()
        break
    except:
        viewer_console.show_money_exception()
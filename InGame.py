from Player import Player
from TableRules import TableRules

pl = Player()
p2 = Player(True)
tr = TableRules()


tr.deal_open_set(pl)
tr.deal_open_set(p2)


pl.get_player_hand()
p2.get_player_hand()



print(tr.deal_cards(pl))
if tr.is_winner_defined:
    if pl.is_busted:
        print('Game over the house wins and takes the money')
    else:
        print('Game over the player has won and takes the money')
else:
    print(tr.deal_cards(p2))

pl.get_player_hand()
p2.get_player_hand()



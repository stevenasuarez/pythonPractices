from Player import Player
from TableRules import TableRules

pl = Player()
p2 = Player(True)
tr = TableRules()

print(pl)
#print(p2)

print(tr.deal_cards(pl))
#print(pl.hand)
#print(pl.is_dealer)
#print(deck.get_52_k())



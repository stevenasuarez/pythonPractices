from Player import Player
from TableRules import TableRules

pl = Player()
p2 = Player(True)
tr = TableRules()

print(tr.deal_cards(pl))
if not tr.is_winner_defined:
    print(tr.deal_cards(p2))

print(pl)
print(p2)



from Player import Player
from TableRules import TableRules

pl = Player(1000)
p2 = Player(2000, True)
tr = TableRules()


def validate_bet(bankroll, bet):
    while True:
        if bankroll >= bet:
            print('Valid bet, money taken from bankroll')
            tr.bet_money += bet
            break
        else:
            bet = int(input('invalid bet, please input a valid amount'))


def set_bet():
    print('Welcome players, please raise your bets')
    pl_bet = int(input('p1 your bet'))
    validate_bet(pl.bankroll, pl_bet)
    pl.decrease_bankroll(pl_bet)
    p2_bet = int(input('p2 your bet'))
    validate_bet(p2.bankroll, p2_bet)
    p2.decrease_bankroll(p2_bet)


set_bet()
tr.deal_open_set(pl)
tr.deal_open_set(p2)

pl.get_player_hand()
p2.get_player_hand()

tr.deal_cards(pl)


def set_house_winning():
    print('Game over the house wins and takes the money')
    p2.increase_bankroll(tr.bet_money)
    print(f'his bankroll is {p2.bankroll}')
    tr.bet_money = 0


def set_player_winning():
    print('Game over the player has won and takes the money')
    pl.increase_bankroll(tr.bet_money)
    print(f'his bankroll is {pl.bankroll}')
    tr.bet_money = 0


if tr.is_winner_defined:
    if pl.is_busted:
        set_house_winning()
    else:
        set_player_winning()
else:
    tr.deal_cards(p2)
    if p2.is_busted:
        set_player_winning()
    else:
        if p2.card_count > pl.card_count:
            set_house_winning()
        elif p2.card_count < pl.card_count:
            set_player_winning()
        elif p2.card_count == pl.card_count:
            print('Tie')



pl.get_player_hand()
p2.get_player_hand()

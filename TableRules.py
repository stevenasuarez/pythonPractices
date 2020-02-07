from Deck import Deck
from PlayerBusted import PlayerBusted
import random


class TableRules:
    bet_money = 0
    is_winner_defined = False
    dc = Deck()
    deck = dc.get_52_k()

    def deal_open_set(self, player):
        for i in range(0, 2):
            try:
                self.add_cards_to_hand(player)
            except PlayerBusted:
                pass


    def deal_cards(self, player):
        try:
            while True:
                hit = input(f'\nYour current hand is {player.hand}'
                            f'\nYour current count is {player.card_count}'
                            f'\nCurrent bet {self.bet_money}'
                            f'\nDo you wanna hit or stay? input h or s respectively')
                if hit == 'h':
                    self.add_cards_to_hand(player)
                elif hit == 's':
                    break
                else:
                    print('Please enter either h or s')
        except PlayerBusted:
            pass
        return 'ici'

    def add_cards_to_hand(self, player):
        card = self.serve_random_card()
        card_value = self.dc.get_card_value(card)
        player.increase_card_count(card_value)
        if card not in player.hand:
            player.hit_card(card)
            self.check_busted(player)

    def serve_random_card(self):
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card

    def check_busted(self, player):
        if player.card_count > 21:
            print('You are busted!')
            self.is_winner_defined = True
            player.is_busted = True
            raise PlayerBusted
        elif player.card_count == 21:
            print('You have won')
            self.is_winner_defined = True
            raise PlayerBusted

    def reset_deck(self):
        self.deck = Deck()

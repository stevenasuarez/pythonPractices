from Deck import Deck

import random


class TableRules:
    dc = Deck()
    deck = dc.get_52_k()

    def deal_cards(self, player):
        pl_count = player.card_count
        while True:
            hit = input('Do you wanna hit or stay? input h or s respectively')
            if hit == 'h':
                card = self.serve_random_card()
                card_value = self.dc.get_card_value(card)
                player.increase_card_count(card_value)
                print(f"before {player.hand}")
                print(f"player count {player.card_count}")
                if card not in player.hand:
                    player.hit_card(card)
            elif hit == 's':
                break
            else:
                print('Please enter either h or s')
        print(player.hand)
        return 'ici'

    def serve_random_card(self):
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card

    def reset_deck(self):
        self.deck = Deck()

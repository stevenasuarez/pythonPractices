class Player:
    def __init__(self, is_dealer=False, is_busted=False, bankroll=0, hand=None, card_count=0):
        self.bankroll = bankroll
        self.is_dealer = is_dealer
        self.is_busted = is_busted
        self.card_count = card_count
        if hand:
            self.hand = hand
        else:
            self.hand = []

    def __str__(self):
        return f"Hey" \
               f"\nThe player has a bankroll of {self.bankroll}" \
               f"\nCards in Hand: {self.hand}" \
               f"\nAnd a card count equal to {self.card_count}" \
               f"\n is dealer {self.is_dealer}"

    def increase_bankroll(self, money_won=0):
        if money_won == 0:
            self.bankroll = int(input("How much do you have to play?"))
        else:
            self.bankroll += money_won

    def decrease_bankroll(self, money_taken):
        self.bankroll -= money_taken

    def hit_card(self, card):
        self.hand.append(card)

    def increase_card_count(self, value):
        self.card_count += value

    def get_player_hand(self):
        if self.is_dealer:
            printable_hand = ['X']
            for card in self.hand[1:]:
                printable_hand.append(card)
            print(f'Croupier current hand'
                  f'\n{printable_hand}')
        else:
            print(f'Player current hand'
                  f'\n{self.hand}')

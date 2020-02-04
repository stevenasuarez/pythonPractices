class Player:
    card_count = 0

    def __init__(self, is_dealer=False, bankroll=0, hand=[]):
        self.bankroll = bankroll
        self.hand = hand
        self.is_dealer = is_dealer

    def __str__(self):
        return f"Hey" \
               f"\nThe player has a bankroll of {self.bankroll}" \
               f"\nCards in Hand: {self.hand}" \
               f"\nAnd a card count equal to {self.card_count}"

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

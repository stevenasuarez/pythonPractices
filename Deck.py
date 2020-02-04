class Deck:
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ['♠', '♦', '♣', '♥']
    values = {}

    def get_52_k(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append(rank + ' ' + suit)
        return deck

    def get_card_value(self, card):
        card = card.split()
        value = card[0]

        if value.isdigit():
            return int(value)
        else:
            if value == 'J' or value == 'Q' or value == 'K':
                return 10

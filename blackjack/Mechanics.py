# Game's Core Mechanics

class Player:
    values = {
        "A": 11, "K": 10, "Q": 10, "J": 10,
        "10": 10, "9": 9, "8": 8, "7": 7,
        "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }

    def __init__(self, name, balance = 1000):
        self.name = name
        self.hand = []
        self.score = 0
        self.balance = balance  # The Default balance will always be 1000 for every user or 'object'.
        self.bet = 0  # Player's bet
        self.previous_bet = 0  # ML uses this to see how player's bet changed round to round.

    def place_bet(self, amount):
        if amount <= 0:
            return False
        if amount > self.balance:
            return False

        self.previous_bet = self.bet
        self.bet = amount
        self.balance -= self.bet
        return True

    def win_bet(self): # For v.s. Machine only
        self.balance += self.bet * 2
        self.bet = 0

    def win_bet_pvp(self, opponent_bet): # Figure out how to do handle this in real time.
        self.balance += self.bet + opponent_bet
        self.bet = 0

    def win_blackjack_dealer(self): # For v.s. Machine only
        self.balance += int(self.bet * 2.5)
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def tie(self):
        self.balance += self.bet
        self.bet = 0

    def broke(self):
        return self.balance <= 0

    def draw_card(self, deck):
            self.hand.append(deck.draw())

    def calculation(self):
        total, aces = 0, 0
        for card in self.hand:
            value = card[:-1]
            total += Player.values[value]
            if value == "A":
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def get_hand(self, hide_first=False):
        """Returns the hand as a list. GUI will use this to render cards."""
        if hide_first:
            return ["?"] + self.hand[1:]
        return list(self.hand)

    def hand_reset(self):
        self.hand.clear()

from Deck_Generator import Deck
from Mechanics import Player

class Game:
    class OnePlayer:
        def __init__(self):
            self.deck = Deck()
            self.player = Player("You")
            self.dealer = Player("Dealer")
            self.p_stand = False
            self.d_stand = False
            self.round_over = False
            self.message = ""

        def get_state(self):
            return {
                "player_hand": self.player.hand,
                "dealer_hand": self.dealer.hand,
                "player_total": self.player.calculation(),
                "dealer_total": self.dealer.calculation(),
                "player_score": self.player.score,
                "dealer_score": self.dealer.score,
                "round_over": self.round_over,
                "message": self.message,
            }

        def start_round(self):
            self.player.hand_reset()
            self.dealer.hand_reset()
            self.p_stand = False
            self.d_stand = False
            self.round_over = False
            self.message = ""
            self.deck.deck_regen()

            for _ in range(2):
                self.player.draw_card(self.deck)
                self.dealer.draw_card(self.deck)

            if self.player.calculation() == 21:
                self.player.score += 1
                self.round_over = True
                self.message = "Blackjack! You win!"
            elif self.dealer.calculation() == 21:
                self.dealer.score += 1
                self.round_over = True
                self.message = "Dealer has Blackjack! Dealer wins."

        def player_hit(self):
            if self.round_over or self.p_stand:
                return

            self.player.draw_card(self.deck)

            if self.player.calculation() > 21:
                self.dealer.score += 1
                self.round_over = True
                self.message = "You busted! Dealer wins."

            if not self.round_over:
                self._dealer_turn()

        def player_stand(self):
            if self.round_over or self.p_stand:
                return

            self.p_stand = True
            self._dealer_turn()

        def _dealer_turn(self):
            if not self.p_stand:
                return

            while self.dealer.calculation() < 17:
                self.dealer.draw_card(self.deck)

            if self.dealer.calculation() > 21:
                self.player.score += 1
                self.round_over = True
                self.message = "Dealer busted! You win."
                return

            self.d_stand = True

            if self.p_stand and self.d_stand:
                self._resolve_round()

        def _resolve_round(self):
            """Compares hands and determines the winner."""
            p = self.player.calculation()
            d = self.dealer.calculation()

            if p > d:
                self.player.score += 1
                self.message = "You won!"
            elif p < d:
                self.dealer.score += 1
                self.message = "Dealer won!"
            else:
                self.message = "It's a tie!"

            self.round_over = True

        def get_final_result(self):
            p = self.player.score
            d = self.dealer.score
            if p > d:
                return f"Final Score: You {p} - Dealer {d} | You won the session!"
            elif p == d:
                return f"Final Score: You {p} - Dealer {d} | It's a tie!"
            else:
                return f"Final Score: You {p} - Dealer {d} | Dealer won the session."

    class TwoPlayers:
        def __init__(self):
            pass

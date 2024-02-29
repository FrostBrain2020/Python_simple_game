from random import choice
CARD_SCORING = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)


class Dealer:

    def __init__(self):
        self.my_cards = []
        self.dealer_cards = []

    def complete_hand(self, hand, amount):
        """Add to the hand list new cards. The given amount indicates how many cards we add."""
        for _ in range(amount):
            hand.append(choice(CARD_SCORING))
        return hand

    def print_hand(self):
        """Reading the status of individual players' cards"""
        print(f"Your card: {self.my_cards}")
        print(f"Computer's card: {self.dealer_cards}")

    def count_points(self, cards):
        """Take list of cards and return the score calculated from the cards."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def who_win(self):
        """A function that determines who won the hand"""
        my_score = self.count_points(self.my_cards)
        self.dealer_cards = self.complete_hand(self.dealer_cards, 1)
        dealer_score = self.count_points(self.dealer_cards)
        while dealer_score < 17:
            self.dealer_cards = self.complete_hand(self.dealer_cards, 1)
            dealer_score = self.count_points(self.dealer_cards)
        self.print_hand()
        if my_score > 21:
            print("Bust - You have above 21 point in cart. You lose")
            return
        elif dealer_score == my_score:
            print("Draw - You and dealer have this same points in cards")
            return
        elif my_score == 0:
            print("You have blackjack. You win!!")
        elif (21 - my_score) < (21 - dealer_score) or dealer_score > 21:
            print("You win!!")
        else:
            print("Computer win :(")

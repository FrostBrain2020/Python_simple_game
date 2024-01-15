from art import logo
import random


# Blackjack / 21 roles:
# You play against the dealer (computer). You must get the closest score to 21 points in the hand.
# If you have more than 21 points, you automatically lose.
# Scoring rules:
# - cards from 2 to 10 have a clear score, e.g. 2 has 2 points etc.
# - Jack, Queen and King always have a value of 10.
# - Ace, depending on your choice, may have a value of 1 or 11
# Glossary of terms:
# Draw - You and dealer have this same points in cards
# Bust - You have above 21 point in cart. You lose

def complete_hand(hand, amount):
    """Add to the hand list new cards. The given amount indicates how many cards we add."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(amount):
        hand.append(random.choice(cards))
    return hand


def print_hand(gamer, computer):
    print(f"Your card: {gamer}")
    print(f"Computer's first card: {computer}")


def count_points(cards):
    """Take list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def who_win(gamer_cards, computer_cards):
    my_score = count_points(gamer_cards)
    computer_cards = complete_hand(computer_cards, 1)
    dealer_score = count_points(computer_cards)
    while dealer_score < 17:
        computer_cards = complete_hand(computer_cards, 1)
        dealer_score = count_points(computer_cards)
    print_hand(my_cards, computer_cards)
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


print(logo)
my_cards = []
dealer_cards = []
continue_drawing_cards = False

my_cards = complete_hand(my_cards, 2)
dealer_cards = complete_hand(dealer_cards, 1)
print_hand(my_cards, dealer_cards)

pick = input("Type 'y' to get another card, type 'n' to pass: ")
if pick == "y":
    continue_drawing_cards = True
while continue_drawing_cards:
    my_cards = complete_hand(my_cards, 1)
    print_hand(my_cards, dealer_cards)
    pick = input("Type 'y' to get another card, type 'n' to pass: ")
    if pick == "n":
        continue_drawing_cards = False
who_win(my_cards, dealer_cards)


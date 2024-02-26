from art import logo
from dealer_brain import Dealer

print(logo)
d = Dealer()
continue_drawing_cards = False

d.my_cards = d.complete_hand(d.my_cards, 2)
d.dealer_cards = d.complete_hand(d.dealer_cards, 1)
d.print_hand()

pick = input("Type 'y' to get another card, type 'n' to pass: ")
if pick == "y":
    continue_drawing_cards = True
while continue_drawing_cards:
    d.my_cards = d.complete_hand(d.my_cards, 1)
    d.print_hand()
    pick = input("Type 'y' to get another card, type 'n' to pass: ")
    if pick == "n":
        continue_drawing_cards = False
d.who_win()

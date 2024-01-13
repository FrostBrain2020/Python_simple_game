import random
from game_data import data
from art import logo


def print_person(person):
    print(f"{person["name"]}: a {person["description"]}, from {person["country"]}")


def correct_answer(guess, person_one, person_two):
    if person_one["follower_count"] > person_two["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
fin = False
first_person = random.choice(data)

while not fin:
    second_person = random.choice(data)
    print_person(first_person)
    print("          VS")
    print_person(second_person)
    choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    is_correct = correct_answer(choice, first_person, second_person)
    if is_correct:
        score += 1
        print(f"\nYou're right!. Current score: {score}")
        first_person = second_person
    else:
        print(f"\n\nGame over. Final score: {score}")
        fin = True

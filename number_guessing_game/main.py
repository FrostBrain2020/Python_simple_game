from random import randint

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10


def set_life():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    elif level == "easy":
        return EASY_LEVEL_TURNS
    else:
        print("Error. Choose correct level")


def check_answer(number):
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")
        return False
    elif guess > number:
        print("To high.")
        return False
    else:
        return True


print("Welcome to the Number Guessing Game!\nI'm thinking of number between 1 and 100.")
search_number = randint(1, 100)
life = set_life()
for i in range(life, 0, -1):
    print(f"You have {i} attempts to guess the number")
    if_guess = check_answer(search_number)
    if if_guess:
        print("You win")
        break
    elif i == 0:
        print("You loose")

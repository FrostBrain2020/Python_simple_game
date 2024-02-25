from random import randint
from sys import exit
import resources

images = [resources.rock, resources.paper, resources.scissors]
score = {
    "wins": 0,
    "loses": 0,
    "draws": 0,
}

while True:
    print(f"Your score is: wins - {score["wins"]}, loses - {score["loses"]}, draws - {score["draws"]}")
    while True:
        try:
            pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
                             "For Exit game type 9: "))
        except ValueError:
            print("Please select correct number.")
            continue
        if pick == 9:
            exit()
        elif pick > 2 or pick < 0:
            print("Please select correct number.")
        else:
            print(images[pick])
            break
    computer_pick = randint(0, 2)
    print(f"Computer choose:\n{images[computer_pick]}")
    if pick == computer_pick:
        print("Draw in the game. No one won!\n")
        score["draws"] = score["draws"] + 1
    elif ((pick == 0 and computer_pick == 2) or
          (pick == 1 and computer_pick == 0) or
          (pick == 2 and computer_pick == 1)):
        print("You win!\n")
        score["wins"] = score["wins"] + 1
    else:
        print("You lose!\n")
        score["loses"] = score["loses"] + 1

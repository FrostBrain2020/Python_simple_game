import random
import resources

images = [resources.rock, resources.paper, resources.scissors]
pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if pick > 2 or pick < 0:
    print("Please select correct number.")
else:
    print(images[pick])
    computer_pick = random.randint(0, 2)
    print(f"Computer choose:\n{images[computer_pick]}")
    if pick == computer_pick:
        print("Draw in the game. No one won! ")
    elif ((pick == 0 and computer_pick == 2) or
          (pick == 1 and computer_pick == 0) or
          (pick == 2 and computer_pick == 1)):
        print("You win!")
    else:
        print("You lose!")

from random import choice
from hangman_dictionary import word_list
from resources import hangman_stages

chosen_word = choice(word_list)
display = []
fin = False
left_to_find = len(chosen_word)
life = 7
letters_used = []

print("Searched word:")
for letter in chosen_word:
    if letter == " ":
        display += " "
    else:
        display += "_"

print("".join(display))

while not fin and life != 0:
    if len(letters_used) != 0:
        print(f"Letters already used: {letters_used}")
    guess = input("Guess a letter: ").lower()
    letters_used.append(guess)
    for i in range(len(chosen_word)):  # for letter in word: => return String
        if chosen_word[i] == guess:
            display[i] = guess
            left_to_find -= 1
    if guess not in display:
        life -= 1
        print(hangman_stages[life])
    print("".join(display))
    if left_to_find == 0:
        fin = True

if life != 0:
    print("You win!")
else:
    print(f"Game Over!\nThe word you are looking for is: {chosen_word}")

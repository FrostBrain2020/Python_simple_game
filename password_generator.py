import random
import resources


def select_symbols(max, list):
    word = []
    for char in range(max):
        word += random.choice(list)
    return word


print("Welcome to the Pypassword_list Generator!")
nr_letters = int(input("How many letters would you like in your password_list?\n"))
nr_numbers = int(input("How many numbers would you have in your password_list?\n"))
nr_symbols = int(input("How many special symbol would you have in your password_list?\n"))
password_list = []
password = ""

password_list += select_symbols(nr_letters, resources.alphabet)
password_list += select_symbols(nr_numbers, resources.numbers)
password_list += select_symbols(nr_symbols, resources.symbols)
random.shuffle(password_list)
for char in password_list:
    password += char

print(password)

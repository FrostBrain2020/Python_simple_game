import random
import resources

print("Welcome to the Pypassword_list Generator!")
nr_letters = int(input("How many letters would you like in your password_list?\n"))
nr_numbers = int(input("How many numbers would you have in your password_list?\n"))
nr_symbols = int(input("How many special symbol would you have in your password_list?\n"))
password_list = []
password = ""

for char in range(1, nr_letters + 1):
    password_list += random.choice(resources.alphabet)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(resources.numbers)
for char in range(1, nr_symbols +1):
    password_list += random.choice(resources.symbols)

random.shuffle(password_list)
for char in password_list:
    password += char

print(password)


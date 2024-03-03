#100 days of code: The copmplete Python Pro Bootcamp

#Password generator - day 5 project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_lenght = nr_letters + nr_symbols + nr_numbers

pass_letters = []
pass_symbols = []
pass_numbers = []


for letter in range(0, nr_letters): 
    pass_letters += random.choice(letters)

for symbol in range(0, nr_symbols):
    pass_symbols += random.choice(symbols)

for number in range(0, nr_numbers):
    pass_numbers += random.choice(numbers)

pass_list = list(pass_letters + pass_symbols + pass_numbers)

random.shuffle(pass_list)

password = ''.join(pass_list)

print("Your unbreakable password:\n")
print(password)

    









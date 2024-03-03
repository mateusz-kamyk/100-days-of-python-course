#100 days of code: The copmplete Python Pro Bootcamp

#Rock-Paper-Scissors game - day 4 project

import random

def computer_chose():
    global computer_chose_number
    computer_chose_number = random.randint(0,2) 
    if computer_chose_number == 0:
        print("Computer chose:\n\n" + "Rock\n")
    elif computer_chose_number == 1:
        print("Computer chose:\n\n" + "Paper\n")
    elif computer_chose_number == 2:
        print("Computer chose:\n\n" + "Scissors\n")


print("This is a Rock-Paper-Scissors game")
chose = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors.\n'))
print("Your chose:\n")
if chose == 0:
    print("Rock\n")
    computer_chose()
    if computer_chose_number == 0:
        print("Draw")
    elif computer_chose_number == 1:
        print("You lose")
    elif computer_chose_number == 2:
        print("You win")
elif chose == 1:
    print("Paper\n")
    computer_chose()
    if computer_chose_number == 1:
        print("Draw")
    elif computer_chose_number == 2:
        print("You lose")
    elif computer_chose_number == 0:
        print("You win")
elif chose == 2:
    print("Scissors\n")
    computer_chose()
    if computer_chose_number == 2:
        print("Draw")
    elif computer_chose_number == 0:
        print("You lose")
    elif computer_chose_number == 1:
        print("You win")
else:
    print("You choose wrong. End of the game")
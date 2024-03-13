#100 days of code: The copmplete Python Pro Bootcamp

#Guess the number game - day 12 project

import random

print("Welcome to the Number Guessing Game!")

def generate_number():
    number = random.randint(1, 100)
    print(f"I am thinking of a number between 1 and 100.")
    return number

def difficulty_level():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess a number.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess a number.")

    return attempts

def subtract_attempt(attempts):
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess a number.")
    return attempts

def guess_number(attempts, number):
    guessing = True
    while guessing:
        guessed_number = int(input("Make a guess: "))
        if guessed_number > number:
            print("Too high.")
        elif guessed_number < number: 
            print("Too low.")
        else:
            print("You got it! You win.")
            break
        if attempts > 1:
            attempts = subtract_attempt(attempts)
        else:
            print("You don't have any attempts left. Game over.")
            guessing = False
        
number = generate_number()
attempts = difficulty_level()
guess_number(attempts, number)
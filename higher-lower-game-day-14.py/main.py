#100 days of code: The copmplete Python Pro Bootcamp

#Higher Lower Game - day 14 project

import random
import game_data

print("Higher Lower Game")

def random_pick():
    random_dict = random.choice(game_data.data)
    name = random_dict['name']
    followers = random_dict['follower_count']
    description = random_dict['description']
    country = random_dict['country']

    return name, followers, description, country

def print_A(name, description, country):
    print(f"Compare A: {name}, a/an {description}, from {country}")

def print_B(name, description, country):
    print(f"Compare B: {name}, a/an {description}, from {country}")

def play_and_compare():
    counter = 0
    game_on = True
    while game_on:
        counter += 1
        name1, followers1, description1, country1 = random_pick()
        name2, followers2, description2, country2 = random_pick()
        print_A(name1, description1, country1)
        print_B(name2, description2, country2)
        decision = input("Who has more followers? Type 'A' or 'B': ")
        if followers1 > followers2:
            right_answer = 'A'
        else:
            right_answer = 'B'
        if decision == right_answer:
            print(f"You're right! Current score is: {counter}.\n")
        else:
            print(f"You lose. Your score: {counter}\n")
            game_on = False

play_and_compare()

#100 days of code: The copmplete Python Pro Bootcamp

#Blackjack - day 11 project

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

start_game = input("Do you want to start a Blackjack game (type 'y' or 'n')?: ")

def start():
    if start_game == "y":
        user_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]
        print(f"Your cards: {user_cards}\nComputer cards: {computer_cards}")
        return user_cards, computer_cards
    else:
        print("Something went wrong.")

user_cards, computer_cards = start()

def add_values(user_cards, computer_cards):
    sum_user_cards = sum(user_cards)
    sum_computer_cards = sum(computer_cards)
    return sum_user_cards, sum_computer_cards


game = True
while game:
    sum_user_cards, sum_computer_cards = add_values(user_cards, computer_cards)
    if sum_user_cards == 21:
        print("You win!")
        game = False
    elif sum_computer_cards == 21:
        print("You lose :(")
        game = False
    elif sum_user_cards and sum_computer_cards == 21:
        print("Draw.")
        game = False
    elif sum_user_cards > 21:
        for index, card in enumerate(user_cards):
            if card == 11:
                ace_or_1_decision = str(input("You have an ace. Do you want to keep it as 1 or 11? Type '1'or '11': "))
                if ace_or_1_decision == "1":
                    user_cards[index] = 1
                elif ace_or_1_decision == "11":
                    user_cards[index] = 11
                else:
                    print("Type error.")
            else:
                continue
        sum_user_cards = sum(user_cards)
        if sum_user_cards > 21:
            print("You lose :(")
            game = False
        elif sum_computer_cards > 21:
            print("You win!")
            game = False
    else:
        new_user_card = input("Do you want another card? Type 'y' or 'n': ")
        if new_user_card == 'y':
            user_cards.append(random.choice(cards))
            print(f"Your cards: {user_cards}")
        elif new_user_card == 'n':
            while True:
                if sum_computer_cards < 17:
                    computer_cards.append(random.choice(cards))
                    sum_computer_cards = sum(computer_cards)
                else:
                    break
            game = False
            print(f"Your cards: {user_cards}")
            print(f"Computer's cards: {computer_cards}")
            if sum_user_cards > sum_computer_cards and sum_user_cards <= 21:
                print("You win!")
            elif sum_computer_cards > sum_user_cards and sum_computer_cards <= 21:
                print("You lose :(")
            elif sum_user_cards > 21:
                print("You lose :(")
            elif sum_computer_cards > 21:
                print("You win!")
            elif sum_user_cards == sum_computer_cards:
                print("Draw.")





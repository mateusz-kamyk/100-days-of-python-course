#100 days of code: The copmplete Python Pro Bootcamp

#Treasure island - day 3 project

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
way_1 = input('''You're at a cross road. Where do you want to go? Type "left" or "right". ''').lower()

if way_1 == "left":
    way_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if way_2 == "wait":
        way_3 = input("You arrived at the isnland unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if way_3 == "yellow":
            print("You win! Congrats.")
        elif way_3 == "red":
            print("You've been burnde by fire. Game Over.")
        elif way_3 == "Blue":
            print("You entered to a room full of beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You've been attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over")

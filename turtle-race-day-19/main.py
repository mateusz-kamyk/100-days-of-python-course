from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter the color: ")

colors = ["red", "blue", "yellow", "black", "green", "purple"]
turtle_number = []

x_start = -230
y_start = -200

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y_start += 50
    new_turtle.goto(x_start, y_start)
    turtle_number.append(new_turtle)

race_on = True

while race_on:
    for turtle in turtle_number:
        if turtle.xcor() > 220:
            race_on = False
            winner = turtle.pencolor()
        turtle.forward(random.randint(1, 5))   

if user_bet == winner:
    print(f"You've won! The {winner} turtle is the winner.")
else:
    print(f"You've lost. The winner is {winner} turtle")

screen.exitonclick()
import turtle
import random

turtle_browar = turtle.Turtle()

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)

    return random_colours

turtle_browar.speed("fastest")

x = -300
y = -300
turtle.colormode(255)
turtle_browar.penup()
turtle_browar.setposition(x, y)

for i in range(12):
    turtle_browar.setposition(x, y + (i * 50))

    for _ in range(12):
        random_colours = random_colour()
        turtle_browar.forward(50)
        turtle_browar.dot(25, random_colours)

screen = turtle.Screen()
turtle_browar.hideturtle()
screen.exitonclick()
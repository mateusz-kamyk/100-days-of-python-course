from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1 

    def increase_speed(self):
        self.x_move *= 1.05
        self.y_move *= 1.05

    def reset_speed(self):
        self.x_move = 0.1
        self.y_move = 0.1
    
    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1

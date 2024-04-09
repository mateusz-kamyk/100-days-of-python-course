from turtle import Turtle
from food import Food


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write_score()
        
    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", "20", "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", "20", "normal"))

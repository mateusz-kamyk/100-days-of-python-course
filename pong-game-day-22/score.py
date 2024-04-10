from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(0, 230)
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align="center", font=("Courier", 40, "normal"))
        
    def add_point_r(self):
        self.r_score += 1
        self.update_score()
        
    def add_point_l(self):
        self.l_score += 1
        self.update_score()
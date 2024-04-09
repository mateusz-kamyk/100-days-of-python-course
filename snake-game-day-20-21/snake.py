from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for turtle_index in range(3):
            self.add_segment(turtle_index)

    def add_segment(self, turtle_index):
        x_start = 20
        y_start = 0
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        x_start -= 20
        new_segment.setpos(x_start, y_start)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_number-1].xcor()
            new_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    

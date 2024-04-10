from turtle import Turtle, Screen, mainloop
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
 
while game_is_on:
    screen.update()
    
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.wall_bounce()
    if ball.xcor() > 340:
        score.add_point_l()
        ball.reset()
        ball.reset_speed()
    if ball.xcor() < -345:
        score.add_point_r()
        ball.reset()
        ball.reset_speed()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        ball.increase_speed()

screen.exitonclick()
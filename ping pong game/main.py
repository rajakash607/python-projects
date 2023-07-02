from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scorecard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scorecard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)
    # wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # paddle hitting
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
    # paddle miss by right player
    if ball.xcor() > 380:
        ball.reset_position()
        ball.hit()
        scoreboard.l_point()
    # paddle miss by left player
    if ball.xcor() < -380:
        ball.reset_position()
        ball.hit()
        scoreboard.r_point()


screen.exitonclick()

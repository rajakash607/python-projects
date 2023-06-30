from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scorecard

screen = Screen()
screen.setup(600, 600)
screen.title("Classic Snake Game")
screen.bgcolor("Black")


screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scorecard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # refreshing food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # collision detection
    if snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

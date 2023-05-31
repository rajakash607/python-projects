from turtle import *
import random

screen = Screen()
screen.setup(500, 400)

colors = ["red", "green", "blue", "yellow", "black", "orange", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
should_continue = True
screen.bgcolor("lightblue")
for _ in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(-238, y_positions[_])
    all_turtles.append(tim)
user_bet = screen.textinput(
    "Make your bet", "choose color of turtle that will win: ")
while should_continue:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            colur = turtle.color()
            print(colur)
            should_continue = False
if colur == user_bet:
    print(f"You got it right buddy! {colur} turtle wins")
else:
    print(f"You got it wrong buddy! {colur} turtle wins")

screen.exitonclick()

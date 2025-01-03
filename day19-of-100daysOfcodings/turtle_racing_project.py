import turtle
from turtle import Turtle, Screen
import random


is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'green', 'blue', 'purple', 'black']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, y_position[i])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lose! The {winning_color} turtle is the winner")


        rand_direction = random.randint(0, 10)
        turtle.forward(rand_direction)


screen.exitonclick()

from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
timmy_the_turtle.shapesize(1.5, 1.5, 1)
timmy_the_turtle.color("OrangeRed1")


#timmy_the_turtle.speed(1)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 120, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(10)


for _ in range(100):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(direction))





screen = Screen()
screen.exitonclick()

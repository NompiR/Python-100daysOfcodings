from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
timmy_the_turtle.shapesize(1.5, 1.5, 1)
timmy_the_turtle.color("OrangeRed1")


#timmy_the_turtle.speed(1)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "orange"]
def draw_shape(num_sides):
    angles = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angles)


for side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(side_n)



screen = Screen()
screen.exitonclick()

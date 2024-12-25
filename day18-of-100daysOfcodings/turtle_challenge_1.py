from turtle import Turtle, Screen


def triangle(move, left):
    for _ in range(4):
        timmy_the_turtle.speed(1)
        timmy_the_turtle.forward(move)
        timmy_the_turtle.left(left)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
timmy_the_turtle.shapesize(1.5, 1.5, 1) #Size the shape
timmy_the_turtle.color("OrangeRed1")

triangle(100, -90)


screen = Screen()
screen.exitonclick()

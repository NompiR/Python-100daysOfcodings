from turtle import Turtle, Screen



timmy_the_turtle = Turtle()
timmy_the_turtle.shape("classic")
timmy_the_turtle.shapesize(1.5, 1.5, 1)
timmy_the_turtle.color("OrangeRed1")


#for _ in range(int(200/(8 + 10))):
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()





screen = Screen()
screen.exitonclick()

import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


timmy_the_turtle = t.Turtle()
t.colormode(255)

timmy_the_turtle.shape("classic")
timmy_the_turtle.shapesize(1.5, 1.5, 1)
timmy_the_turtle.color("OrangeRed1")

direction = [0, 90, 120, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(10)


for _ in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(direction))

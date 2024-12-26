import turtle as t
import random

t.Turtle()
t.shape()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


t.speed("fastest")
def draw_spirograph(size_gap):
    for i in range(int(360 / size_gap)): #or the range is 0, 70
        t.color(random_color())
        t.circle(100)
        current_heading = t.heading()  # heading from 0.0
        t.setheading(current_heading + size_gap) #heading to 0.0 +5 is 0.5 till 70 ranges



draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()

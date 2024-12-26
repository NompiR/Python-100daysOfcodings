from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


lists = ['f', 'b', 'r', 'l', 'c']
dict = {'f': move_forward, 'b': move_backward, 'r': turn_right, 'l':turn_left, 'c': clear}
for i in lists:
    d = dict[i]
    screen.listen()
    screen.onkey(d, i)
    


screen.exitonclick()

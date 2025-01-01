from turtle import Turtle
from scoreboard import  Scoreboard


THREE_SQUARES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_segment = self.segments[0]


    def create_snake(self):
        for position in THREE_SQUARES:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle("square")
        t.speed("slowest")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head_segment.forward(MOVE_DISTANCE)



    def up(self):
        if self.head_segment.heading() != DOWN:
            self.head_segment.setheading(UP)


    def left(self):
        if self.head_segment.heading() != RIGHT:
            self.head_segment.setheading(LEFT)


    def right(self):
        if self.head_segment.heading() != LEFT:
            self.head_segment.setheading(RIGHT)


    def down(self):
        if self.head_segment.heading() != UP:
            self.head_segment.setheading(DOWN)

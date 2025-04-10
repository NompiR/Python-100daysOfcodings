from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        #self.paddle = Turtle()
        #self.x, self.y = x
        """self.paddle.shape("square")
        self.paddle.shapesize(5, 1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(self.x, self.y)"""

        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)


    def go_up(self):
        new_paddle = self.ycor() + 20
        self.goto(self.xcor(), new_paddle)

    def go_down(self):
        new_paddle = self.ycor() - 20
        self.goto(self.xcor(), new_paddle)

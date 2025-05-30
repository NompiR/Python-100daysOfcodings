from turtle import Turtle
FONT = ('Courier', 24, 'normal')
ALIGNMENT = "center"

class Scoreboards(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        #self.write(f"Level: {self.level}", align="left", font=FONT)
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

from turtle import Screen
from paddle import Paddle
from  ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
score = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_x = Paddle((360, 0))
paddle_y = Paddle((-360, 0))
balls = Ball()


screen.listen()
screen.onkeypress(paddle_x.go_up, "Up")
screen.onkeypress(paddle_x.go_down, "Down")

screen.onkeypress(paddle_y.go_up, "w")
screen.onkeypress(paddle_y.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(balls.move_speed)
    screen.update()
    balls.go_upto()

    #wall detection collision
    if balls.ycor() > 280 or balls.ycor() < -280:
        #need to bounce the ball
        balls.bounce_x()

        #detect collision with r paddle
    if balls.distance(paddle_x) < 50 and balls.xcor() > 320 or balls.distance(paddle_y) < 50 and balls.xcor() < -320:
        #print("Made contacted the ball to paddle")
        balls.bounce_y()

    #Detect paddle right
    if balls.xcor() > 380:
        balls.reset_position()
        score.l_score()

    #Detect paddle left
    if balls.xcor() < -380:
        balls.reset_position()
        score.r_score()

screen.exitonclick()

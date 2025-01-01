from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Welcome to my Snake Game.")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head_segment.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head_segment.xcor() > 290 or snake.head_segment.xcor() < -290 or snake.head_segment.ycor() > 290 or snake.head_segment.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()


    """for segment in snake.segments:
        if segment == snake.head_segment:
            pass
        elif snake.head_segment.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()"""

    for segment in snake.segments[1:]:
        if snake.head_segment.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()


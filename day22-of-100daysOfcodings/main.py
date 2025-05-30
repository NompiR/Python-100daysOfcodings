import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboards


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboards()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision cars to the turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    #Detect successful crossing

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

        scoreboard.increase_level()






screen.exitonclick()

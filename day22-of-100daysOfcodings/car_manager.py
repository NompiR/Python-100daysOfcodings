from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green','blue','purple','brown']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:


    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE #car Speed is a self var
        #super().__init__()


    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2) #stretch width 2 is two time equal to 20pixels , stretch len is 1 time orginal length
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT

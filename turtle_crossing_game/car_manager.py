from turtle import Turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLOR))
            car.penup()
            car.shapesize(1, 2)
            car.goto(350, random.randint(-200, 200))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

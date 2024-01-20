from turtle import Screen
from scoreboard import Scoreboard
from gamer import Gamer
from car_manager import CarManager
import time
FINISH_LINE = 200

screen = Screen()
screen.setup(700, 500)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

screen.update()
score = Scoreboard()
gamer = Gamer()
car_manager = CarManager()

screen.onkey(gamer.move, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()
    # Detect move to next level
    if gamer.ycor() > FINISH_LINE:
        score.rise_level()
        gamer.reset_start_position()
        car_manager.level_up()
    # Detect collision in car
    for car in car_manager.all_cars:
        if car.distance(gamer) < 23:
            score.game_over()
            is_game_on = False

screen.exitonclick()

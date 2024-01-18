from turtle import Turtle, Screen
from random import randint, choice

is_race_on = False
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
racers = []
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:")

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_position[turtle_index])
    racers.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 220:
            turtle_color = turtle.pencolor()
            if turtle_color == user_bet:
                print("You win!")
            else:
                print("You lose")
            print(f"Turtle {turtle_color} won the race")
            is_race_on = False
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

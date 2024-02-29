from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

MOVE_SPEED = 0.7

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.update()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.eat()
        score.rise_score()

    # Detect collision with wall
    if (snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 290
            or snake.head.ycor() < -290):
        is_game_on = False
        score.print_game_over()

    # if head collide with any segment in the tail:
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.print_game_over()

screen.exitonclick()

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
START_POSITION = [(-390, 0), (380, 0)]

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)   # update screen
screen.listen()

screen.update()
score = Scoreboard()
left_paddle = Paddle(START_POSITION[0])
right_paddle = Paddle(START_POSITION[1])
ball = Ball()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detect collision in paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 370 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -370):
        ball.bounce_x()
        ball.rise_speed_ball()

    # Detect increase points
    if ball.xcor() > 380:
        ball.restart_position()
        score.left_point()
    if ball.xcor() < -380:
        ball.restart_position()
        score.right_point()

screen.exitonclick()

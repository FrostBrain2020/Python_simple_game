from turtle import Turtle
START_MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = START_MOVE_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = START_MOVE_SPEED

    def rise_speed_ball(self):
        self.move_speed *= 0.9

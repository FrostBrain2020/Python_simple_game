from turtle import Turtle
STEP = 20
START_POSITION = (0, -230)


class Gamer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(START_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + STEP)

    def reset_start_position(self):
        self.goto(START_POSITION)



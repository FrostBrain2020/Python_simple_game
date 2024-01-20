from turtle import Turtle
STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(3, 0.4)
        self.goto(position)

    def up(self):
        y_cor = self.ycor()
        if y_cor <= 210:
            self.goto(self.xcor(), y_cor + STEP)

    def down(self):
        y_cor = self.ycor()
        if y_cor >= -200:
            self.goto(self.xcor(), y_cor - STEP)

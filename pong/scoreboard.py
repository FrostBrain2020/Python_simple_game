from turtle import Turtle
DOWN = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write_score()

    def create_center_line(self):
        self.speed("fastest")
        self.pensize(2)
        self.goto(0, 250)
        self.setheading(DOWN)
        for step in range(17):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def write_score(self):
        self.clear()
        self.create_center_line()
        self.goto(-80, 180)
        self.write(self.left_score, False, "center", ("Arial", 40, "normal"))
        self.goto(80, 180)
        self.write(self.right_score, False, "center", ("Arial", 40, "normal"))

    def left_point(self):
        self.left_score += 1
        self.write_score()

    def right_point(self):
        self.right_score += 1
        self.write_score()

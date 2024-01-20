from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))

    def rise_score(self):
        self.score += 1
        self.write_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", False, "center", ("Arial", 20, "normal"))


from turtle import Turtle
FONT = ("Arial", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(-270, 200)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def rise_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.write_level()
        self.goto(0, 0)
        self.write("Game over!", False, "center", FONT)

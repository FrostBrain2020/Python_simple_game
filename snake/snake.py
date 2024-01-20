from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        snake = self.snake_body
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = snake[segment - 1].xcor()
            new_y = snake[segment - 1].ycor()
            snake[segment].goto(new_x, new_y)
            self.head.forward(MOVE_STEP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("chartreuse4")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def eat(self):
        self.add_segment(self.snake_body[-1].position())
import turtle
import pandas
FONT = ("Arial", 7, "normal")


def mark_state(state_name, x, y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x, y)
    state.write(state_name, False, "center", FONT)


def you_win():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.write("You win !!!", False, "center", ("Arial", 40, "normal"))


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_nr = 0
game_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while game_on:
    answer_state = screen.textinput(f"{guessed_nr}/50 States Correct",
                                    "What's another state's name?").title()
    if answer_state in all_states:
        state = data[data.state == answer_state]
        mark_state(answer_state, int(state.x.iloc[0]), int(state.y.iloc[0]))
        guessed_nr += 1
    elif guessed_nr == 50:
        you_win()
        game_on = False
    elif answer_state == "Exit":
        break

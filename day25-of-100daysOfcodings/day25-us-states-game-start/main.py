import turtle
import pandas as pd


screen = turtle.Screen()

screen.title("U.S. State Game")
screen.window_width()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:

    answer_states = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} state correct",
                                     prompt="What's another state's name?").title()

    if answer_states == "Exit":
        #missing_states = []
        missing_states = [state for state in all_states if state not in guessed_states]
        """for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)"""
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("State_to_learn.csv")
        break

    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(), state_data.y.item())
        #t.write(state_data.state.item())
        t.write(answer_states)


"""
data_coor = data[data["state"] == answer_states]


if answer_states in str(data["state"]):
    set_x = data_coor["x"].item()
    set_y = data_coor["y"].item()

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.position()
    t.setx(set_x)
    t.sety(set_y)
    t.write(answer_states)
else:
    while answer_states not in str(data["state"]):
        answer_states = screen.textinput(title="Guess the state", prompt="What's another state's name?")

"""

"""def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""


screen.exitonclick()

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "image.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

is_on = True
guessed_state = []
number = 0

while len(guessed_state) < 50 and is_on:
    answer_state = screen.textinput(title=f"{number}/50 State Correct", prompt="What's another State name?").title()
    if answer_state in all_states:
        guessed_state.append(answer_state)
        number += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        is_on = False







screen.exitonclick() 
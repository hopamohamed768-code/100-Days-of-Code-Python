import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State's name?")

    guessed_state = answer_state.title()

    if guessed_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if guessed_state in all_states:
        guessed_states.append(guessed_state)
        state_data = data[data.state == guessed_state]
        x_coor = int(state_data.x.item())
        y_coor = int(state_data.y.item())

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coor, y_coor)
        t.write(guessed_state)


# States to learn.csv

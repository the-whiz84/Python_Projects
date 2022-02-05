from turtle import Turtle, Screen
import pandas

IMAGE = "./blank_states_img.gif"
FONT = ("Arial", 8, "normal")

# Enlarged GIF from about 800x500 to 1200x900 for better visibility
screen = Screen()
turtle = Turtle()

# screen.addshape(IMAGE)
screen.title("US States Game")
screen.setup(1300, 900)
screen.bgpic(IMAGE)
turtle.hideturtle()
turtle.penup()
turtle.color("black")

# The way the coordinates were added to the csv file is using this function to gather the x and y values from the mouse click
# Changed all coordinates in the csv file to match the new turtle screen size 1300x900

# def get_mouse_coord(x, y):
#     print(x, y)

# screen.onscreenclick(get_mouse_coord)

# screen.mainloop()
data = pandas.read_csv("./50_states.csv")
states_list = data["state"].to_list()


guessed_states = []
# states_to_learn = []
x_position = 0
y_position = 0

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's a state's name?")
    answer_state = answer.title()

    if answer_state == "Exit":
    #     for state_name in states_list:
    #         if state_name not in guessed_states:
    #             states_to_learn.append(state_name)
    # Alternative way using Day 26 lesson, List Comprehension
        states_to_learn = [name for name in states_list if name not in guessed_states]
        output = pandas.DataFrame(states_to_learn)
        output.to_csv("./states_to_learn.csv")
        break
    
    if answer_state in states_list:
        guessed_states.append(answer_state)
        x_position = int(data[data.state == answer_state].x)
        y_position = int(data[data.state == answer_state].y)
        turtle.goto(x_position, y_position)
        turtle.write(f"{answer_state}", align="left", font=FONT)

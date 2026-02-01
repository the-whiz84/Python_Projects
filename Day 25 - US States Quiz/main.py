import turtle, pandas
from quiz_game import QuizGame

screen =  turtle.Screen()
screen.setup(width=800, height=600)
screen.title("US States Quiz")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
quiz = QuizGame()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
	answer_data = screen.textinput(title=f"{quiz.score}/50 States Guessed", prompt="What's another state's name? ").title()
	if answer_data == "Exit":
		# states_to_learn = []
		# for state in states:
		# 	if state not in guessed_states:
		# 		states_to_learn.append(state)
		# Updated using Day 26 List Comprehension
		states_to_learn = [state for state in all_states if state not in guessed_states]
		pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
		break
	if answer_data in all_states:
		guessed_state = data[data["state"] == answer_data]
		state_xcor = int(guessed_state["x"].item())
		state_ycor = int(guessed_state["y"].item())
		quiz.add_state(answer_data, state_xcor, state_ycor)
		guessed_states.append(answer_data)
		quiz.increase_score()

# How thw x,y coordinates were added to csv for each state:
# def get_mouse_coord(x, y):
# 	print(x, y)
#
# turtle.onscreenclick(get_mouse_coord)
# turtle.mainloop()

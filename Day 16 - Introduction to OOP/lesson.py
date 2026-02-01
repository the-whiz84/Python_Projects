# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("SeaGreen")
# timmy.forward(100)
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", column=["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", column=["Electric", "Water", "Fire"])
table.align = ("l")

print(table)
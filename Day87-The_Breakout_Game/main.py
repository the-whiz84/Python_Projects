# main.py
from game import Game
from menu import Menu


def start_game():
    game = Game()
    game.run()


if __name__ == "__main__":
    menu = Menu(start_game)
    menu.run()

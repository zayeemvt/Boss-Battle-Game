"""
bbg_main.py

The main file for Boss Battle Game. Run this to play the game.
"""

from io_handler import *
from game_handler import GameHandler

if __name__ == '__main__':
    io = IOHandler()
    game = GameHandler()
    while True:
        instruction = io.getInput()

        game.playGame(instruction)
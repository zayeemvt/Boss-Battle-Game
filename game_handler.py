"""
game_handler.py

Handles all of the top-level game functions and bridges game interface with UI.
"""

from Fighters.player import *
from Fighters.enemy import *

class GameHandler:
    def __init__(self):
        self.state = 'setup'
        gameSetup = GameSetup()
        gameBattle = GameBattle()
        gameResults = GameResults()
        self.fsm = {
            'setup':gameSetup,
            'battle':gameBattle,
            'results':gameResults
        }
        self.players = []

    def playGame(self, instruction):
        self.state, self.players = self.fsm[self.state].process(instruction, self.players)


class GameSetup:
    def __init__(self):
        pass

    def process(self, instruction, players):
        state = 'setup'

        command = instruction[0]
        payload = instruction[1]

        if (command == "argNumLow"):
            print('Insufficient number of arguments')
        elif (command == "newPlayer"):
            players.append(Player(payload[0], payload[1], payload[2]))
            print("New character created")
        elif (command == "savePlayerInfo"):
            state = 'battle'
            print("Character data saved")

        return state, players

class GameBattle:
    def __init__(self):
        pass

    def process(self, instruction, players):
        while(players[0].curHP > 0 and players[1].curHP > 0):
            players[0].attack(players[1])
            if(players[1].curHP > 0):
                players[1].attack(players[0])
            print(players[0])
            print(players[1])

        state = 'results'
        return state, players

class GameResults:
    def __init__(self):
        pass

    def process(self, instruction, players):
        print("Finished!")
        return 'results', players
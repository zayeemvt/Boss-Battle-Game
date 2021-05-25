"""
bbg_main.py

The main file for Boss Battle Game. Run this to play the game.
"""

from Fighters.player import *
from Fighters.enemy import *

if __name__ == '__main__':
    print("Hello, world!")
    myFighters = {'Player1':Player('Test'),'Player2':Player('Catch')}
    print(myFighters['Player1'])
    print(myFighters['Player2'])
    while(myFighters['Player2'].curHP > 0):
        myFighters['Player1'].attack(myFighters['Player2'])
        print(myFighters['Player1'])
        print(myFighters['Player2'])

    print(Warrior())
    print(Mage())
    print(Knight())
    print(Cleric())
    print(Thief())
    
    
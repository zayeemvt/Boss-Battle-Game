"""
bbg_main.py

The main file for Boss Battle Game. Run this to play the game.
"""

from Fighters.player import *
from Fighters.enemy import *

if __name__ == '__main__':
    print("Hello, world!")
    classSelect = ClassManager()
    myFighters = [Player('Test', classSelect.classes['Mage'], classSelect.classes['Thief']),
                    Player('Catch', classSelect.classes['Warrior'], classSelect.classes['Knight'])]
    print(myFighters[0])
    print(myFighters[0].calcStats)
    print(myFighters[1])
    print(myFighters[1].calcStats)
    while(myFighters[0].curHP > 0 and myFighters[1].curHP > 0):
        myFighters[0].attack(myFighters[1])
        if(myFighters[1].curHP > 0):
            myFighters[1].attack(myFighters[0])
        print(myFighters[0])
        print(myFighters[1])

    # print(Warrior())
    # print(Mage())
    # print(Knight())
    # print(Cleric())
    # print(Thief())
    
    
from .base import *
from .player_class import *

class Player(Combatant):
    def __init__(self, name, jobclass = Warrior(), subclass = Warrior()):
        self.playerBase = { # TO-DO
            'HP':1500,
            'STR':120,
            'MAG':120,
            'DEF':50,
            'RES':50,
            'SPD':80
        }
        super().__init__(name, self.playerBase)
        self.jobclass = jobclass
        self.subclass = subclass
        self.numSkills = 5 # TO-DO
        self.skills = None
        self.statPoints = {
            'HP':0,
            'STR':0,
            'MAG':0,
            'DEF':0,
            'RES':0,
            'SPD':0
        }
        HP = self.playerBase['HP'] * self.jobclass.getHPmod() * self.subclass.getHPsubmod()
        self.calcStats = self.baseStats # TO-DO

    def __str__(self):
        string = "Name: " + self.name + '\n' + "HP: " + str(self.curHP) + '/' + str(self.calcStats["HP"])
        return string + '\n'
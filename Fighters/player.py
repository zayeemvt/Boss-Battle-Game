from .base import Combatant

class Player(Combatant):
    def __init__(self, name, jobclass = "Freelancer", subclass = "Freelancer"):
        self.playerBase = { # TO-DO
            'HP':100,
            'MP':20,
            'STR':15,
            'MAG':15,
            'DEF':7,
            'RES':7,
            'SPD':10
        }
        super().__init__(name, self.playerBase)
        self.jobclass = jobclass
        self.subclass = subclass
        self.numSkills = 5 # TO-DO
        self.skills = None
        self.statPoints = {
            'HP':0,
            'MP':0,
            'STR':0,
            'MAG':0,
            'DEF':0,
            'RES':0,
            'SPD':0
        }
        self.calcStats = self.baseStats # TO-DO

    def __str__(self):
        string = {
            'Name':self.name,
            'Stats':self.baseStats,
            'Class':self.jobclass,
            'Sub-Class':self.subclass
        }
        return str(string)
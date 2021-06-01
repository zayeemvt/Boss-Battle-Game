from .base import *
from .player_class import *
from math import floor

class Player(Combatant):
    def __init__(self, name, jobclass = 'warrior', subclass = 'warrior'):
        self.playerBase = {
            'HP':1500,
            'STR':120,
            'MAG':120,
            'DEF':50,
            'RES':50,
            'SPD':80
        }
        super().__init__(name, self.playerBase)
        self.statPoints = {
            'HP':0,
            'STR':0,
            'MAG':0,
            'DEF':0,
            'RES':0,
            'SPD':0
        }
        self.jobclass = None
        self.subclass = None
        self.setJobClass(jobclass)
        self.setSubClass(subclass)
        if self.jobclass == None:
            self.setJobClass('warrior')
        if self.subclass == None:
            self.setSubClass('warrior')
        self.recalculateStats()
        self.curHP = self.calcStats['HP']

        self.numSkills = 5 # TO-DO
        self.skills = None

    def __str__(self):
        string = "Name: " + self.name + '\n' + "HP: " + str(self.curHP) + '/' + str(self.calcStats["HP"])
        return string + '\n'

    def recalculateStats(self):
        HP = floor((self.playerBase['HP'] + self.statPoints['HP']*150) * (1 + self.jobclass.getHPmod() + self.subclass.getHPsubmod()))
        STR = floor((self.playerBase['STR'] + self.statPoints['STR']*15) * (1 + self.jobclass.getSTRmod() + self.subclass.getSTRsubmod()))
        MAG = floor((self.playerBase['MAG'] + self.statPoints['MAG']*15) * (1 + self.jobclass.getMAGmod() + self.subclass.getMAGsubmod()))
        DEF = floor((self.playerBase['DEF'] + self.statPoints['DEF']*15) * (1 + self.jobclass.getDEFmod() + self.subclass.getDEFsubmod()))
        RES = floor((self.playerBase['RES'] + self.statPoints['RES']*15) * (1 + self.jobclass.getRESmod() + self.subclass.getRESsubmod()))
        SPD = floor((self.playerBase['SPD'] + self.statPoints['SPD']*15) * (1 + self.jobclass.getSPDmod() + self.subclass.getSPDsubmod()))
        self.calcStats = {'HP':HP, 'STR':STR, 'MAG':MAG, 'DEF':DEF, 'RES':RES, 'SPD':SPD}

    def setJobClass(self, newclass):
        if newclass.lower() in PLAYER_CLASSES:
            self.jobclass = PLAYER_CLASSES[newclass.lower()]
            if (self.subclass != None):
                self.recalculateStats()
            return True
        else:
            print("Main class not found")
            return False

    def setSubClass(self, newclass):
        if newclass.lower() in PLAYER_CLASSES:
            self.subclass = PLAYER_CLASSES[newclass.lower()]
            self.recalculateStats()
            return True
        else:
            print("Sub class not found")
            return False

    def updateName(self, newname):
        self.name = str(newname)

    def setStatPoints(self, statPoints):
        self.statPoints['HP'] = statPoints[0]
        self.statPoints['STR'] = statPoints[1]
        self.statPoints['MAG'] = statPoints[2]
        self.statPoints['DEF'] = statPoints[3]
        self.statPoints['RES'] = statPoints[4]
        self.statPoints['SPD'] = statPoints[5]
        self.recalculateStats()
        return True

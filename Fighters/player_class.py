class PlayerClass():
    def __init__(self, name, statModifiers, subClassMods, skills):
        self.name = name
        self.statModifiers = statModifiers
        self.subClassMods = subClassMods
        self.skills = skills

    def getHPmod(self):
        return self.statModifiers['HP']

    def getSTRmod(self):
        return self.statModifiers['STR']

    def getMAGmod(self):
        return self.statModifiers['MAG']

    def getDEFmod(self):
        return self.statModifiers['DEF']

    def getRESmod(self):
        return self.statModifiers['RES']

    def getSPDmod(self):
        return self.statModifiers['SPD']

    def getHPsubmod(self):
        return self.subClassMods['HP']

    def getSTRsubmod(self):
        return self.subClassMods['STR']

    def getMAGsubmod(self):
        return self.subClassMods['MAG']

    def getDEFsubmod(self):
        return self.subClassMods['DEF']

    def getRESsubmod(self):
        return self.subClassMods['RES']

    def getSPDsubmod(self):
        return self.subClassMods['SPD']

    def __str__(self):
        string = "Name: " + str(self.name) + '\n' + \
                 "HP: " + str(self.getHPmod()) + ' ' + str(self.getHPsubmod()) + '\n' + \
                 "STR: " + str(self.getSTRmod()) + ' ' + str(self.getSTRsubmod()) + '\n' + \
                 "MAG: " + str(self.getMAGmod()) + ' ' + str(self.getMAGsubmod()) + '\n' + \
                 "DEF: " + str(self.getDEFmod()) + ' ' + str(self.getDEFsubmod()) + '\n' + \
                 "RES: " + str(self.getRESmod()) + ' ' + str(self.getRESsubmod()) + '\n' + \
                 "SPD: " + str(self.getSPDmod()) + ' ' + str(self.getSPDsubmod()) + '\n'

        return string

class Warrior(PlayerClass):
    def __init__(self):
        self.name = "Warrior"
        self.statModifiers = {
            'HP':1.33,
            'STR':2.00,
            'MAG':0.60,
            'DEF':1.00,
            'RES':0.75,
            'SPD':1.66
        }
        self.subClassMods = {
            'HP':0.44,
            'STR':0.66,
            'MAG':0.20,
            'DEF':0.33,
            'RES':0.25,
            'SPD':0.55
        }
        self.skills = {}
        super().__init__(self.name, self.statModifiers, self.subClassMods, self.skills)

class Mage(PlayerClass):
    def __init__(self):
        self.name = "Mage"
        self.statModifiers = {
            'HP':1.00,
            'STR':0.60,
            'MAG':2.00,
            'DEF':0.75,
            'RES':1.66,
            'SPD':1.33
        }
        self.subClassMods = {
            'HP':0.33,
            'STR':0.20,
            'MAG':0.66,
            'DEF':0.25,
            'RES':0.55,
            'SPD':0.44
        }
        self.skills = {}
        super().__init__(self.name, self.statModifiers, self.subClassMods, self.skills)

class Knight(PlayerClass):
    def __init__(self):
        self.name = "Knight"
        self.statModifiers = {
            'HP':1.66,
            'STR':1.00,
            'MAG':0.75,
            'DEF':2.00,
            'RES':1.33,
            'SPD':0.60
        }
        self.subClassMods = {
            'HP':0.55,
            'STR':0.33,
            'MAG':0.25,
            'DEF':0.66,
            'RES':0.44,
            'SPD':0.20
        }
        self.skills = {}
        super().__init__(self.name, self.statModifiers, self.subClassMods, self.skills)

class Cleric(PlayerClass):
    def __init__(self):
        self.name = "Cleric"
        self.statModifiers = {
            'HP':0.60,
            'STR':0.75,
            'MAG':1.33,
            'DEF':1.66,
            'RES':2.00,
            'SPD':1.00
        }
        self.subClassMods = {
            'HP':0.20,
            'STR':0.25,
            'MAG':0.44,
            'DEF':0.55,
            'RES':0.66,
            'SPD':0.33
        }
        self.skills = {}
        super().__init__(self.name, self.statModifiers, self.subClassMods, self.skills)

class Thief(PlayerClass):
    def __init__(self):
        self.name = "Thief"
        self.statModifiers = {
            'HP':0.75,
            'STR':1.33,
            'MAG':1.66,
            'DEF':0.60,
            'RES':1.00,
            'SPD':2.00
        }
        self.subClassMods = {
            'HP':0.25,
            'STR':0.44,
            'MAG':0.55,
            'DEF':0.20,
            'RES':0.33,
            'SPD':0.66
        }
        self.skills = {}
        super().__init__(self.name, self.statModifiers, self.subClassMods, self.skills)

class ClassManager():
    def __init__(self):
        self.classes = {'Warrior':Warrior(), 'Mage':Mage(), 'Knight':Knight(), 'Cleric':Cleric(), 'Thief':Thief()}
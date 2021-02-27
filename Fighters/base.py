class Combatant:
    def __init__(self, name, base):
        self.name = name
        self.curHP = base['HP']
        self.curMP = base['MP']
        self.baseStats = base #HP, MP, STR, MAG, DEF, RES, SPD
        self.calcStats = self.baseStats
        self.modifiers = None
        self.effects = None
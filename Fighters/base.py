class Combatant:
    def __init__(self, name, base):
        self.name = name
        self.curHP = base['HP']
        self.baseStats = base #HP, STR, MAG, DEF, RES, SPD
        self.calcStats = self.baseStats
        self.modifiers = None # Stat modifiers (buffs and debuffs)
        self.effects = None # Status effects

    def attack(self, target):
        damage = self.calcStats['STR'] - target.calcStats['DEF']
        if damage < 0:
            damage = 0
        target.curHP = target.curHP - damage
        if target.curHP < 0:
            target.curHP = 0
         
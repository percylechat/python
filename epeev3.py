import random
import copy
from typing import List

class Weapon():
    def __init__(self, crit : list, touch : int, name : str):
        self.crit = crit
        self.touch = touch
        self.name = name
    def get_critique(self) -> list:
        return self.crit
    def get_touch(self):
        return self.touch

class Massue(Weapon):
    def __init__(self, crit : list = [20], touch : int = 9, name = "Massue"):
        Weapon.__init__(self, crit, touch, name)
    def degat(self) -> int :
        d1 = random.randint(1, 10)
        deg1 = d1 + 6
        return deg1

class Epee(Weapon):
    def __init__(self, crit : list = [19,20], touch : int = 6, name = "Epee"):
        Weapon.__init__(self, crit, touch, name)
    def degat(self) -> int :
        d1 = random.randint(1, 8)
        d2 = random.randint(1, 8)
        deg1 = d1 + d2 + 5
        return deg1

class Enemy():
    def __init__(self, pv : int, turn : int = 0,name : str=  "ennemy"):
        self.pv = pv
        self.turn = turn
        self.name = name
    def __str__(self):
        return "name : "+self.name + " pv:" + str(self.pv) + " turn :"+str(self.turn)
    def __repr__(self):
        return "name : "+self.name + " pv:" + str(self.pv) + " turn :"+str(self.turn)

class Engine():
    def __init__(self, touch : int = 15):
        self.touch = touch
    def arena(self, fighters : List[Enemy], to_comp : List[Weapon]):
        result = []
        print("list ennemy")
        print(fighters )
        for weapon in to_comp:
            for fighter1 in fighters:
                print("fighter from list")
                print(fighter1)
                fighter : Enemy = copy.deepcopy(fighter1)
                print("fighter from copy")
                print(fighter)
                result_weapon = {}
                while fighter.pv > 0:
                    fighter = engine.tour(weapon, fighter)
                result_weapon[weapon.name+":"+fighter.name] = fighter
                result.append(result_weapon)
        return result
    def attack(self, deg : int, enemy : Enemy):
        enemy.turn += 1
        if deg >= enemy.pv:
            print("The "+enemy.name+" died!")
            print("It took", str(enemy.turn), "turns")
            enemy.pv = 0
        else:
            print("The "+enemy.name+" has been hit for", str(deg), "damages")
            enemy.pv = enemy.pv - deg
        return enemy
    def tour(self, weapon : Weapon, enemy : Enemy) ->int:
        d1 = random.randint(1, 20)
        if d1 in weapon.get_critique():
            res = weapon.degat() * 2
            print("Critique " + weapon.name)
            return self.attack(res, enemy)
        if d1 + weapon.get_touch() >= self.touch:
            res = weapon.degat()
            print("Touché " + weapon.name)
            return self.attack(res, enemy)
        else:
            print("Fail " + weapon.name)
            return enemy

if __name__ == '__main__':
    engine = Engine()
    sword = Epee([19, 20], 6)
    masse = Massue(touch=9)
    l_weapon = [masse,sword]
    goblin = Enemy(30,name="goblin")
    orc = Enemy(60,name="orc")
    l_foes = [goblin,orc]
    print(engine.arena(l_foes, l_weapon))
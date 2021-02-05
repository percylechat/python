import random

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

class Engine():
    def __init__(self, touch : int = 15):
        self.touch = touch
    def tour(self, weapon : Weapon) ->int:
        d1 = random.randint(1, 20)
        if d1 in weapon.get_critique():
            print("Critique " + weapon.name)
            return weapon.degat() * 2
        if d1 + weapon.get_touch() >= self.touch:
            print("Touché " + weapon.name)
            return weapon.degat()
        else:
            print("Fail " + weapon.name)
            return 0

if __name__ == '__main__':
    engine = Engine()
    sword = Epee([19, 20], 6)
    masse = Massue(touch=9)
    print(engine.tour(sword))
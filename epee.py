import random

class Weapon():
    def __init__(self, crit : list, touch : int):
        self.crit = crit
        self.touch = touch
    def get_critique(self, crit) -> list:
        return self.crit
    def get_touch(self, touch):
        return self.touch

class Massue(Weapon):
    def __init__(self, crit : int, touch : int):
        Weapon.__init__(self, crit, touch)
    def degat(self) -> int :
        d1 = random.randint(1, 10)
        deg1 = d1 + 6
        return deg1

class Epee(Weapon):
    def __init__(self, crit : int, touch : int):
        Weapon.__init__(self, crit, touch)
    def degat(self) -> int :
        d1 = random.randint(1, 8)
        d2 = random.randint(1, 8)
        deg1 = d1 + d2 + 5
        return deg1

class Engine():
    def __init(self, touch : int = 15):
        self.touch = touch
    def tour(self, weapon : Weapon) ->int:
        d1 = random.randint(1, 20)
        if d1 in weapon.get_critique():
            return weapon.degat() * 2
        if d1 + weapon.get_touch() >= self.touch:
            return weapon.degat()
        else:
            return 0

"""
1d20 + 9
si 20 20 deg
1s10 + 6 

1d20 + 6
si 20 20 ou 19 deg
2d8 + 5

ajout 3 monstres, 10, 50 100
voir cmb de tour pour tuer chacun avec chaque arme
"""
i1 = 100
i2 = 100


def jet(pv : int = 100):
    touch1 = 0
    touch2 = 0
    deg1 = 0
    deg2 = 0
    crit2 = 0
    end1 = 0
    end2 = 0
    i1 = pv
    i2 = pv
    t1 = random.randint(1, 20)
    if (t1 + 9) >= 15:
        touch1 += 1
        d1 = random.randint(1, 10)
        if t1 == 20:
            crit1 += 1
            deg1 += (d1 + 6) * 2
        else:
            deg1 += d1 + 6
        i1 -= deg1
        if i1 > 0:
            end1 += 1
    if t1 + 6 >= 15:
        touch2 += 1
        d2 = random.randint(1, 8)
        d3 = random.randint(1, 8)
        if t1 == 20 or t1 == 19:
            crit2 += 1
            deg2 += (d2 + d3 + 5) * 2
        else:
            deg2 += d2 + d3 + 5
        i2 -= deg2
        if i2 > 0:
            end2 += 1
    tab: list = [touch1, deg1, end1, touch2, deg2, end2]

while i1 > 0 and i2 > 0:
    

end1 += 1
end2 += 1
print("la massue a tue l ennemi en",str(end1) , "tours")
print("l'epee' a tue l ennemi en",str(end2) , "tours")
"""print("La massue a touché" , str(touch1), "soit", str(touch1/100000 * 100), "pourcent du temps")
print("Elle a fait en moyenne" , str(deg1 / touch1) ,"par attaque")
print("Elle a fait en moyenne" , str(deg1 / 100000), "par tour")
print("Elle a fait", str(crit1), "critiques")
print("L'épée' a touché" , str(touch2), "soit", str(touch2/100000 * 100), "pourcent du temps")
print("Elle a fait en moyenne" , str(deg2 / touch2), "par attaque")
print("Elle a fait en moyenne" , str(deg2 / 100000) ,"par tour")
print("Elle a fait", str(crit2), "critiques")"""
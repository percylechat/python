"""
creer classe humain qui donnera homme femme, possede poid taille ratio
homme
ration 0
 femme
 ratio -10
sous classe appelle imc
"""

class Human:
    def __init__(self, weight : int = 10, size : float = 2.00, ratio : int = 0):
       self.weight = weight
       self.size = size
       self.ratio = ratio
    def calc_imc(self) -> float:
        result : float = (self.weight - self.ratio) / (self.size * self.size)
        return result

class Male(Human):
   def __init__(self, weight : int, size : float, ratio : int):
       self.ratio = 0
       Human.__init__(self, weight, size, ratio)


class Female(Human):
   def __init__(self, weight : int, size : float, ratio : int = 10):
        self.ratio = 10
        Human.__init__(self, weight, size, ratio)

if __name__ == "__main__":
    f = Female(46, 1.63)
    print(f.calc_imc())
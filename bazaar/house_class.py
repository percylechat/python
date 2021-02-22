from typing import List, Dict

"""Contains house name, type of family and list with objects of habitants"""
class House():
    def __init__(self, name : str, nb_hab : int, habs : list):
        self.nb_hab = nb_hab
        self.name = name
        self.habs = habs
    def get_nb_hab(self):
        if self.nb_hab == 0:
            return "alone"
        if self.nb_hab == 1:
            return "couple"
        if self.nb_hab == 2:
            return "family with one child"
        if self.nb_hab == 3:
            return "family with two children"
        if self.nb_hab == 4:
            return "brothers / sisters"
    def __str__(self):
        return " last name: " +str(self.name) +" type: "+ self.get_nb_hab() + " habitants: " + str(self.habs)
    def __repr__(self):
        return " last name: " +str(self.name) +" type: "+ self.get_nb_hab() + " habitants: " + str(self.habs)

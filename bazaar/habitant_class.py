from typing import List, Dict

"""Contains full name, sex, age, and global state"""
class Habitant():
    def __init__(self, last_name: str, first_name: str, age: int, age_categ: int, sex :int, status: float, workplace:str, is_dead: bool = False, is_customer:bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.age_categ = age_categ
        self.sex = sex
        self.status = status
        self.is_dead = is_dead
        self.workplace = workplace
        self.is_customer = is_customer
    def get_age_categ(self) ->str:
        if self.age_categ == 0:
            return "is a child"
        elif self.age_categ == 1:
            return "is an adult"
        else:
            return "is a senior"
    def get_sex(self) -> str:
        if self.sex == 1:
            return "Female"
        else:
            return "Male"
    def get_status(self) -> str:
        if self.status < 1:
            return "Exhausted"
        if self.status > 1 and self.status < 2:
            return "Tired"
        if self.status > 2 and self.status < 3:
            return "Fine"
        if self.status > 3:
            return "Well rested"     
    def __str__(self):
        return " last name: " +str(self.last_name) +" first name: " + str(self.first_name) +" age: "+str(self.age) + " sex: " + self.get_sex() + " status: " + self.get_status() + " workplace: " + str(self.workplace)
    def __repr__(self):
        return " last name: " +str(self.last_name) +" first name: " + str(self.first_name) +" age: "+str(self.age) + " sex: " + self.get_sex() + " status: " + self.get_status()+ " workplace: " + str(self.workplace)

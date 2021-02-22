from typing import List, Dict

"""Contains full name, sex, age, and global state"""
class Habitant():
    def __init__(self, last_name : str, first_name : str, age : int, sex : int, status : float, is_customer:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.status = status
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
        return " last name: " +str(self.last_name) +" age: "+str(self.age) + " sex: " + self.get_sex() + " first name: " + str(self.first_name) + " status: " + self.get_status()
    def __repr__(self):
        return " last name: " +str(self.last_name) +" age: "+str(self.age) + " sex: " + self.get_sex() + " first name: " + str(self.first_name) + " status: " + self.get_status()

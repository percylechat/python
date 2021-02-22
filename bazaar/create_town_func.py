import random
import csv
from typing import List, Dict
from house_class import House
from habitant_class import Habitant
from sql_generation_func import *

def generate_citizen(l_name : str, sex : int, child : int = 0) -> Habitant:
    a = random.randint(18, 80)
    if child == 1:
        a = random.randint(0, 18)
    stat = random.uniform(0, 4)
    if sex == 0:
        file_name= "name_bazaar_male.csv"
    else:
        file_name= "name_bazaar_female.csv"
    input_file = csv.DictReader(open(file_name))
    list_dict : List = list(input_file)
    f_name : str = list_dict[random.randint(0,len(list_dict)-1)]["first_name"] 
    return Habitant(l_name, f_name, a, sex, stat, 0)
        
def generate_house(h_name, h_type, habs):
    return House(h_name, h_type, habs)
    
def generate_town(nb_house : int) ->list :
    l_houses = []
    input_file = csv.DictReader(open('name_bazaar.csv'))
    list_dict : List = list(input_file)
    for i in range (len(list_dict)):
        if i < nb_house:
            l_habitants = []
            h_name : str = list_dict[i]["last_name"]
            h_type : int = random.randint(0, 4)
            sex : int = random.randint(0, 1)
            if h_type == 0:
                l_habitants.append(generate_citizen(h_name, sex))
            elif h_type == 1:
                l_habitants.append(generate_citizen(h_name, sex = 0))
                l_habitants.append(generate_citizen(h_name, sex = 1))
            elif h_type == 2:
                l_habitants.append(generate_citizen(h_name, sex = 0))
                l_habitants.append(generate_citizen(h_name, sex = 1))
                l_habitants.append(generate_citizen(h_name, sex, 1))
            elif h_type == 3:
                l_habitants.append(generate_citizen(h_name, sex = 0))
                l_habitants.append(generate_citizen(h_name, sex = 1))
                l_habitants.append(generate_citizen(h_name, sex, 1))
                l_habitants.append(generate_citizen(h_name, sex, 1))
            else:
                l_habitants.append(generate_citizen(h_name, sex))
                l_habitants.append(generate_citizen(h_name, sex))
            l_houses.append(generate_house(h_name, h_type, l_habitants))
            i += 1
    return l_houses

def generate_relationships(l_houses : List, conn):
    family: bool = True
    for house in l_houses:
        l_name: str= house.name
        if house.nb_hab == 4:
            base: int = 25
            love: bool = False
            f_name1: str = house.habs[0].first_name
            f_name2: str = house.habs[1].first_name
            create_relationship(conn, l_name,l_name,f_name1,f_name2,family,love,base + random.randint(-50, 50))
            create_relationship(conn, l_name,l_name,f_name2,f_name1,family,love,base + random.randint(-50, 50))
        elif house.nb_hab == 0:
            pass
        elif house.nb_hab == 1:
            base: int = 50
            love: bool = True
            f_name1: str = house.habs[0].first_name
            f_name2: str = house.habs[1].first_name
            create_relationship(conn, l_name,l_name,f_name1,f_name2,family,love,base + random.randint(-50, 50))
            create_relationship(conn, l_name,l_name,f_name2,f_name1,family,love,base + random.randint(-50, 50))
        else:
            base: int = 50
            for i in house.habs:
                for j in house.habs:
                    if i != j:
                        if i.age > 18 and j.age > 18:
                            create_relationship(conn, l_name,l_name,i.first_name,j.first_name,family,True,base + random.randint(-50, 50))
                        else:
                            create_relationship(conn, l_name,l_name,i.first_name,j.first_name,family,False,base + random.randint(-50, 50))
    return conn
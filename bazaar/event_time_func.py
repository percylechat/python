import random
from typing import List, Dict
from habitant_class import Habitant
from house_class import House
from sql_generation_func import *

def meet_someone(people : List, conn):
    for someone in people:
        new = random.randint(0, len(people) - 1)
        if someone.last_name is people[new].last_name and someone.first_name is people[new].first_name:
            return
        if check_relationship(conn, someone.last_name, people[new].last_name, someone.first_name, people[new].first_name) == 1:
            return
        else:
            pos = random.randint(0, 1)
            # print(someone.last_name, people[new].last_name, someone.first_name, people[new].first_name, check_relationship(someone.last_name, people[new].last_name, someone.first_name, people[new].first_name))
            if pos == 1:
                rel = 30
            else:
                rel = -30
            create_relationship(conn, someone.last_name, people[new].last_name, someone.first_name, people[new].first_name, 0, 0, rel)
            create_relationship(conn, people[new].last_name, someone.last_name, people[new].first_name, someone.first_name, 0, 0, rel)

def school_day(students : List, conn):
    skip_school = []
    at_school = []
    for child in students:
        skipped = random.randint(0, 100)
        if skipped < 5:
            skip_school.append(child)
        else:
            at_school.append(child)
    for child in at_school:
        meet_someone(at_school, conn)

def work_day(workers : List, conn):
    print(workers)
    for people in workers:
        meet_someone(workers, conn)

def day_status(town : List, conn):
    school = []
    work = []
    for house in town:
        for hab in house.habs:
            hab.status += random.randint(-1, 1)
            if hab.age < 18:
                school.append(hab)
            else:
                work.append(hab)
    for house1 in town:
        for i in house.habs:
                for j in house.habs:
                    if i != j:
                        mod = random.randint(-10, 10)
                        update_relationship(i.last_name, j.last_name, i.first_name, j.first_name, mod)
    work_day(work, conn)
    school_day(school, conn)

def visit_shop(self, habitant : Habitant):
    habitant.is_customer = True
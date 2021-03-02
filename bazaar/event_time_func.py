import random
from typing import List, Dict
from habitant_class import Habitant
from house_class import House
from places_class import *
from shop_func import *
from social_func import *
from relationship_sql_func import *

def school_day(students : List, conn, town):
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

def work_day(workers : List, conn, town):
    sawmill = []
    for people in workers:
        if people.workplace == "Sawmill":
            sawmill.append(people)
        meet_someone(workers, conn)
    workday_sawmill = Sawmill([0, 3], sawmill)
    workday_sawmill.check_accident(conn, town)

def idle_day(people : List, conn, town):
    for someone in people:
        roll = random.randint(0, 100)
        if roll < 10:
            visit_shop(someone)

def lunch_break(customers, conn):
    pass

def what_do_weekday(town : List, conn):
    school = []
    work = []
    idle = []
    lunch = []
    for house in town:
        for hab in house.habs:
            if hab.age_categ == 0:
                school.append(hab)
            elif hab.age_categ == 1:
                work.append(hab)
            else:
                idle.append(hab)
    for someone in work:
        roll = random.randint(0, 100)
        if roll < 33:
            lunch.append(someone)
    for someone in idle:
        roll = random.randint(0, 100)
        if roll < 33:
            lunch.append(someone)
    school_day(school, conn, town)
    work_day(work, conn, town)
    idle_day(idle, conn, town)
    lunch_break(lunch, conn)

def weekday(town : List, conn):
    cemetary = []
    what_do_weekday(town, conn)
    # check death
    for house in town:
        for hab in house.habs:
            if hab.is_dead is True:
                house.habs.remove(hab)
                cemetary.append(hab)
    # check if relatives know of death
    # apply status modification and relationship movements
    for house in town:
        for i in house.habs:
            i.status += random.randint(-1, 1)
            for j in house.habs:
                if i != j:
                    mod = random.randint(-10, 10)
                    update_relationship(i.last_name, j.last_name, i.first_name, j.first_name, mod)
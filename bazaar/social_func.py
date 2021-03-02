from relationship_sql_func import *
import random

def meet_someone(people : List, conn):
    for someone in people:
        new = random.randint(0, len(people) - 1)
        if someone.last_name is people[new].last_name and someone.first_name is people[new].first_name:
            return
        if check_relationship(conn, someone.last_name, people[new].last_name, someone.first_name, people[new].first_name) == 1:
            return
        else:
            pos = random.randint(0, 1)
            if pos == 1:
                rel = 30
            else:
                rel = -30
            create_relationship(conn, someone.last_name, people[new].last_name, someone.first_name, people[new].first_name, 0, 0, rel)
            create_relationship(conn, people[new].last_name, someone.last_name, people[new].first_name, someone.first_name, 0, 0, rel)

def has_been_killed_by(town, conn, victim, killer):
    for family in town:
        if family.name is victim.last_name:
            for hab in family.habs:
                if check_relationship(conn, killer.last_name, hab.last_name, killer.first_name, hab.first_name) == 1:
                    update_relationship(killer.last_name, hab.last_name, killer.first_name, hab.first_name, -100)
                else:
                    create_relationship(conn, killer.last_name, hab.last_name, killer.first_name, hab.first_name, 0, 0, -100)         
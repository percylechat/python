import random
import csv
from typing import List, Dict

from house_class import House
from habitant_class import Habitant

from create_town_func import *
from event_time_func import *

from rumors_sql_func import *
from relationship_sql_func import *
  
if __name__ == '__main__':
    # city generation
    conn = create_database_relationship()
    create_database_known_rumors()
    listy = generate_town(5)
    generate_worplace(listy)
    conn = generate_relationships(listy, conn)
    print(listy)
    #game time
    weekday(listy, conn)
    print(listy)
    # print(listy[0].habs[1].age)

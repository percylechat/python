import random
import csv
from typing import List, Dict

from house_class import House
from habitant_class import Habitant

from create_town_func import *
from sql_generation_func import *
from event_time_func import *

  
if __name__ == '__main__':
    conn = create_database()
    listy = generate_town(2)
    # print(listy)
    conn = generate_relationships(listy, conn)
    day_status(listy, conn)
    # print(listy)
    # print(listy[0].habs[1].age)

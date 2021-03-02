from typing import List, Dict
import random
from rumors_sql_func import *
# from relationship_sql_func import *

class Places():
    def __init__(self, open_hours:list, people:List):
        self.open_hours = open_hours
    def get_open_hours(self):
        if self.open_hours[0] == 0:
            return "Open from 8AM to"
        elif self.open_hours[0] == 1:
            return "Open from 10AM to"
        elif self.open_hours[0] == 2:
            return "Open from noon to"
        elif self.open_hours[0] == 3:
            return "Open from 2PM to"
        elif self.open_hours[0] == 4:
            return "Open from 4PM to"
        else:
            return "Open from 6PM to"
        if self.open_hours[1] == 0:
            return "10AM"
        elif self.open_hours[1] == 1:
            return "noon"
        elif self.open_hours[1] == 2:
            return "2PM"
        elif self.open_hours[1] == 3:
            return "4PM"
        elif self.open_hours[1] == 4:
            return "6PM"
        else:
            return "midnight"

class Sawmill(Places):
    def __init__(self, open_hours, workers : List):
        self.workers = workers
    def accident(self, worker, conn, town):
        lvl = 3
        nature = "murder"
        details = "killed in an accident at the sawmill"
        who = random.randint(0, len(self.workers)- 1)
        print(str(worker.first_name), str(worker.last_name), "provoked an accident!")
        print(str(self.workers[who].first_name), str(self.workers[who].last_name), "died!")
        # kill someone else
        if worker.last_name is not self.workers[who].last_name and worker.first_name is not self.workers[who].first_name: 
            veracity = True            
            for witness in self.workers:
                if self.workers[who].last_name is not witness.last_name and self.workers[who].first_name is not witness.first_name:
                    roll = random.randint(0, 100)
                    if roll < 50:
                        add_rumor(witness.last_name,witness.first_name,witness.last_name,witness.first_name,lvl,nature,details,veracity,worker.last_name,worker.first_name,self.workers[who].last_name,self.workers[who].first_name)
        # kill themselves
        if worker.last_name is self.workers[who].last_name:
            veracity = False
            culprit = random.randint(0, len(self.workers)- 1)
            if self.workers[who].last_name is self.workers[culprit].last_name and self.workers[who].first_name is self.workers[culprit].first_name:
                return
            else:
                for witness in self.workers:
                    if self.workers[who].last_name is not witness.last_name and self.workers[who].first_name is not witness.first_name:
                        roll = random.randint(0, 100)
                        if roll < 50:
                            add_rumor(witness.last_name,witness.first_name,witness.last_name,witness.first_name,lvl,nature,details,veracity,self.workers[culprit].last_name,self.workers[culprit].first_name,worker.last_name,worker.first_name)
        self.workers[who].is_dead = True
    def check_accident(self, conn, town):
        for worker in self.workers:
            acc = random.randint(0, 100)
            if worker.status < 2:
                if acc == 0:
                    self.accident(worker, conn, town)
                    return 
            if worker.status > 2 and worker.status < 3:
                if acc < 10:
                    self.accident(worker, conn, town)
                    return
            else:
                if acc < 30:
                    self.accident(worker, conn, town)
                    return

class School(Places):
    def __init__(self, open_hours = [0, 3]):
        pass
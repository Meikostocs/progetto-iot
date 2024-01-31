import random
import json

class Battery:
    def __init__(self,capacity,level=100):
        if level is not None:
            self.level = level
        else:
            self.level = 100.0
        self.unit     = "%"
        self.capacity = capacity

    def update_measurements(self):
        self.level = self.level - random.uniform(1,5)
        if self.level<1:
            self.level = 0

    def critical_status(self):
        return self.level < 20


    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
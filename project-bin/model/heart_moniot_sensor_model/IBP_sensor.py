import json
import random



class IBP_sensor:

    def __init__(self):
        self.pressure1 = 100
        self.pressure2 = 120

    def update_measurements(self):
        self.pressure1 += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)
        self.pressure2 += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)

        #range -50 - 300
        self.pressure1 = max(-50, min(self.pressure1, 300))
        self.pressure2 = max(-50, min(self.pressure2, 300))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


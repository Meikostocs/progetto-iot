import json
import random



class IBPSensor:

    def __init__(self, pressure1=None, pressure2=None):
        if pressure1 is None:
            self.pressure1 = 100
        else:
            self.pressure1 = pressure1

        if pressure2 is None:
            self.pressure2 = 120
        else:
            self.pressure2 = pressure2

        self.unit="mmHg"

    def update_measurements(self):
        self.pressure1 += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)
        self.pressure2 += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)

        #range -50 - 300
        self.pressure1 = max(-50, min(self.pressure1, 300))
        self.pressure2 = max(-50, min(self.pressure2, 300))

    def critical_status(self):
        if self.pressure1<70 or self.pressure2>220:
            return True
        else:
            return False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


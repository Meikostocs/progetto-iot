import json
import random


class Pressure_avarage_sensor:

    def __init__(self):
        self.pressure = 70

    def update_measurements(self):
        self.pressure += random.uniform(0.0, 5.0) * random.uniform(-1.0,2.0)

        self.pressure = max(40, min(self.pressure, 130))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
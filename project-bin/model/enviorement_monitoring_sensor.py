import json
import random

class Enviorement_monitoring_sensor:

    def __init__(self):
        self.temperature = 22
        self.humidity = 60
        self.PM10=60
        self.battery=80

    def update_measurements(self):
        self.temperature += random.uniform(-1.0, 1.0)
        self.humidity += random.uniform(-1.0, 1.0)
        self.PM10 += random.uniform(-1.0, 1.0)
        self.battery += random.uniform(-1.0, 1.0)

        #Range PM10 0-300
        self.PM10 = max(0,min(self.PM10,300))
        #range battery
        self.battery = max(0, min(self.battery, 100))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

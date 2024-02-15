import json
import random


class PressureAvarageSensor:

    def __init__(self, pressure=None):

        if pressure is None:
            self.pressure = 70
        else:
            self.pressure = pressure

        self.unit="mmHg"
    def update_measurements(self):
        self.pressure += random.uniform(0.0, 5.0) * random.uniform(-1.0,2.0)

        self.pressure = max(40, min(self.pressure, 130))

    def critical_status(self):
        if self.pressure<70 or self.pressure>100:
            return True
        else:
            return False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
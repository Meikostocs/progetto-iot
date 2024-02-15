import json
import random


class NIBPSensor:

    def __init__(self, pressure_diastolic=None, pressure_sistolic=None):

        if pressure_diastolic is None:
            self.pressure_diastolic = 80
        else:
            self.pressure_diastolic = pressure_diastolic

        if pressure_sistolic is None:
            self.pressure_sistolic = 120
        else:
            self.pressure_sistolic = pressure_sistolic

        self.unit="mmHg"

    def update_measurements(self):
        self.pressure_diastolic += random.uniform(0.0, 5.0) * random.uniform(-1.0,2.0)
        self.pressure_sistolic += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)

        #range pd 40-130
        self.pressure_diastolic=max(40,min(self.pressure_diastolic,130))
        # range ps 70-200
        self.pressure_sistolic = max(70, min(self.pressure_sistolic, 200))

    def critical_status(self):
        if self.pressure_diastolic>120 or self.pressure_sistolic>180:
            return True
        else:
            return False


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)




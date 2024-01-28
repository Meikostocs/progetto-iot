import json
import random


class NIBP_sensor:

    def __init__(self):
        self.pressure_diastolic = 80
        self.pressure_sistolic = 120

    def update_measurements(self):
        self.pressure_diastolic += random.uniform(0.0, 5.0) * random.uniform(-1.0,2.0)
        self.pressure_sistolic += random.uniform(0.0, 5.0) * random.uniform(-1.0, 2.0)

        #range pd 40-130
        self.pressure_diastolic=max(40,min(self.pressure_diastolic,130))
        # range ps 70-200
        self.pressure_sistolic = max(70, min(self.pressure_sistolic, 200))


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)




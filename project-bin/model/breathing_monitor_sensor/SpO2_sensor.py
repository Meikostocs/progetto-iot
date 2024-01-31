import json
import random

class SpO2Sensor:


    def __init__(self, measurement=None):
        """
        SpO2 Sensor

        :param measurement: SpO2 (Blood oxygen saturation value).
        :type measurement: float [%]
        """
        if measurement is None:
            self.measurement = random.uniform(95,100)
        else:
            self.measurement = measurement
        self.unit = "%"
    

    def update_measurements(self):
        self.measurement += random.uniform(-5,5)
        if self.measurement > 100:
            self.measurement = 100
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


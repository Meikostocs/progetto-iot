import json
import random

class Co2Sensor:


    def __init__(self, measurement, unit):
        self.measurement = measurement
        self.unit        = unit
    
    def __init__(self, units="mmHg"):
        self.update_mesurements()
        self.units = units


    def update_measurements(self):
        """
        Perform a measurement in mmHg. 
        If current unit of measurements is kPa, mulitply by conversion constant
        """
        self.measurement = random.uniform(35,45)+random.randint(-5,5)
        if (self.units == 'kPa'):
            self.measurement *= 0.133322 
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


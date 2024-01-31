import json
import random

class EtCO2Sensor:

    def __init__(self, concentration=None, pressure=None, mode="Mainstream"):
        """
        End-Tidal CO2. It measures the concentration of CO2 at exhalation end. 

        :param concentration:
        :type concentration: float [mmHg]
        :param pressure
        :type pressure: float [%]
        """
        if concentration is None:
            self.concentration = random.uniform(2,2)
        else:
            self.concentration = concentration
        
        if pressure is None:
            self.pressure = random.uniform(35,45)
        else:
            self.pressure = pressure

    def update_measurements(self):

        self.pressure += random.uniform(-5,5)
        if self.pressure <= 25:
            self.pressure = 25
        elif self.pressure >= 55:
            self.pressure = 55 
        
        self.concentration += random.uniform(-2,2)
        if self.concentration <= 0:
            self.concentration = 0
        elif self.concentration >= 8:
            self.concentration = 8

    def critical_status(self):
        return self.pressure < 35 or self.pressure > 45 or self.concentration < 3 or self.concentration > 5

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

import json
import random

class Co2Sensor:


    def __init__(self, unit="mmHg", measurement=None):
        """
        CO2 Sensor

        :param unit: Unit of measurement
        :type unit: String, ["mmHg" or "kPa"]
        :param measurement: CO2 value.
        :type measurement: float or None
        """
        if measurement is not None:
            self.measurement = measurement
        else:
            self.measurement = random.uniform(35,45)
        
        self.unit = unit


    def update_measurements(self):
        """
        Perform a measurement in mmHg. 
        If current unit of measurements is kPa, mulitply by conversion constant
        """
        self.measurement += random.uniform(-5,5)
        
        if self.measurement<= 25:
            self.measurement = 25
        elif self.measurement >= 55:
            self.measurement = 55 

        if (self.unit == 'kPa'):
            self.measurement *= 0.133322 

        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


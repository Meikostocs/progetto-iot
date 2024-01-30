import json
import random

class Co2Sensor:


    def __init__(self, measurement=None, unit="mmHg"):
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
        # Switch to mmHg unit
        change_unit = False
        if self.unit == 'kPa':
            change_unit = True
            self.to_mmhg()
        
        # Perform update
        self.measurement += random.uniform(-5,5)
        if self.measurement<= 25:
            self.measurement = 25
        elif self.measurement >= 55:
            self.measurement = 55 

        # Restore unit
        if change_unit:
            self.to_kpa()

        
    def to_mmhg(self):
        if self.unit == 'kPa':
            self.unit = "mmHg"
            self.measurement = self.measurement/0.13332236
    
    def to_kpa(self):
        if self.unit == 'mmHg':
            self.unit = "kPa"
            self.measurement = self.measurement*0.13332236

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


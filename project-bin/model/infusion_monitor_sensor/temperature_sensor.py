import json
import random

class TemperatureSensor:


    def __init__(self, measurement=None, unit="C"):
        """
        Temperature Sensor

        :param measurement: SpO2 (Blood oxygen saturation value).
        :type measurement: float [%]
        :param unit: unit of measure
        :type unit: String ["C", "F"]
        """
        if measurement is None:
            self.measurement = random.uniform(36,37)
            if self.unit == "F":
                self.measurement = self.to_fahrenheit()
        else:
            self.measurement = measurement
        self.unit = "%"


    def update_measurements(self):
        
        #If unit is Fahrenheit change into Celsius
        change_unit = False
        if self.unit == 'F':
            change_unit = True
            self.to_celsius()

        #Perform update using Celsius
        self.measurement += random.uniform(-1,1)
        if self.measurement > 40:
            self.measurement = 40
        elif self.measurement < 36:
            self.measurement = 36

        #Return to original unit
        if change_unit:
            self.to_fahrenheit
        

    def to_fahrenheit(self):
        if self.unit=='C':
            self.measurement = self.mesurements*1.8+32
            self.unit = "F"

    def to_celsius(self):
        if self.unit == 'F':
            self.measurement = (self.measurement - 32)/1.8
            self.unit = 'C'
            
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


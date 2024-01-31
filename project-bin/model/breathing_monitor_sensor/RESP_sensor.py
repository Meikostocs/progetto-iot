import json
import random

class RESPSensor:

    def __init__(self, measurement=None):
        """
        RESP Sensor

        :param measurement: RESP (Respiratory rate).
        :type measurement: int [BPM]
        """
        if measurement is None:
            self.measurement = random.randint(12,18)
        else:
            self.measurement = measurement
        self.unit = "BPM"

    def update_measurements(self):
        self.measurement += random.randint(-1,1 )
        
        if self.measurement <= 0 : 
            self.measurement = 1
        elif self.measurement >= 30:
            self.measurement = 29
    
    def critical_status(self):
        return self.measurement < 12 or self.measurement > 20
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


import json
import random
from request.oxygenation_request import OxygenationRequest as ox_req
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
        self.measurement += random.uniform(-1,1)
        if self.measurement > 100:
            self.measurement = 100

    def needed_oxygen(self):
        if self.measurement > 95:
            return ox_req.OXYGENATION_STOP
        elif self.measurement > 90:
            return ox_req.OXYGENATION_LOW
        elif self.measurement > 85:
            return ox_req.OXYGENATION_MEDIUM
        else:
            return ox_req.OXYGENATION_HIGH


    def critical_status(self):
        return self.measurement < 95

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


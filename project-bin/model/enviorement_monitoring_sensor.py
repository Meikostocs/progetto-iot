import json
import random
from model.battery import Battery
from request.suction_request import SuctionRequestDescriptor

class EnviorementMonitoringSensor:

    def __init__(self, room_id="A1", bed_id="1", temperature=None, humidity=None, PM10=None, battery=None, ):
        if temperature is None:
            self.temperature = 22
        else:
            self.temperature = temperature

        if humidity is None:
            self.humidity = 60
        else:
            self.humidity = humidity

        if PM10 is None:
            self.PM10=60
        else:
            self.PM10 = PM10

        if battery is None:
            self.battery= Battery(capacity=10000, level=100)
        else:
            self.battery= Battery(capacity=10000, level=battery)

        self.room_id = room_id
        self.bed_id = bed_id

    def update_measurements(self):
        self.temperature += random.uniform(-1.0, 1.0)
        self.humidity += random.uniform(-1.0, 1.0)
        self.PM10 += random.uniform(-1.0, 1.0)
        self.battery.update_measurements()

        #Range PM10 0-300
        self.PM10 = max(0,min(self.PM10,300))

    def air_quality_check(self):
        humidity_threshold = 60  # %
        high_humidity = 70
        pm10_threshold = 20  # µg/m³
        pm10_medium = 40
        pm10_high = 50

        if self.humidity >= high_humidity or self.PM10 >= pm10_high:
            return SuctionRequestDescriptor.SUCTION_HIGH
        elif self.PM10 >= pm10_medium:
            return SuctionRequestDescriptor.SUCTION_MEDIUM
        elif self.humidity >= humidity_threshold or self.PM10 >= pm10_threshold:
            return SuctionRequestDescriptor.SUCTION_LOW
        else:
            return SuctionRequestDescriptor.SUCTION_OFF
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

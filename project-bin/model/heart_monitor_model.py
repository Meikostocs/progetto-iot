from heart_monitor_sensor_model.ECG_sensor import ECG_sensor
from heart_monitor_sensor_model.heart_rate_sensor import Heart_rate_sensor
from heart_monitor_sensor_model.IBP_sensor import IBP_sensor
from heart_monitor_sensor_model.NIBP_sensor import NIBP_sensor
from heart_monitor_sensor_model.pressure_avarage_sensor import Pressure_avarage_sensor

import json
import time

class Heart_monitor_model:

    def __init__(self):
        self.ECG = ECG_sensor()
        self.heart_rate = Heart_rate_sensor()
        self.IBP = IBP_sensor()
        self.NIBP = NIBP_sensor()
        self.pressure_avg = Pressure_avarage_sensor()

    def update_measurements(self):
        self.ECG.update_measurements()
        self.heart_rate.update_measurements()
        self.IBP.update_measurements()
        self.NIBP.update_measurements()
        self.pressure_avg.update_measurements()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

s1= Heart_monitor_model()

while True:
    s1.update_measurements()
    print(s1.to_json())
    time.sleep(3)




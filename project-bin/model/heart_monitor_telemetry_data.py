from heart_monitor_sensor_model.ECG_sensor import ECGSensor
from heart_monitor_sensor_model.heart_rate_sensor import HeartRateSensor
from heart_monitor_sensor_model.IBP_sensor import IBPSensor
from heart_monitor_sensor_model.NIBP_sensor import NIBPSensor
from heart_monitor_sensor_model.pressure_avarage_sensor import PressureAvarageSensor
from model.battery import Battery

import json



class HeartMonitorTelemtryData:
    def __init__(self, ecg_measurement=None, heart_rate_measurement=None, ibp_measurement=None,
                 nibp_measurement=None, pressure_avg_measurement=None, battery_level=None):
        """
        Caputure data.
        """
        self.ECG = ECGSensor(ecg_measurement)
        self.heart_rate = HeartRateSensor(heart_rate_measurement)
        self.IBP = IBPSensor(ibp_measurement)
        self.NIBP = NIBPSensor(nibp_measurement)
        self.pressure_avg = PressureAvarageSensor(pressure_avg_measurement)
        # Battery has 10A
        self.battery = Battery(capacity=10000, level=battery_level)

    def update_measurements(self):
        self.ECG.update_measurements()
        self.heart_rate.update_measurements()
        self.IBP.update_measurements()
        self.NIBP.update_measurements()
        self.pressure_avg.update_measurements()
        self.battery.update_measurements()

    def critical_status(self):
        return (self.ECG.critical_status() or
                self.heart_rate.critical_status() or
                self.IBP.critical_status() or
                self.NIBP.critical_status() or
                self.pressure_avg.critical_status() or
                self.battery.critical_status())

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

from model.breathing_monitor_sensor.CO2_sensor import Co2Sensor
from model.breathing_monitor_sensor.SpO2_sensor import SpO2Sensor
from model.breathing_monitor_sensor.RESP_sensor import RESPSensor
from model.breathing_monitor_sensor.EtCO2_sensor import EtCO2Sensor
from model.battery import Battery
import json


class BreathingMonitorTelemtryData:
    def __init__(self, spo2_measurement=None, resp_measurement=None, co2_measurement=None, co2_unit='mmHg',
                 etco2_concentration=None, etco2_pressure=None, battery_level=None):
        """
        Caputure data.
        """
        self.SpO2 = SpO2Sensor(spo2_measurement)
        self.RESP = RESPSensor(resp_measurement)
        self.CO2 = Co2Sensor(co2_measurement, co2_unit)
        self.EtCO2 = EtCO2Sensor(etco2_concentration, etco2_pressure)
        # Battery has 10A
        self.battery = Battery(capacity=10000, level=battery_level)

    def update_measurements(self):
        self.SpO2.update_measurements()
        self.RESP.update_measurements()
        self.CO2.update_measurements()
        self.EtCO2.update_measurements()
        self.battery.update_measurements()

    def critical_status(self):
        return (self.SpO2.critical_status() or
                self.RESP.critical_status() or
                self.CO2.critical_status() or
                self.EtCO2.critical_status() or
                self.battery.critical_status())

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

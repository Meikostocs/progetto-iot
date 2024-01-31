from breathing_monitor_sensor.CO2_sensor import Co2Sensor
from breathing_monitor_sensor.SpO2_sensor import SpO2Sensor
from breathing_monitor_sensor.RESP_sensor import RESPSensor
from breathing_monitor_sensor.EtCO2_sensor import EtCO2Sensor
import json 

class BreathingMonitorTelemtryData:
    def __init__(self):
        """
        Caputure data.
        """
        self.SpO2  = SpO2Sensor()
        self.RESP  = RESPSensor()
        self.CO2   = Co2Sensor() 
        self.EtCO2 = EtCO2Sensor()

    def update_measurements(self):
        self.SpO2.update_measurements()
        self.RESP.update_measurements()
        self.CO2.update_measurements()
        self.EtCO2.update_measurements()
        

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
import json
from infusion_monitor_sensor.temperature_sensor import TemperatureSensor

class InfusionMonitorTelemetryData:
    def __init__(self):
        """
        Caputure data.
        """
        self.temperature = TemperatureSensor()

    def update_measurements(self):
        self.temperature.update_measurements()

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
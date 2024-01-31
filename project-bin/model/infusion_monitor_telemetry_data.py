import json
from model.infusion_monitor_sensor.temperature_sensor import TemperatureSensor
from model.battery import Battery


class InfusionMonitorTelemetryData:
    def __init__(self, battery_level=None, temp_unit='C', temp_measurement=None):
        """
        Caputure data.
        """
        self.unit = temp_unit
        if temp_unit is None:
            self.unit = 'C'
        self.temperature = TemperatureSensor(unit=self.unit, measurement=temp_measurement)
        # Battery has 10A
        self.battery = Battery(capacity=10000, level=battery_level)

    def update_measurements(self):
        self.temperature.update_measurements()
        self.battery.update_measurements()

    def critical_status(self):
        self.temperature.critical_status()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

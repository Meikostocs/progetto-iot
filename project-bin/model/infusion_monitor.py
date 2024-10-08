import json
from model.infusion_monitor_descriptor import InfusionMonitorDescriptor
from model.infusion_monitor_telemetry_data import InfusionMonitorTelemetryData

class InfusionMonitor:

    def __init__(self,id_room, id_bed,temp_measurement=None,temp_unit=None,battery_level=None):
        self.infusion_monitor_descriptor     = InfusionMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.infusion_monitor_telemetry_data = InfusionMonitorTelemetryData(temp_measurement=temp_measurement, temp_unit=temp_unit, battery_level=battery_level) 

    def update_measurements(self):
        self.infusion_monitor_telemetry_data.update_measurements()

    def critical_status(self):
        return self.infusion_monitor_telemetry_data.battery.critical_status() or self.infusion_monitor_telemetry_data.temperature.critical_status()

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
import json
from infusion_monitor_descriptor import InfusionMonitorDescriptor
from infusion_monitor_telemetry_data import InfusionMonitorTelemetryData

class InfusionMonitor:

    def __init__(self,id_room, id_bed):
        self.infusion_monitor_descriptor     = InfusionMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.infusion_monitor_telemetry_data = InfusionMonitorTelemetryData() 

    def update_measurements(self):
        self.infusion_monitor_telemetry_data.update_measurements()

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
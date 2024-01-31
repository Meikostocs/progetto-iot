import json
from breathing_monitor_descriptor import BreathingMonitorDescriptor
from breathing_monitor_telemetry_data import BreathingMonitorTelemtryData

class BreathingMonitor:

    def __init__(self,id_room, id_bed):
        self.breathing_monitor_descriptor     = BreathingMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.breathing_monitor_telemetry_data = BreathingMonitorTelemtryData() 

    def update_measurements(self):
        self.breathing_monitor_telemetry_data.update_measurements()

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
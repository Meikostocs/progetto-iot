import json
from breathing_monitor_descriptor import BreathingMonitorDescriptor
from breathing_monitor_telemetry_data import BreathingMonitorTelemtryData

class BreathingMonitor:

    def __init__(self,
                id_room,
                id_bed,
                spo2_measurement    = None,
                resp_measurement    = None,
                co2_measurement     = None,
                co2_unit            = 'mmHg',
                etco2_concentration = None,
                etco2_pressure      = None,
                battery_level       = None):
                
        self.breathing_monitor_descriptor     = BreathingMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.breathing_monitor_telemetry_data = BreathingMonitorTelemtryData(spo2_measurement    = spo2_measurement,
                                                                             resp_measurement   = resp_measurement,
                                                                             co2_measurement     = co2_measurement, 
                                                                             co2_unit            = co2_unit,
                                                                             etco2_concentration = etco2_concentration,
                                                                             etco2_pressure      = etco2_pressure,
                                                                             battery_level       = battery_level) 


    def update_measurements(self):
        self.breathing_monitor_telemetry_data.update_measurements()

    def critical_status(self):
        return self.breathing_monitor_telemetry_data.critical_status()

    def to_json(self):
        return json.dumps(self,default=lambda o: o.__dict__)
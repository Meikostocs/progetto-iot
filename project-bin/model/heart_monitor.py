from model.heart_monitor_descriptor import HeartMonitorDescriptor
from model.heart_monitor_telemetry_data import HeartMonitorTelemtryData
import json

class HeartMonitor:

    def __init__(self,
                 id_room,
                 id_bed,
                 ecg_measurement=None,
                 heart_rate_measurement=None,
                 ibp_pressure1_measurement=None,
                 ibp_pressure2_measurement=None,
                 nibp_diastolic_measurement=None,
                 nibp_sistolic_measurement=None,
                 pressure_avg_measurement=None,
                 battery_level=None):

        self.heart_monitor_descriptor = HeartMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.heart_monitor_telemetry_data = HeartMonitorTelemtryData(ecg_measurement=ecg_measurement,
                                                                         heart_rate_measurement=heart_rate_measurement,
                                                                         ibp_pressure1_measurement=ibp_pressure1_measurement,
                                                                         ibp_pressure2_measurement=ibp_pressure2_measurement,
                                                                         nibp_diastolic_measurement=nibp_diastolic_measurement,
                                                                         nibp_sistolic_measurement=nibp_sistolic_measurement,
                                                                         pressure_avg_measurement=pressure_avg_measurement,
                                                                         battery_level=battery_level)

    def update_measurements(self):
        self.heart_monitor_telemetry_data.update_measurements()

    def critical_status(self):
        return self.heart_monitor_telemetry_data.critical_status()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)










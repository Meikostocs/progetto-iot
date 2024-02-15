from model.heart_monitor_descriptor import HeartMonitorDescriptor
from model.heart_monitor_telemetry_data import HeartMonitorTelemtryData
from model.console import Console
import json
import time

class HeartMonitor:

    def __init__(self,
                 id_room,
                 id_bed,
                 ecg_measurement=None,
                 heart_rate_measurement=None,
                 ibp_measurement=None,
                 nibp_measurement=None,
                 pressure_avg_measurement=None,
                 battery_level=None):

        self.heart_monitor_descriptor = HeartMonitorDescriptor(id_room=id_room, id_bed=id_bed)
        self.heart_monitor_telemetry_data = HeartMonitorTelemtryData(ecg_measurement=ecg_measurement,
                                                                         heart_rate_measurement=heart_rate_measurement,
                                                                         ibp_measurement=ibp_measurement,
                                                                         nibp_measurement=nibp_measurement,
                                                                         pressure_avg_measurement=pressure_avg_measurement,
                                                                         battery_level=battery_level)

    def update_measurements(self):
        self.heart_monitor_telemetry_data.update_measurements()

    def critical_status(self):
        return self.heart_monitor_telemetry_data.critical_status()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


prova= HeartMonitor(id_room='prova', id_bed='1')
console=Console

while True:
    prova.update_measurements()
    print(prova.to_json())
    if prova.critical_status():
        console.error(console,"Stato critico")
    else:
        console.print(console,"tutto ok")
    time.sleep(0.5)







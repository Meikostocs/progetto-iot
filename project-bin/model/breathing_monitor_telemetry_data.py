from breathing_monitor_sensor.co2_sensor import Co2Sensor

class BreathingMonitorTelemtryData:
    def __init__(self, spo2, resp, co2, etco2):
        """
        Caputure data.

        :param spo2: SpO2 (Blood oxygen saturation value).
        :type spo2: float [%]
        :param resp: RESP, Respiration Frequency.
        :type resp: int [BPM]
        :param co2: CO2 value.
        :type co2: float [mmHg]
        :param etco2: End-Tidal CO2. It measures the concentration of CO2 at exhalation end. 
        :type etco2: dict
            - "pressure":"mmHg".
            - "percentage":"%".
        """
        self.spo2  = spo2
        self.resp  = resp
        self.co2   = Co2Sensor(units="mmHg") 
        self.etco2 = etco2


    def to_json(self):
        return json.dump(self,default=lambda o: o.__dict__)
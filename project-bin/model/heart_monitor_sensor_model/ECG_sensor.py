import json
import random


class ECGSensor:

    def __init__(self,ecg_signal=None):
        if ecg_signal is None or len(ecg_signal)!=7:
            self.ecg_signal = [random.uniform(-0.5, 0.5) for _ in range(7)]
        else:
            self.ecg_signal = ecg_signal
        self.unit="mV"

    def update_measurements(self):
        for i in range(len(self.ecg_signal)):
            self.ecg_signal[i] = random.uniform(-1, 1)

    def critical_status(self):
        for i in range(len(self.ecg_signal)):
            if self.ecg_signal[i] == -0.5 or self.ecg_signal[i] == 0.5:
                return True
        return False


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

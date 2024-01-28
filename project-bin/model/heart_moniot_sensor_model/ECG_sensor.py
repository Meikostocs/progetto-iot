import json
import random


class ECG_sensor:

    def __init__(self):
        self.ecg_signal = [random.uniform(-0.5, 0.5) for _ in range(7)]

    def update_measurements(self):
        for i in range(len(self.ecg_signal)):
            self.ecg_signal[i] = random.uniform(-1, 1)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

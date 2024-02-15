import json
import random



class HeartRateSensor:

    def __init__(self, bpm=None):
        if bpm is None:
            self.bpm = 80
        else:
            self.bpm = bpm

        self.unit="BPM"

    def update_measurements(self):
        self.bpm += random.uniform(-10.0, 10.0)

        #range
        self.bpm = max(0.0, min(self.bpm,250))

    def critical_status(self):
        if self.bpm<60 or self.bpm>220:
            return True
        else:
            return False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)





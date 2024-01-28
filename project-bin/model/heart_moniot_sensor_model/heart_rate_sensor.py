import json
import random



class Heart_rate_sensor:

    def __init__(self):
        self.bpm = 80

    def update_measurements(self):
        self.bpm += random.uniform(-10.0, 10.0)

        #range
        self.bpm = max(0.0, min(self.bpm,250))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)





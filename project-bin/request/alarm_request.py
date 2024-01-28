#COAP
import json

class AlarmRequestDescriptor:
    ALARM_ON = "on"
    ALARM_OFF = "off"

    def __init__(self, type):
        self.type = type

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
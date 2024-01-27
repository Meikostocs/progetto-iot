#COAP
import json

class LightRequestDescriptor:
    LIGHT_LOW = "low_light"
    LIGHT_MEDIUM ="medium_light"
    LIGHT_HIGH ="high_light"
    TURN_OFF="off_light"

    def __init__(self, type):
        self.type = type

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
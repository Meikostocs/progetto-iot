import json


class OxygenationRequest:

    OXYGENATION_LOW = "low_oxigenation"
    OXYGENATION_MEDIUM = "medium_oxigenation"
    OXYGENATION_HIGH = "high_oxigenation"
    OXYGENATION_STOP = "stop_oxigenation"

    def __init__(self, type):
        self.type = type

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
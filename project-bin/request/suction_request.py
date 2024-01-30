#COAP
import json

class SuctionRequestDescriptor:
    SUCTION_LOW = "low_suction"
    SUCTION_MEDIUM = "medium_suction"
    SUCTION_HIGH = "high_suction"
    SUCTION_OFF="off_suction"

    def __init__(self, suction_state):
        self.suction_state = suction_state

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
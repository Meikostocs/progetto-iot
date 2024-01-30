import json
from model.suction_statuses import SuctionStatuses as ss
from enum import Enum

class SuctionFan:
    def __init__(self, room_id, bed_id):
        self.room = room_id
        self.bed_id = bed_id
        self.suction_state = ss.SUCTION_OFF.value

    def switch_suction_state(self):
        match self.suction_state:
            case ss.SUCTION_OFF.value:
                self.suction_state = ss.SUCTION_LOW.value
            case ss.SUCTION_LOW.value:
                self.suction_state = ss.SUCTION_MEDIUM.value
            case ss.SUCTION_MEDIUM.value:
                self.suction_state = ss.SUCTION_HIGH.value
            case ss.SUCTION_HIGH.value:
                self.suction_state = ss.SUCTION_OFF.value

    def set_suction_state(self,level):
        match level:
            case ss.SUCTION_OFF.value:
                self.suction_state = level
            case ss.SUCTION_LOW.value:
                self.suction_state = level
            case ss.SUCTION_MEDIUM.value:
                self.suction_state = level
            case ss.SUCTION_HIGH.value:
                self.suction_state = level

    def to_json(self):
        #return json.dumps(self, default=lambda o: o.__dict__)
        return json.dumps(self, default=lambda o: o.value if isinstance(o, Enum) else o.__dict__)
import json
from model.suction_statuses import SuctionStatuses as ss

class SuctionFan:
    def __init__(self, room, bed_id):
        self.room = room
        self.bed_id = bed_id
        self.suction_state = ss.SUCTION_OFF

    def switch_suction_state(self):
        match self.suction_state:
            case ss.SUCTION_OFF:
                self.suction_state = ss.SUCTION_LOW
            case ss.SUCTION_LOW:
                self.suction_state = ss.SUCTION_MEDIUM
            case ss.SUCTION_MEDIUM:
                self.suction_state = ss.SUCTION_HIGH
            case ss.SUCTION_HIGH:
                self.suction_state = ss.SUCTION_OFF

    def set_suction_state(self,level):
        match level:
            case ss.SUCTION_OFF:
                self.suction_state = level
            case ss.SUCTION_LOW:
                self.suction_state = level
            case ss.SUCTION_MEDIUM:
                self.suction_state = level
            case ss.SUCTION_HIGH:
                self.suction_state = level

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
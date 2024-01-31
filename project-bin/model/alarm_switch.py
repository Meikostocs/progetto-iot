import json
from model.alarm_statuses import AlarmStatuses as As
from enum import Enum
class AlarmSwitch:

    def __init__(self,room_id,bed_id):
        self.room = room_id
        self.bed_id = bed_id
        self.alarm_state = As.ALARM_OFF.value

    def switch_alarm_state(self):
        match self.alarm_state:
            case As.ALARM_ON.value:
                self.alarm_state = As.ALARM_OFF.value
            case As.ALARM_OFF.value:
                self.alarm_state = As.ALARM_ON.value

    def turn_on(self):
        self.alarm_state = As.ALARM_ON.value

    def turn_off(self):
        self.alarm_state = As.ALARM_OFF.value

    def to_json(self):
        return json.dumps(self, default=lambda o: o.value if isinstance(o, Enum) else o.__dict__)
import json
from model.alarm_statuses import AlarmStatuses as As

class AlarmSwitch:

    def __init__(self,room,bed_id):
        self.room = room
        self.bed_id = bed_id
        self.alarm_state = As.ALARM_OFF

    def switch_alarm_state(self):
        match self.alarm_state:
            case As.ALARM_ON:
                self.alarm_state = As.ALARM_OFF
            case As.ALARM_OFF:
                self.alarm_state = As.ALARM_ON

    def turn_on(self):
        self.alarm_state = As.ALARM_ON

    def turn_off(self):
        self.alarm_state = As.ALARM_OFF

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
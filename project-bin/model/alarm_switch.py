import json

class AlarmSwitch:

    def __init__(self,room,bed_id):
        self.room=room
        self.bed_id=bed_id
        self.state="off"

    def turn_on(self):
        self.power_state = "on"

    def turn_off(self):
        self.power_state = "off"


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
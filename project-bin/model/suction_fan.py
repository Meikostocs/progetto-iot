import json

class SuctionFan:
    def __init__(self, room, fan_id):
        self.room = room
        self.fan_id = fan_id
        self.state = "off"

    def set_suction_mode(self,level):
        levels = ["Low", "Medium", "High","Off"]
        if level in levels:
            self.state = level

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
import json
from model.light_statuses import LightStatuses as ls
from enum import Enum

class LightSmartObj:
    def __init__(self,room_id,bed_id):
        self.room=room_id
        self.bed_id = bed_id
        self.light_state = ls.LIGHT_OFF
        self.energy_consumption_sensor = 0.0

    def switch_light_state(self):
        match self.light_state:
            case ls.LIGHT_OFF:
                self.light_state = ls.LIGHT_LOW
            case ls.LIGHT_LOW:
                self.light_state = ls.LIGHT_MEDIUM
            case ls.LIGHT_MEDIUM:
                self.light_state = ls.LIGHT_HIGH
            case ls.LIGHT_HIGH:
                self.light_state = ls.LIGHT_OFF

    def set_light_state(self, level):
        match level:
            case ls.LIGHT_LOW:
                self.light_state = level
            case ls.LIGHT_MEDIUM:
                self.light_state = level
            case ls.LIGHT_MEDIUM:
                self.light_state = level
            case ls.LIGHT_OFF:
                self.light_state = level

    def update_energy_consumption(self):
        if self.light_state == ls.LIGHT_LOW:
            self.energy_consumption_sensor = 3 #kw/hora
        if self.light_state ==ls.LIGHT_MEDIUM:
            self.energy_consumption_sensor = 6
        if self.light_state == ls.LIGHT_HIGH:
            self.energy_consumption_sensor = 10

    def to_json(self):
        return json.dumps(self, default=lambda o: o.value if isinstance(o, Enum) else o.__dict__)

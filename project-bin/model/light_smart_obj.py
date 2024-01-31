import json
from model.light_statuses import LightStatuses as ls
from enum import Enum
import asyncio
from client.coap_get_client import get_coap_light as get_coap_message


class LightSmartObj:
    def __init__(self,room_id,bed_id):
        self.room_id=room_id
        self.bed_id = bed_id
        self.light_state = ls.LIGHT_OFF.value
        self.energy_consumption_sensor = 0.0

    def switch_light_state(self):
        match self.light_state:
            case ls.LIGHT_OFF.value:
                self.light_state = ls.LIGHT_LOW.value
            case ls.LIGHT_LOW.value:
                self.light_state = ls.LIGHT_MEDIUM.value
            case ls.LIGHT_MEDIUM.value:
                self.light_state = ls.LIGHT_HIGH.value
            case ls.LIGHT_HIGH.value:
                self.light_state = ls.LIGHT_OFF.value

    def set_light_state(self, level):
        match level:
            case ls.LIGHT_LOW.value:
                self.light_state = level
            case ls.LIGHT_MEDIUM.value:
                self.light_state = level
            case ls.LIGHT_HIGH.value:
                self.light_state = level
            case ls.LIGHT_OFF.value:
                self.light_state = level


    def update_energy_consumption(self):
        if self.light_state == ls.LIGHT_LOW.value:
            self.energy_consumption_sensor = 3 #kw/hora
        if self.light_state ==ls.LIGHT_MEDIUM.value:
            self.energy_consumption_sensor = 6
        if self.light_state == ls.LIGHT_HIGH.value:
            self.energy_consumption_sensor = 10


    def update_energy_consumption_mqtt(self):
        new_state = asyncio.get_event_loop().run_until_complete(get_coap_message())
        self.light_state = new_state["light_state"]

        if self.light_state == ls.LIGHT_LOW.value:
            self.energy_consumption_sensor = 3 #kw/hora
        if self.light_state ==ls.LIGHT_MEDIUM.value:
            self.energy_consumption_sensor = 6
        if self.light_state == ls.LIGHT_HIGH.value:
            self.energy_consumption_sensor = 10

    def to_json(self):
        return json.dumps(self, default=lambda o: o.value if isinstance(o, Enum) else o.__dict__)

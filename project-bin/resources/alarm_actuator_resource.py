import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import time
import json
from aiocoap.numbers.codes import Code
from request.alarm_request import AlarmRequestDescriptor
from model.alarm_switch import AlarmSwitch
from kpn_senml import *
from model.console import Console


class AlarmActuatorResource(resource.Resource):
    def __init__(self,id_room, id_bed):
        super().__init__()
        self.device_name = f'alarm-{id_room}-{id_bed}'
        self.id_room = id_room
        self.id_bed = id_bed

        self.device_info = AlarmSwitch(room_id=self.id_room,bed_id=self.id_bed)
        self.if_ = "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']  # TESTO, METTO DENTRO "LOW" O "MEDIUM" O "HIGH"
        self.rt = "it.project.device.actuator.alarm"
        self.title = "AlarmSwitch"
        self.console = Console(debug=True)
        self.console.print(f"[+] AlarmSwitch {id_room}-{id_bed} UP")


    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        pack.base_time = int(time.time())
        state = SenmlRecord("alarm_state",value=self.device_info.alarm_state)
        pack.add(state)
        return pack.to_json()

    async def render_post(self, request):
        self.console.debug(f"POST AT {self.id_room}-{self.id_bed}")
        self.device_info.switch_alarm_state()
        self.console.debug(f'STATE CHANGED IN: {self.device_info.alarm_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        self.console.print(f"ALARM PUT AT {self.id_room}-{self.id_bed}")
        self.console.debug(f'PUT PAYLOAD : {json_payload_string}')
        change_alarm_request = AlarmRequestDescriptor(**json.loads(json_payload_string))
        self.console.debug(f'SWITCH STATUS INTO {change_alarm_request.type}')

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_ON:
            self.device_info.turn_on()
            print(f'🚨ALARM RECIVED {self.id_room}-{self.id_bed}🚨')
            return aiocoap.Message(code=Code.CHANGED)

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_OFF:
            self.device_info.turn_off()
            print(f'ALARM STOP {self.id_room}-{self.id_bed}')
            return aiocoap.Message(code=Code.CHANGED)


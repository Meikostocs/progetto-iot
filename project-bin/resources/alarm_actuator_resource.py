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

    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        pack.base_time = int(time.time())
        state = SenmlRecord("alarm_state",value=self.device_info.alarm_state)
        pack.add(state)
        return pack.to_json()

    async def render_post(self, request):
        self.console.debug("AlarmActuatorResource -> POST Request Received ...")
        self.device_info.switch_alarm_state()
        print(f'State changed in: {self.device_info.alarm_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        #print(f'AlarmActuatorResource -> PUT Byte payload: {request.payload}')
        json_payload_string = request.payload.decode('UTF-8')
        print(f'AlarmActuatorResource -> PUT String Payload: {json_payload_string}')
        change_alarm_request = AlarmRequestDescriptor(**json.loads(json_payload_string))
        print(f'Change Alarm Request Received: {change_alarm_request.type}')

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_ON:
            self.device_info.turn_on()
            print(f'🚨ALARM RECIVED FROM {self.id_room}-{self.id_bed}🚨')
            print(f'State changed in: {self.device_info.alarm_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_OFF:
            self.device_info.turn_off()
            print(f'ALARM STOP FROM {self.id_room}-{self.id_bed}')
            return aiocoap.Message(code=Code.CHANGED)


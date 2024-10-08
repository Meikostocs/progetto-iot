import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import json
from aiocoap.numbers.codes import Code
from request.alarm_request import AlarmRequestDescriptor
from model.alarm_switch import AlarmSwitch
from model.console import Console


class AlarmActuatorResource(resource.Resource):
    def __init__(self,id_room, id_bed):
        super().__init__()
        self.device_name = f'alarm-{id_room}-{id_bed}'
        self.id_room = id_room
        self.id_bed = id_bed
        self.device_info = AlarmSwitch(room_id=self.id_room,bed_id=self.id_bed)
        self.if_ = "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']
        self.rt = "it.project.device.actuator.alarm"
        self.title = "AlarmSwitch"
        self.console = Console(debug=True)
        self.console.print(f"[+] ALARM SWITCH {id_room}-{id_bed} UP")

    async def render_post(self, request):
        self.console.debug(f"POST AT {self.id_room}-{self.id_bed}")
        self.device_info.switch_alarm_state()
        self.console.debug(f'STATE CHANGED IN: {self.device_info.alarm_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        self.console.print(f"PUT AT ALARM FROM {self.id_room}-{self.id_bed}")
        self.console.debug(f'PUT PAYLOAD : {json_payload_string}')
        change_alarm_request = AlarmRequestDescriptor(**json.loads(json_payload_string))
        self.console.debug(f'SWITCH STATUS INTO {change_alarm_request.type}')

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_ON:
            self.device_info.turn_on()
            print(f'🚨ALARM RECEIVED {self.id_room}-{self.id_bed}🚨')
            return aiocoap.Message(code=Code.CHANGED)

        if change_alarm_request.type == AlarmRequestDescriptor.ALARM_OFF:
            self.device_info.turn_off()
            print(f'ALARM STOP {self.id_room}-{self.id_bed}')
            return aiocoap.Message(code=Code.CHANGED)

    async def render_get(self, request):
        payload_string = self.device_info.to_json()
        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))
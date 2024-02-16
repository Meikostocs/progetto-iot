import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import json
from aiocoap.numbers.codes import Code
from request.suction_request import SuctionRequestDescriptor
from model.suction_fan import SuctionFan
from model.console import Console

class SuctionActuatorResource(resource.Resource):
    def __init__(self,id_room,id_bed):
        super().__init__()
        self.device_name = f'alarm-{id_room}-{id_bed}'
        self.id_room = id_room
        self.id_bed = id_bed
        self.device_info = SuctionFan(room_id=self.id_room,bed_id=self.id_bed)
        self.if_ = "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']
        self.rt = "it.project.device.actuator.suctionfan"
        self.title = "Suction Fan"
        self.console = Console(debug=True)
        self.console.print(f"[+] SUCTION FAN {id_room}-{id_bed} UP")

    async def render_post(self,request):
        self.console.print(f"POST AT SUCTION FAN FROM {self.id_room}-{self.id_bed}")
        self.device_info.switch_suction_state()
        self.console.debug(f'STATE CHANGED IN: {self.device_info.suction_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        change_suction_request = SuctionRequestDescriptor(**json.loads(json_payload_string))
        self.console.print(f"PUT AT SUCTION FAN FROM {self.id_room}-{self.id_bed}")
        self.console.debug(f'PUT PAYLOAD : {json_payload_string}')
        self.console.debug(f'SWITCH STATUS INTO {change_suction_request.suction_state}')

        if change_suction_request.suction_state == SuctionRequestDescriptor.SUCTION_LOW:
            self.device_info.set_suction_state(change_suction_request.suction_state)
            print(f'State changed in: {self.device_info.suction_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_suction_request.suction_state == SuctionRequestDescriptor.SUCTION_MEDIUM:
            self.device_info.set_suction_state(change_suction_request.suction_state)
            print(f'State changed in: {self.device_info.suction_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_suction_request.suction_state == SuctionRequestDescriptor.SUCTION_HIGH:
            self.device_info.set_suction_state(change_suction_request.suction_state)
            print(f'State changed in: {self.device_info.suction_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_suction_request.suction_state == SuctionRequestDescriptor.SUCTION_OFF:
            self.device_info.set_suction_state(change_suction_request.suction_state)
            print(f'State changed in: {self.device_info.suction_state}')
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)

    async def render_get(self, request):
        payload_string = self.device_info.to_json()

        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))
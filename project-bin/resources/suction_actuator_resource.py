import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import time
import json
from aiocoap.numbers.codes import Code
from request.suction_request import SuctionRequestDescriptor
from model.suction_fan import SuctionFan
from kpn_senml import *


class SuctionActuatorResource(resource.Resource):
    def __init__(self,id_room,id_bed):
        super().__init__()
        self.device_name = f'alarm-{id_room}-{id_bed}'
        self.id_room = id_room
        self.id_bed = id_bed
        self.device_info = SuctionFan(room_id=self.id_room,bed_id=self.id_bed)
        self.if_ = "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']  # TESTO, METTO DENTRO "LOW" O "MEDIUM" O "HIGH"
        self.rt = "it.project.device.actuator.suctionfan"
        self.title = "Suction Fan"

    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        pack.base_time = int(time.time())
        current = SenmlRecord("current_fan_state", value=self.device_info.suction_state)
        pack.add(current)
        return pack.to_json()

    async def render_post(self,request):
        print("SuctionActuatorResource -> POST Request Received ...")
        # self.coffee_history.increase_short_coffee()
        self.device_info.switch_suction_state()
        print(f'State changed in: {self.device_info.suction_state}')


        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        #print(f'SuctionActuatorResource -> PUT Byte payload: {request.payload}')
        json_payload_string = request.payload.decode('UTF-8')
        print(f'LightActuatorResource -> PUT String Payload: {json_payload_string}')
        change_suction_request = SuctionRequestDescriptor(**json.loads(json_payload_string))
        print(f'Change Suction Request Received:{change_suction_request.suction_state} FROM {self.id_room}-{self.id_bed}')

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
import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import time
import json
from aiocoap.numbers.codes import Code
from request.light_request import LightRequestDescriptor
from model.light_smart_obj import LightSmartObj
from kpn_senml import *
#AL MOMENTO E' SOLO PER LOW MEDIU HIGH. dEVO FARE UN ALTRO PER ON OFF?

class LightActuatorResource(resource.Resource): #se cambio qualcosa, viene rimandata la risorsa nuova

    def __init__(self,device_name):
        super().__init__()
        self.device_name = device_name
        self.device_info = LightSmartObj(room_id='A1',bed_id=1)
        self.if_= "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']  # TESTO, METTO DENTRO "LOW" O "MEDIUM" O "HIGH"
        self.rt ="it.project.device.actuator.light"
        self.title = "Light Actuator"

    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        pack.base_time = int(time.time())
        #serializzo per ogni stato corrente
        current = SenmlRecord("current_light",value=self.device_info.light_state)
        pack.add(current)
        return pack.to_json()


    async def render_get(self, request):
        print("LightActuatorResource -> GET Request Received ...")
        payload_string = self.device_info.to_json()
        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))


    async def render_post(self, request):
        print("LightActuatorResource -> POST Request Received ...")
        #self.coffee_history.increase_short_coffee()
        self.device_info.switch_light_state()
        self.device_info.update_energy_consumption()
        print(f'State changed in: {self.device_info.light_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        print(f'LightActuatorResource -> PUT String Payload: {json_payload_string}')
        #change_light_request = LightRequestDescriptor(json.loads(json_payload_string)["light_state"])
        change_light_request = LightRequestDescriptor(**json.loads(json_payload_string))
        print(f'Change Light Request Received: {change_light_request.light_state}')

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_LOW:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            print(self.device_info.light_state)
            print(f'State changed in: {self.device_info.light_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_MEDIUM:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            print(f'State changed in: {self.device_info.light_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_HIGH:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            print(f'State changed in: {self.device_info.light_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.TURN_OFF:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            print(f'State changed in: {self.device_info.light_state}')
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)
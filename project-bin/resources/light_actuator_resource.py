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
        self.device_info = LightSmartObj(room=1,bed_id=2)
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

    async def render_post(self, request):
        print("LightActuatorResource -> POST Request Received ...")
        #self.coffee_history.increase_short_coffee()
        self.device_info.switch_light_state()
        self.device_info.update_energy_consumption()
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        print(f'LightActuatorResource -> PUT Byte payload: {request.payload}')
        json_payload_string = request.payload.decode('UTF-8')
        print(f'LightActuatorResource -> PUT String Payload: {json_payload_string}')
        change_light_request = LightRequestDescriptor(**json.loads(json_payload_string))
        print(f'Change Light Request Received: {change_light_request.type}')
        print('Changed light status to: ', end='')

        if change_light_request.type == LightRequestDescriptor.LIGHT_LOW:
            self.device_info.set_light_state(change_light_request.type)
            self.device_info.update_energy_consumption()
            print(change_light_request.type)
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.type == LightRequestDescriptor.LIGHT_MEDIUM:
            self.device_info.set_light_state(change_light_request.type)
            self.device_info.update_energy_consumption()
            print(change_light_request.type)
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.type == LightRequestDescriptor.LIGHT_HIGH:
            self.device_info.set_light_state(change_light_request.type)
            self.device_info.update_energy_consumption()
            print(change_light_request.type)
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.type == LightRequestDescriptor.TURN_OFF:
            self.device_info.set_light_state(change_light_request.type)
            self.device_info.update_energy_consumption()
            print(change_light_request.type)
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)
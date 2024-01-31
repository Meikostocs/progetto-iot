import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import json
from aiocoap.numbers.codes import Code
from request.light_request import LightRequestDescriptor
from model.light_smart_obj import LightSmartObj
from model.console import Console

class LightActuatorResource(resource.Resource):

    def __init__(self,device_name):
        super().__init__()
        self.device_name = device_name
        self.device_info = LightSmartObj(room_id='A1',bed_id=1)
        self.if_= "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']
        self.rt ="it.project.device.actuator.light"
        self.title = "Light Actuator"
        self.console = Console(debug=True)
        self.console.print(f"[+] LIGHT ACTUATOR UP")

    async def render_get(self, request):
        #self.console.debug("GET AT LIGHT ACTUATOR")
        payload_string = self.device_info.to_json()
        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))

    async def render_post(self, request):
        self.console.debug(f"POST AT LIGHT ACTUATOR")
        self.device_info.switch_light_state()
        self.device_info.update_energy_consumption()
        self.console.debug(f'STATE CHANGED In: {self.device_info.light_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        self.console.debug(f"PUT AT LIGHT ACTUATOR")
        self.console.debug(f'PUT PAYLOAD : {json_payload_string}')
        change_light_request = LightRequestDescriptor(**json.loads(json_payload_string))

        self.console.debug(f'SWITCH STATUS INTO {change_light_request.light_state}')

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_LOW:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_MEDIUM:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.LIGHT_HIGH:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            return aiocoap.Message(code=Code.CHANGED)

        if change_light_request.light_state == LightRequestDescriptor.TURN_OFF:
            self.device_info.set_light_state(change_light_request.light_state)
            self.device_info.update_energy_consumption()
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)
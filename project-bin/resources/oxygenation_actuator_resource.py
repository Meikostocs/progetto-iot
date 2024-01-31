import aiocoap.resource as resource
import aiocoap
from aiocoap.numbers.codes import Code
from request.oxygenation_request import OxygenationRequest
from model.oxygenator import Oxygenator
import json
from model.console import Console

class OxygenationActuatorResource(resource.Resource):

    def __init__(self,room_id, bed_id):
        super(OxygenationActuatorResource,self).__init__()
        self.room_id = room_id
        self.bed_id = bed_id
        self.name = f'oxygenator-{self.room_id}-{self.bed_id}'
        self.device_info = Oxygenator(room_id=self.room_id,bed_id=self.bed_id)
        self.if_ = "core.a"
        self.rt = "it.project.device.actuator.oxygenator"
        self.title = "Oxigenator"
        self.console = Console(debug=True)
        self.console.print(f'[+] OXYGENETOR {self.room_id}-{self.bed_id} UP')

    async def render_post(self, request):
        self.console.debug(f"POST AT OXYGEN ACTUATOR")
        self.device_info.switch_oxygenation_state()
        self.console.debug(f'STATE CHANGED In: {self.device_info.oxigenation_state}')
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        change_oxygen_request = OxygenationRequest(**json.loads(json_payload_string))
        self.console.print(f"OXYGENATOR PUT AT {self.room_id}-{self.bed_id}")
        self.console.debug(f'PUT PAYLOAD : {json_payload_string}')
        self.console.debug(f'SWITCH STATUS INTO {change_oxygen_request.oxigenation_state}')

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_LOW:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            #self.console.print(f'Change in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_MEDIUM:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            #self.console.print(f'Change in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_HIGH:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            #self.console.print(f'Change in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_STOP:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            #self.console.print(f'Change in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)
        
        
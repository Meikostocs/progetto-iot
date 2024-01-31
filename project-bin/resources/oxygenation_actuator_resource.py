import aiocoap.resource as resource
import aiocoap
from aiocoap.numbers.codes import Code
from request.oxygenation_request import OxygenationRequest
from model.oxygenator import Oxygenator
import json
from model.console import Console

class OxygenationActuatorResource(resource.Resource):

    def __init__(self,device_name):
        super().__init__()
        self.device_name = device_name
        self.device_info = Oxygenator(room_id='1A',bed_id=1)
        self.if_ = "core.a"
        #self.ct = numbers.media_types_rev['application/senml+json']
        self.rt = "it.project.device.actuator.oxygenator"
        self.title = "Oxigenator"
        self.console = Console(debug=True)


    async def render_post(self, request):
        self.console.debug("POST ON OXYGENATION")
        return aiocoap.Message(code=Code.CHANGED)



    async def render_put(self, request):
        json_payload_string = request.payload.decode('UTF-8')
        print(f'OxygenationActuatorResource -> PUT String Payload: {json_payload_string}')
        change_oxygen_request = OxygenationRequest(**json.loads(json_payload_string))
        print(f'Change Light Request Received: {change_oxygen_request.oxigenation_state}')

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_LOW:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            print(f'State changed in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_MEDIUM:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            print(f'State changed in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_HIGH:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            print(f'State changed in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        if change_oxygen_request.oxigenation_state == OxygenationRequest.OXYGENATION_STOP:
            self.device_info.set_oxigenation_state(change_oxygen_request.oxigenation_state)
            print(f'State changed in: {self.device_info.oxigenation_state}')
            return aiocoap.Message(code=Code.CHANGED)

        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)
        
        
import aiocoap.resource as resource
import aiocoap
from aiocoap.numbers.codes import Code
from request.oxygenation_request import OxygenationRequest
import json
from model.console import Console

class OxygenationActuatorResource(resource.Resource):

    def __init__(self,device_name):
        super().__init__()
        self.console = Console(debug=True)


    async def render_post(self, request):
        self.console.debug("POST ON OXYGENATION")
        return aiocoap.Message(code=Code.CHANGED)



    async def render_put(self, request):
        #print(f'SuctionActuatorResource -> PUT Byte payload: {request.payload}')
        json_payload_string = request.payload.decode('UTF-8')
        self.console.debug(f'GOT A PUT {json_payload_string}')
        
        
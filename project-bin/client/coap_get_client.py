import json
from aiocoap import *


'''
The use of this get is limited to the case sensor/actuator Light Smart Object.
Once the value is updated by a POST/PUT, a GET is needed to update the values in MQTT.

'''

async def get_coap_light():
    protocol = await Context.create_client_context()
    request = Message(code=Code.GET, uri='coap://127.0.0.1:5683/actuation/light')
    response = await protocol.request(request).response
    response_string = response.payload.decode("utf-8")
    return json.loads(response_string)

async def get_coap_alarm(uri):
    protocol = await Context.create_client_context()
    request = Message(code=Code.GET, uri=uri)
    response = await protocol.request(request).response
    response_string = response.payload.decode("utf-8")
    return json.loads(response_string)

async def get_coap_fan_state(uri):
    protocol = await Context.create_client_context()
    request = Message(code=Code.GET, uri=uri)
    response = await protocol.request(request).response
    response_string = response.payload.decode("utf-8")
    return json.loads(response_string)

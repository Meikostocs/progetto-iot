import logging
import asyncio
from aiocoap import *
import json
from request.light_request import LightRequestDescriptor


logging.basicConfig(level=logging.INFO)
TARGET_ENDPOINT = 'coap://127.0.0.1:5683'

target_light_uri ='/actuation/light'
target_suction_uri ='/actuation/suction'
target_alarm_uri ='/actuation/alarm'

async def set_light_state(level): #gli passo il livello a cui voglio switchare
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + target_light_uri)
    light_request = LightRequestDescriptor(level) #request del livelo a cui voglio cambiare ???
    payload_json_string = light_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        print(response)
        response_string = response.payload.decode("utf-8")

        print(f'Result: {response.code}\nPayload: {response.payload}\nPayload String: {response_string}')



async def set_suction_state():
    pass

async def set_alarm_state():
    pass

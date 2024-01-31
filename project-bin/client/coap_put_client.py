import logging
import asyncio
from aiocoap import *
import json
import aiocoap
from aiocoap.numbers.codes import Code
from request.light_request import LightRequestDescriptor
from request.suction_request import SuctionRequestDescriptor
from request.alarm_request import AlarmRequestDescriptor
from request.oxygenation_request import OxygenationRequest

logging.basicConfig(level=logging.ERROR) #DEBUG,INFO
TARGET_ENDPOINT = 'coap://127.0.0.1:5683'

target_light_uri ='/actuation/light'
target_suction_uri ='/actuation/suction'
target_alarm_uri ='/actuation/alarm'
target_ooxygenation_uri ='/actuation/oxygenation'

async def set_light_state(level): #gli passo il livello a cui voglio switchare
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + target_light_uri)
    #light_request = LightRequestDescriptor(LightRequestDescriptor.LIGHT_MEDIUM) #request del livelo a cui voglio cambiare ???
    light_request = LightRequestDescriptor(level)
    payload_json_string = light_request.to_json()

    request.payload = payload_json_string.encode("utf-8")
    #request.payload = json.dumps({'light_state':LightRequestDescriptor.LIGHT_MEDIUM}).encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        #print(response)
        #response_string = response.payload.decode("utf-8")

        print(f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\n')

async def set_suction_state(level):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + target_suction_uri)
    suction_request = SuctionRequestDescriptor(level)
    payload_json_string = suction_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        print(
            f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\n')

async def set_alarm_state(level):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + target_alarm_uri)
    alarm_request = AlarmRequestDescriptor(level)
    payload_json_string = alarm_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        print(response)
        response_string = response.payload.decode("utf-8")

        print(
            f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\nResponse:{response_string}\n')

async def set_oxygenation_state(level):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + target_oxygenation_uri)
    oxygenation_request = OxygenationRequest(level)
    payload_json_string = oxygenation_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        print(
            f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\n')



async def main():
    await set_light_state()
    await set_suction_state()
    await set_alarm_state()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
import logging
import asyncio
from aiocoap import *
from aiocoap.numbers.codes import Code
from request.light_request import LightRequestDescriptor
from request.suction_request import SuctionRequestDescriptor
from request.alarm_request import AlarmRequestDescriptor
from request.oxygenation_request import OxygenationRequest

'''
I'll make a different post for each actuator, so I can
trigger an actuation of my choice on a actuator,
or better: in the collector and manager I will call the function to change actuator status based on
the occurrence of an event

change_light_state: none room_id and bed_id because it is shared between the rooms.
'''

logging.basicConfig(level=logging.ERROR) #DEBUG,INFO
TARGET_ENDPOINT = 'coap://127.0.0.1:5683'

target_light_uri ='/actuation/light'


async def set_light_state(level):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + target_light_uri)
    light_request = LightRequestDescriptor(level)
    payload_json_string = light_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        print(f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\n')

async def set_suction_state(level,id_room,id_bed):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + f'/actuation/{id_room}/{id_bed}/suction')
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

async def set_alarm_state(level, id_room, id_bed):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.PUT, uri=TARGET_ENDPOINT + f'/actuation/{id_room}/{id_bed}/alarm')
    alarm_request = AlarmRequestDescriptor(level)
    payload_json_string = alarm_request.to_json()
    request.payload = payload_json_string.encode("utf-8")
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        response_string = response.payload.decode("utf-8")

        print(
            f'Result: {response.code}\nRequest payload: {request.payload.decode("utf-8")}\nResponse:{response_string}\n')

async def set_oxygenator_state(level, id_room, id_bed):
        try:
            coap_client = await Context.create_client_context()
            request = Message(code=Code.PUT, uri='coap://127.0.0.1:5683' + f'/actuation/{id_room}/{id_bed}/oxygenation')
            oxygenation_request = OxygenationRequest(level)
            payload_json_string = oxygenation_request.to_json()
            request.payload = payload_json_string.encode("utf-8")
            response = await coap_client.request(request).response

        except Exception as e:
            print('Failed to fetch resources:')
            print(e)


'''
main() is used for debug
'''

async def main():
    pass
    #await set_light_state()
    #await set_suction_state()
    #await set_alarm_state()
    #await set_oxygenation_state()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
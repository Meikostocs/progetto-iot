import logging
import asyncio
from aiocoap import *

'''
POST is not used in the dcem!
'''

logging.basicConfig(level=logging.INFO)
TARGET_ENDPOINT = 'coap://127.0.0.1:5683'


async def change_light_state():
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT +'/actuation/light')
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        if response.code.is_successful():
            return True
        else:
            return False

async def change_suction_state(id_room, id_bed):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + f'/actuation/{id_room}/{id_bed}/suction')
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        if response.code.is_successful():
            return True
        else:
            return False

async def change_alarm_state(id_room, id_bed):
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + f'/actuation/{id_room}/{id_bed}/alarm')
    try:
        response = await coap_client.request(request).response
    except Exception as e:
        print('Failed to fetch resources:')
        print(e)
    else:
        if response.code.is_successful():
            return True
        else:
            return False

'''
main() is used for debug
'''
async def main():
    #await change_light_state()
    #await change_suction_state('A1', '1')
    #await change_alarm_state('A1', '1')
    return 0

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    #asyncio.run(main())

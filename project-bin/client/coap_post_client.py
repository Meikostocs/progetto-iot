import logging
import asyncio
from aiocoap import *
import json

'''faccio una post diversa per ogni sensore, così posso 
triggerare a mia scelta una attuazione su un determinato sensore,
o meglio: nel collector e manager chiamerò la funzione per fare post di sensore x'''

logging.basicConfig(level=logging.INFO)
TARGET_ENDPOINT = 'coap://127.0.0.1:5683'

target_light_uri ='/actuation/light'
target_suction_uri ='/actuation/suction'
target_alarm_uri ='/actuation/alarm'

async def change_light_state():
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + target_light_uri)
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

async def change_suction_state():
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + target_suction_uri)
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

async def change_alarm_state():
    coap_client = await Context.create_client_context()
    request = Message(code=Code.POST, uri=TARGET_ENDPOINT + target_alarm_uri)
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


async def main():
    await change_light_state()
    #await change_suction_state()
    #await change_alarm_state()
    return 0

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    #asyncio.run(main())

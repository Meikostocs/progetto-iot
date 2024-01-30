import logging
import asyncio
from aiocoap import *
import json
import datetime
from process.all_server_coap import main as all_server_coap
import client.coap_put_client as coap_put_client
from model.light_statuses import LightStatuses
from request.light_request import LightRequestDescriptor

async def get_current_time():
    return datetime.datetime.now().time()
async def set_light_time():
    while True:
        current_time = await get_current_time()
        #current_time = datetime.datetime.now().time()
        if datetime.time(8, 0) <= current_time < datetime.time(13, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_HIGH)
        elif datetime.time(13, 0) <= current_time < datetime.time(15, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_LOW)
        elif datetime.time(15, 0) <= current_time < datetime.time(20, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_MEDIUM)
        elif datetime.time(20, 0) <= current_time < datetime.time(22, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_LOW)
        else:
            await coap_put_client.set_light_state(LightRequestDescriptor.TURN_OFF)

        await asyncio.sleep(2)
async def main():
    await set_light_time()
    #asyncio.create_task(all_server_coap())



if __name__ == "__main__":
    asyncio.run(main())

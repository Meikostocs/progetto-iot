import logging
import asyncio
from aiocoap import *
import json
import datetime
from process.all_server_coap import main as all_server_coap
import client.coap_put_client as coap_put_client
from request.light_request import LightRequestDescriptor
from request.suction_request import SuctionRequestDescriptor
import client.coap_post_client as coap_post_client

import random

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

        await asyncio.sleep(3600) #ogni ora

async def activate_suction_fan():
    humidity_threshold = 60 #%
    high_humidity = 70
    pm10_threshold = 20 #µg/m³
    pm10_medium = 40
    pm10_high= 50

    while True:
        current_humidity = random.randint(30, 70)  # andrebbe vista con mqtt consumer
        current_pm10 = random.randint(10,50)
        print(f'current humidity: {current_humidity}')
        print(f'current pm10: {current_pm10}')
        if current_humidity >= high_humidity or current_pm10 >= pm10_high:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_HIGH)
        elif current_pm10 >= pm10_medium:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_MEDIUM)
        elif current_humidity >= humidity_threshold or current_pm10 >= pm10_threshold:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_LOW)
        else:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_OFF)

        await asyncio.sleep(300) #aspetta 5 minuti

async def switch_alarm():
    while True:

        CO2_min =
        CO2_max =
        EtCO2_min =
        EtCO2_max =
        SpO2_min =
        SpO2_min =
        RESP_max =

        temp_max=

        heart_rate_min =
        heart_rate_max =
        NIBP_min =
        NIBP_max =
        IBP_min =
        IBP_max =
        ECG_min =
        ECG_max =
        pressure_avarage_min =
        pressure_avarage_max =

        Temperature_min =
        Temperature_max =
        Battery_min =
        Battery_max =

        '''
        Monitor respirazione:
        CO2 =
        EtCO2 =
        SpO2 =
        RESP =
        
        Monitor infusione:
        temp = 
        
        Monitor Cuore:
        heart_rate = 
        NIBP = 
        IBP = 
        ECG =
        pressure_avarage = 
        
        Environment Monitoring :
        Temperature =
        Battery =
        '''
        #consumer MQTT, LEGGO PARAMENTRI
        #GET..
        return 0    #get_..


async def main():
    tasks = [set_light_time(), activate_suction_fan()]
    await asyncio.gather(*tasks)
    #asyncio.create_task(all_server_coap())



if __name__ == "__main__":
    asyncio.run(main())

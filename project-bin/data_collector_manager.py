import sys
sys.path.append("./")
sys.path.append("./process")
sys.path.append("./resources")
import threading
import client.coap_put_client as coap_put_client
from dcm_class.breathing_monitor_manager import BreathingMonitorManager 
from dcm_class.infusion_monitor_manager import InfusionMonitorManager
from dcm_class.heart_monitor_manager import HeartMonitorManager
from dcm_class.EM_manager import EmManager
import random
import asyncio
import datetime
from request.light_request import LightRequestDescriptor
from request.suction_request import SuctionRequestDescriptor

'''
async def activate_suction_fan():
    humidity_threshold = 60 #%
    high_humidity = 70
    pm10_threshold = 20 #µg/m³
    pm10_medium = 40
    pm10_high= 50

    while True:
        current_humidity = random.randint(30, 70) #andrebbe vista con mqtt consumer
        current_pm10 = random.randint(10,50)
        print(f'current humidity: {current_humidity}')
        print(f'current pm10: {current_pm10}')
        if current_humidity >= high_humidity or current_pm10 >= pm10_high:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_HIGH,'A1','1')
        elif current_pm10 >= pm10_medium:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_MEDIUM,'A1','1')
        elif current_humidity >= humidity_threshold or current_pm10 >= pm10_threshold:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_LOW,'A1','1')
        else:
            await coap_put_client.set_suction_state(SuctionRequestDescriptor.SUCTION_OFF,'A1','1')

        await asyncio.sleep(300) #5 minutes
'''

async def get_current_time():
    return datetime.datetime.now().time()

async def set_light_time():
    while True:
        current_time = await get_current_time()
        if datetime.time(8, 0) <= current_time < datetime.time(13, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_HIGH )
        elif datetime.time(13, 0) <= current_time < datetime.time(15, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_LOW)
        elif datetime.time(15, 0) <= current_time < datetime.time(20, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_MEDIUM)
        elif datetime.time(20, 0) <= current_time < datetime.time(22, 0):
            await coap_put_client.set_light_state(LightRequestDescriptor.LIGHT_LOW)
        else:
            await coap_put_client.set_light_state(LightRequestDescriptor.TURN_OFF)

        await asyncio.sleep(3600)


async def switch_alarm(id_room,id_bed,status):
    await coap_put_client.set_alarm_state(status,id_room,id_bed)

async def switch_fan_state(id_room,id_bed,status):
    await coap_put_client.set_suction_state(status,id_room,id_bed)


def breathing_monitor_thread_handler():
    BreathingMonitorManager(alarm_handler=switch_alarm).run()

def infusion_monitor_thread_handler():
    InfusionMonitorManager(alarm_handler=switch_alarm).run()

def heart_monitor_thread_handler():
    HeartMonitorManager(alarm_handler=switch_alarm).run()

def EM_monitor_thread_handler():
    EmManager(alarm_handler=switch_fan_state).run()

def set_light_time_handler():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(set_light_time())
    loop.close()
'''

def activate_suction_fan_handler():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activate_suction_fan())
    loop.close()
'''

async def main():
    infusion_monitor_thread = threading.Thread(target=infusion_monitor_thread_handler).start()
    breathing_monitor_thread = threading.Thread(target=breathing_monitor_thread_handler).start()
#    set_light_time_thread = threading.Thread(target=set_light_time_handler).start()
#   activate_suction_fan_thread = threading.Thread(target=activate_suction_fan_handler).start()
    heart_monitor_thread = threading.Thread(target=heart_monitor_thread_handler).start()
    EM_monitor_thread = threading.Thread(target=EM_monitor_thread_handler).start()


if __name__ == "__main__":
    asyncio.run(main())

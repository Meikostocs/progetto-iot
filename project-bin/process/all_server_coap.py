import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
import sys
sys.path.append("../resources")
sys.path.append('../')
from alarm_actuator_resource import AlarmActuatorResource
from light_actuator_resource import LightActuatorResource
from suction_actuator_resource import SuctionActuatorResource
from oxygenation_actuator_resource import OxygenationActuatorResource

logging.basicConfig(level=logging.ERROR) #debug,info
logging.getLogger("coap-server").setLevel(logging.ERROR) #debug,info

def main():

    light_smart_obj = "light-smart-obj0001"

    root = resource.Site()
    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation', 'light'], LightActuatorResource(light_smart_obj))
    root.add_resource(['actuation','A1','1', 'suction'], SuctionActuatorResource(id_room='A1', id_bed='1'))
    root.add_resource(['actuation','A1','1','alarm'],AlarmActuatorResource(id_room='A1',id_bed='1'))
    root.add_resource(['actuation','A1','1','oxygenation'], OxygenationActuatorResource(room_id='A1', bed_id='1'))

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
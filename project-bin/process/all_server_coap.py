import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
import sys
sys.path.append("../resources")
sys.path.append('../')
from resources.alarm_actuator_resource import AlarmActuatorResource
from resources.light_actuator_resource import LightActuatorResource
from resources.suction_actuator_resource import SuctionActuatorResource
from resources.oxygenation_actuator_resource import OxygenationActuatorResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.INFO)
#logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    alarm_switch="alarm-switch"
    light_smart_obj = "light-smart-obj0001"
    suction_fan = "suction-fan0001"
    oxygenation_a1_1 = 'oxygenation-A1-1'
    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation','alarm'],AlarmActuatorResource(alarm_switch))
    root.add_resource(['actuation', 'light'], LightActuatorResource(light_smart_obj))
    root.add_resource(['actuation', 'suction'], SuctionActuatorResource(suction_fan))
    root.add_resource(['actuation', 'oxygenation'], OxygenationActuatorResource(oxygenation_a1_1))
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
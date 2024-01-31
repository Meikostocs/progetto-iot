import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
import sys
sys.path.append("../resources")
sys.path.append('../')
from resources.oxygenation_actuator_resource import OxygenationActuatorResource

logging.basicConfig(level=logging.ERROR) #debug,info
logging.getLogger("coap-server").setLevel(logging.ERROR) #debug,info

def main():

    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation','A1','1','oxygenation'], OxygenationActuatorResource(room_id='A1', bed_id='1'))

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
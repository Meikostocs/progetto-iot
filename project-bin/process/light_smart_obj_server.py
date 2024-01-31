import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.light_actuator_resource import LightActuatorResource


logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.INFO)


def main():

    light_smart_obj="light-smart-obj0001"

    # Resource tree creation
    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation','light'], LightActuatorResource(light_smart_obj))
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
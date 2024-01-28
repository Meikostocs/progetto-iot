import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.suction_actuator_resource import SuctionActuatorResource


logging.basicConfig(level=logging.INFO)
#logging.getLogger("coap-server").setLevel(logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():

    suction_fan="suction-fan0001"

    # Resource tree creation
    root = resource.Site()

    #root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation','suction'],SuctionActuatorResource(suction_fan))
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
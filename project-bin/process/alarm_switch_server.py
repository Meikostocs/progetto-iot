import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.alarm_actuator_resource import AlarmActuatorResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    root = resource.Site()

    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['actuation', 'A1', '1', 'alarm'], AlarmActuatorResource(id_room='A1', id_bed='1'))

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
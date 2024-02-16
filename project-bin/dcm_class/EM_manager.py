import json
import sys
sys.path.append("../")
sys.path.append("../model")
from conf.mqtt_conf_167108 import MqttConfigurationParameters
from model.enviorement_monitoring_sensor import EnviorementMonitoringSensor
from model.console import Console
from model.mqtt_subscriber import MQTTSubscriber
import asyncio
from request.alarm_request import AlarmRequestDescriptor
from client.coap_get_client import get_coap_alarm

class EmManager:

    def __init__(self, alarm_handler=None):

        self.console = Console(debug=True)
        self.EM_id = "python-EM-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
        self.topic = "{0}/+/+/{1}/{2}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            MqttConfigurationParameters.TELEMETRY_TOPIC,
            MqttConfigurationParameters.ENVIORMENT_MONITOR_TOPIC
        )

        self.alarm_handler = alarm_handler

        self.mqtt_subscriber = MQTTSubscriber(
            broker_address=MqttConfigurationParameters.BROKER_ADDRESS,
            broker_port=MqttConfigurationParameters.BROKER_PORT,
            subscriber_id=self.EM_id,
            topic=self.topic,
            on_connect_handler=self.on_connect,
            on_message_handler=self.on_message
        )

    def run(self):
        self.mqtt_subscriber.start_connection()

    def on_connect(self, client, userdata, flags, rc):
        self.console.print("Connected with result code " + str(rc))
        self.mqtt_subscriber.subscribe_to_topic()

    def on_message(self, client, userdata, message):
        message_payload = str(message.payload.decode("utf-8"))
        self.console.print("Telemtry Data Published")
        self.console.debug(f'Payload: {message_payload}')

        measured_value = json.loads(message_payload)
        id_room = measured_value['room_id']
        id_bed = measured_value['bed_id']
        temperature_measurement = measured_value['temperature']
        humidity_measurement = measured_value['humidity']
        PM10_measurement = measured_value['PM10']
        battery_level = measured_value['battery']['level']

        EM_sensor = EnviorementMonitoringSensor(room_id=id_room,
                                                bed_id=id_bed,
                                                temperature=temperature_measurement,
                                                humidity=humidity_measurement,
                                                PM10=PM10_measurement,
                                                battery=battery_level
                                             )

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        fan = loop.run_until_complete(get_coap_alarm(f'coap://127.0.0.1:5683/actuation/{id_room}/{id_bed}/suction'))
        loop.close()


        if EM_sensor.air_quality_check()!=fan["suction_state"]:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.alarm_handler(id_room, id_bed, EM_sensor.air_quality_check()))
            loop.close()





import json
import sys

sys.path.append("./")
sys.path.append("./model")
# Configuration files
from conf.mqtt_conf_166317 import MqttConfigurationParameters
# Custom models
from model.breathing_monitor import BreathingMonitor
from model.console import Console
from model.mqtt_subscriber import MQTTSubscriber
import logging
import asyncio
import aiocoap
from aiocoap import *
from request.oxygenation_request import OxygenationRequest
from request.alarm_request import AlarmRequestDescriptor
from client.coap_put_client import set_oxygenator_state


class BreathingMonitorManager:

    def __init__(self, alarm_handler=None):

        self.console = Console(debug=True)
        self.breathing_monitor_id = "python-breathing-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
        self.topic = "{0}/+/+/{1}/{2}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            MqttConfigurationParameters.TELEMETRY_TOPIC,
            MqttConfigurationParameters.BREATHING_MONITOR_TOPIC
        )
        self.alarm = False
        self.had_oxygen_problem = False

        self.mqtt_subscriber = MQTTSubscriber(
            broker_address=MqttConfigurationParameters.BROKER_ADDRESS,
            broker_port=MqttConfigurationParameters.BROKER_PORT,
            subscriber_id=self.breathing_monitor_id,
            topic=self.topic,
            on_connect_handler=self.on_connect,
            on_message_handler=self.on_message
        )
        self.alarm_handler = alarm_handler

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
        id_room = measured_value['breathing_monitor_descriptor']['id_room']
        id_bed = measured_value['breathing_monitor_descriptor']['id_bed']
        spo2_measurement = measured_value['breathing_monitor_telemetry_data']['SpO2']['measurement']
        resp_measurement = measured_value['breathing_monitor_telemetry_data']['RESP']['measurement']
        co2_measurement = measured_value['breathing_monitor_telemetry_data']['CO2']['measurement']
        co2_unit = measured_value['breathing_monitor_telemetry_data']['CO2']['unit']
        etco2_concentration = measured_value['breathing_monitor_telemetry_data']['EtCO2']['concentration']
        etco2_pressure = measured_value['breathing_monitor_telemetry_data']['EtCO2']['pressure']
        battery_level = measured_value['breathing_monitor_telemetry_data']['battery']['level']

        breathing_monitor = BreathingMonitor(id_room=id_room,
                                             id_bed=id_bed,
                                             spo2_measurement=spo2_measurement,
                                             resp_measurement=resp_measurement,
                                             co2_measurement=co2_measurement,
                                             co2_unit=co2_unit,
                                             etco2_concentration=etco2_concentration,
                                             etco2_pressure=etco2_pressure,
                                             battery_level=battery_level
                                             )

        if breathing_monitor.critical_status():
            self.console.print(f'CRITICAL SITUATION AT {id_room}-{id_bed} BREATHING MONITOR')
            if not self.alarm:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.alarm_handler(id_room, id_bed, AlarmRequestDescriptor.ALARM_ON))
                loop.close()
            self.alarm = True
        elif self.alarm:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.alarm_handler(id_room, id_bed, AlarmRequestDescriptor.ALARM_OFF))
            loop.close()
            self.alarm = False


        if breathing_monitor.breathing_monitor_telemetry_data.SpO2.critical_status():
            self.console.print(f"CRITICAL SITUATION AT {id_room}-{id_bed} SPO2")
            if not self.had_oxygen_problem:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.activate_emergency_oxygenation(breathing_monitor))
                loop.close()
                self.had_oxygen_problem = True
        elif self.had_oxygen_problem:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.activate_emergency_oxygenation(breathing_monitor))
            loop.close()
            self.had_oxygen_problem = False

    async def activate_emergency_oxygenation(self, breathing_monitor):
        level = breathing_monitor.breathing_monitor_telemetry_data.SpO2.needed_oxygen()
        await set_oxygenator_state(level,
                                   id_room=breathing_monitor.breathing_monitor_descriptor.id_room,
                                   id_bed=breathing_monitor.breathing_monitor_descriptor.id_bed)

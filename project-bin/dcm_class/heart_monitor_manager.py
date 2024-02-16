import json
import sys
sys.path.append("../")
sys.path.append("../model")
from conf.mqtt_conf_167108 import MqttConfigurationParameters
from model.heart_monitor import HeartMonitor
from model.console import Console
from model.mqtt_subscriber import MQTTSubscriber
import asyncio
from request.alarm_request import AlarmRequestDescriptor
from client.coap_get_client import get_coap_alarm

class HeartMonitorManager:

    def __init__(self, alarm_handler=None):

        self.console = Console(debug=True)
        self.heart_monitor_id = "python-heart-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
        self.topic = "{0}/+/+/{1}/{2}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            MqttConfigurationParameters.TELEMETRY_TOPIC,
            MqttConfigurationParameters.HEART_MONITOR_TOPIC
        )

        self.alarm = False
        self.mqtt_subscriber = MQTTSubscriber(
            broker_address=MqttConfigurationParameters.BROKER_ADDRESS,
            broker_port=MqttConfigurationParameters.BROKER_PORT,
            subscriber_id=self.heart_monitor_id,
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
        id_room = measured_value['heart_monitor_descriptor']['id_room']
        id_bed = measured_value['heart_monitor_descriptor']['id_bed']
        ECG_measurement = measured_value['heart_monitor_telemetry_data']['ECG']['ecg_signal']
        heart_rate_measurement = measured_value['heart_monitor_telemetry_data']['heart_rate']['bpm']
        IBP_pressure1_measurement = measured_value['heart_monitor_telemetry_data']['IBP']['pressure1']
        IBP_pressure2_measurement = measured_value['heart_monitor_telemetry_data']['IBP']['pressure2']
        NIBP_diastolic_concentration = measured_value['heart_monitor_telemetry_data']['NIBP']['pressure_diastolic']
        NIBP_sistolic_concentration = measured_value['heart_monitor_telemetry_data']['NIBP']['pressure_sistolic']
        pressure_avg_pressure = measured_value['heart_monitor_telemetry_data']['pressure_avg']['pressure']
        battery_level = measured_value['heart_monitor_telemetry_data']['battery']['level']

        heart_monitor = HeartMonitor(id_room=id_room,
                                             id_bed=id_bed,
                                             ecg_measurement=ECG_measurement,
                                             heart_rate_measurement=heart_rate_measurement,
                                             ibp_pressure1_measurement=IBP_pressure1_measurement,
                                             ibp_pressure2_measurement=IBP_pressure2_measurement,
                                             nibp_diastolic_measurement=NIBP_diastolic_concentration,
                                             nibp_sistolic_measurement=NIBP_sistolic_concentration,
                                             pressure_avg_measurement=pressure_avg_pressure,
                                             battery_level=battery_level
                                             )

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        alarm_status = loop.run_until_complete(get_coap_alarm(f'coap://127.0.0.1:5683/actuation/{id_room}/{id_bed}/alarm'))
        loop.close()



        if heart_monitor.critical_status():
            if alarm_status['alarm_state'] == 'off':
                self.console.print(f'CRITICAL SITUATION AT {id_room}-{id_bed} HEART MONITOR')
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.alarm_handler(id_room, id_bed, AlarmRequestDescriptor.ALARM_ON))
                loop.close()
            self.alarm = True

        elif self.alarm:
            if alarm_status['alarm_state'] == 'on':
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.alarm_handler(id_room, id_bed, AlarmRequestDescriptor.ALARM_OFF))
                loop.close()
            self.alarm = False




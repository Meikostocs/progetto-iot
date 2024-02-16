import time
import json
import sys

sys.path.append("../")
sys.path.append("../model")
from conf.mqtt_conf_167108 import MqttConfigurationParameters
from model.heart_monitor import HeartMonitor
from model.console import Console
from model.mqtt_publisher import MQTTPublisher


def on_connect(client, userdata, flags, rc):
    console.print(f"Connected with {str(rc)} status code")


def send_messages(message_limit):
    for message_id in range(message_limit):
        heart_monitor.update_measurements()
        device_payload_string = heart_monitor.to_json()
        mqtt_publisher.publish(device_payload_string)
        console.print("Telemetry Data Published")
        console.debug(f'Topic: {target_topic}')
        console.debug(f'Payload: {device_payload_string}')
        time.sleep(3)


# Init breathing monitor and console
heart_monitor = HeartMonitor('A1', '1')
console = Console(debug=True)
heart_monitor_id = "python-heart_monitor-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
target_topic = "{0}/{1}/{2}/{3}/{4}".format(
    MqttConfigurationParameters.MQTT_BASIC_TOPIC,
    heart_monitor.heart_monitor_descriptor.id_room,
    heart_monitor.heart_monitor_descriptor.id_bed,
    MqttConfigurationParameters.TELEMETRY_TOPIC,
    MqttConfigurationParameters.HEART_MONITOR_TOPIC)

mqtt_publisher = MQTTPublisher(
    broker_address=MqttConfigurationParameters.BROKER_ADDRESS,
    broker_port=MqttConfigurationParameters.BROKER_PORT,
    publisher_id=heart_monitor_id,
    topic=target_topic,
    on_connect_handler=on_connect,
    qos=2)

mqtt_publisher.start_connection()

send_messages(1000)

import paho.mqtt.client as mqtt
import time
import json

import sys
sys.path.append("./")
sys.path.append("./model")

#Configuration files
from conf.mqtt_conf_166317 import MqttConfigurationParameters
#Custom models
from model.breathing_monitor import BreathingMonitor
from model.console import Console



def on_connect(client, userdata, flags, rc):
    console.print(f"Connected with {str(rc)} status code")


def publish_telemetry_data():

    target_topic = "{0}/{1}/{2}/{3}/{4}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            breathing_monitor.breathing_monitor_descriptor.id_room ,
            breathing_monitor.breathing_monitor_descriptor.id_bed,
            MqttConfigurationParameters.TELEMETRY_TOPIC,
            MqttConfigurationParameters.BREATHING_MONITOR_TOPIC)

    device_payload_string = breathing_monitor.to_json()
    # Publish with QoS=2
    mqtt_client.publish(topic=target_topic,payload=device_payload_string, qos=2, retain=False)
    
    console.print("Telemtry Data Published")
    console.debug(f'Topic: {target_topic}')
    console.debug(f'Payload: {device_payload_string}')



# Init breathing monitor and console
breathing_monitor = BreathingMonitor('A1','1')
console = Console(debug=True)

# Configuration variables
brathing_monitor_id = "python-breathing_monitor-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
message_limit = 1000

#Create MQTT Client
mqtt_client            = mqtt.Client(brathing_monitor_id)
mqtt_client.on_connect = on_connect

# Set Account Username & Password
#mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

console.print("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + ":" + str(MqttConfigurationParameters.BROKER_PORT))

mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)
mqtt_client.loop_start()


for message_id in range(message_limit):
    breathing_monitor.update_measurements()
    publish_telemetry_data()
    time.sleep(3)

mqtt_client.loop_stop()
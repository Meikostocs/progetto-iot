import paho.mqtt.client as mqtt
import json

import sys
sys.path.append("./")
sys.path.append("./model")

#Configuration files
from conf.mqtt_conf_166317 import MqttConfigurationParameters
#Custom models
from model.infusion_monitor import InfusionMonitor
from model.console import Console



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    console.print("Connected with result code " + str(rc))

    device_telemetry_topic = "{0}/+/+/{1}/{2}".format(
                    MqttConfigurationParameters.MQTT_BASIC_TOPIC,
                    MqttConfigurationParameters.TELEMETRY_TOPIC,
                    MqttConfigurationParameters.INFUSION_MONITOR_TOPIC)

    mqtt_client.subscribe(device_telemetry_topic)

    console.print("Subscribed to: " + device_telemetry_topic)


# Define a callback method to receive asynchronous messages
def on_message(client, userdata, message):
    message_payload = str(message.payload.decode("utf-8"))
    console.print("Telemtry Data Published")
    console.debug(f'Payload: {message_payload}')


# Configuration variables
console = Console(debug=True)
infusion_monitor_id = "python-infusion_monitor-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)

mqtt_client = mqtt.Client(infusion_monitor_id)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


# Set Account Username & Password
#mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

console.debug("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + " port: " + str(MqttConfigurationParameters.BROKER_PORT))
mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)

mqtt_client.loop_forever()
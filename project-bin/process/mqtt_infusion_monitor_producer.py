import paho.mqtt.client as mqtt
import time
import json

import sys
sys.path.append("./")
sys.path.append("./model")

#Configuration files
from conf.mqtt_conf_166317  import MqttConfigurationParameters
#Custom models
from model.infusion_monitor import InfusionMonitor
from model.console          import Console
from model.mqtt_publisher   import MQTTPublisher 


def on_connect(client, userdata, flags, rc):
    console.print(f"Connected with {str(rc)} status code")

def send_messages(message_limit):
    for message_id in range(message_limit):
        infusion_monitor.update_measurements()
        device_payload_string = infusion_monitor.to_json()
        mqtt_publisher.publish(device_payload_string)
        console.print("Telemtry Data Published")
        console.debug(f'Topic: {topic}')
        console.debug(f'Payload: {infusion_monitor.to_json()}')
        time.sleep(3)
        



# Init breathing monitor and console
infusion_monitor = InfusionMonitor('A1','1')
console = Console(debug=True)
topic = "{0}/{1}/{2}/{3}/{4}".format(
        MqttConfigurationParameters.MQTT_BASIC_TOPIC,
        infusion_monitor.infusion_monitor_descriptor.id_room ,
        infusion_monitor.infusion_monitor_descriptor.id_bed,
        MqttConfigurationParameters.TELEMETRY_TOPIC,
        MqttConfigurationParameters.INFUSION_MONITOR_TOPIC
    )
infusion_monitor_id = "python-infusion_monitor-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)

mqtt_publisher = MQTTPublisher(
    broker_address     = MqttConfigurationParameters.BROKER_ADDRESS,
    broker_port        = MqttConfigurationParameters.BROKER_PORT,
    publisher_id       = infusion_monitor_id,
    topic              = topic,
    on_connect_handler = on_connect,
    qos                = 2
)

mqtt_publisher.start_connection()

send_messages(message_limit=1000)

import time
import json
import sys
sys.path.append("./")
sys.path.append("./model")
#Configuration files
from conf.mqtt_conf_166317   import MqttConfigurationParameters
#Custom models
from model.breathing_monitor import BreathingMonitor
from model.console           import Console
from model.mqtt_publisher    import MQTTPublisher

def on_connect(client, userdata, flags, rc):
    console.print(f"Connected with {str(rc)} status code")

def send_messages(message_limit):
    for message_id in range(message_limit):
        breathing_monitor.update_measurements()
        device_payload_string = breathing_monitor.to_json()
        mqtt_publisher.publish(device_payload_string)
        console.print("Telemtry Data Published")
        console.debug(f'Topic: {target_topic}')
        console.debug(f'Payload: {device_payload_string}')
        time.sleep(3)


# Init breathing monitor and console
breathing_monitor = BreathingMonitor('A1','1')
console = Console(debug=True)
brathing_monitor_id = "python-breathing_monitor-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
target_topic = "{0}/{1}/{2}/{3}/{4}".format(
        MqttConfigurationParameters.MQTT_BASIC_TOPIC,
        breathing_monitor.breathing_monitor_descriptor.id_room ,
        breathing_monitor.breathing_monitor_descriptor.id_bed,
        MqttConfigurationParameters.TELEMETRY_TOPIC,
        MqttConfigurationParameters.BREATHING_MONITOR_TOPIC)

mqtt_publisher = MQTTPublisher(
    broker_address     = MqttConfigurationParameters.BROKER_ADDRESS,
    broker_port        = MqttConfigurationParameters.BROKER_PORT,
    publisher_id       = brathing_monitor_id,
    topic              = target_topic,
    on_connect_handler = on_connect,
    qos                = 2)

mqtt_publisher.start_connection()

send_messages(1000)
import sys
sys.path.append("../")
sys.path.append("../model")
from conf.mqtt_conf_167108 import MqttConfigurationParameters
from model.console import Console
from model.mqtt_subscriber import MQTTSubscriber


def on_connect(client, userdata, flags, rc):
    console.print("Connected with result code " + str(rc))
    mqtt_subscriber.subscribe_to_topic()


def on_message(client, userdata, message):
    message_payload = str(message.payload.decode("utf-8"))
    console.print("Telemtry Data Published")
    console.debug(f'Payload: {message_payload}')


console = Console(debug=True)

breathing_monitor_id = "python-heart-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
topic = "{0}/+/+/{1}/{2}".format(
    MqttConfigurationParameters.MQTT_BASIC_TOPIC,
    MqttConfigurationParameters.TELEMETRY_TOPIC,
    MqttConfigurationParameters.HEART_MONITOR_TOPIC
)

mqtt_subscriber = MQTTSubscriber(
    broker_address=MqttConfigurationParameters.BROKER_ADDRESS,
    broker_port=MqttConfigurationParameters.BROKER_PORT,
    subscriber_id=breathing_monitor_id,
    topic=topic,
    on_connect_handler=on_connect,
    on_message_handler=on_message
)

mqtt_subscriber.start_connection()

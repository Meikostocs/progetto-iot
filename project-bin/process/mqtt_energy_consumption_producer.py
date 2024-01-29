import paho.mqtt.client as mqtt
import time
from model.light_smart_obj import LightSmartObj
from conf.mqtt_conf_168194 import MqttConfigurationParameters


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {str(rc)}')

def publish_telemetry_data():
    target_topic = "{0}/{1}/{2}/{3}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            light1.room_id,
            light1.bed_id,
            MqttConfigurationParameters.TELEMETRY_TOPIC,
            MqttConfigurationParameters.ENERGY_CONSUMPTION_TOPIC)
   # device_payload_string = light1.energy_consumption_sensor.to_json()
    device_payload_string = light1.to_json()
    #device_payload_string =LightSmartObj.to_json()
    #device_payload_string = electric_vehicle_telemetry_data.to_json()

    mqtt_client.publish(target_topic, device_payload_string, 0, False)
    print(f"Telemetry Data Published: Topic: {target_topic} Payload: {device_payload_string}")

light1 = LightSmartObj(room_id="A1",bed_id=1)
message_limit = 100
mqtt_client = mqtt.Client(light1.room_id)
mqtt_client.on_connect = on_connect

# Set Account Username & Password
mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

print("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + " port: " + str(MqttConfigurationParameters.BROKER_PORT))
mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)
mqtt_client.loop_start()


publish_telemetry_data()

for message_id in range(message_limit):
    light1.update_energy_consumption()
    publish_telemetry_data()
    time.sleep(3)

mqtt_client.loop_stop()

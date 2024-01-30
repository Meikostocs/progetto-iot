import json
import sys
sys.path.append("./")
sys.path.append("./model")
#Configuration files
from conf.mqtt_conf_166317  import MqttConfigurationParameters
#Custom models
from model.breathing_monitor import BreathingMonitor
from model.console           import Console
from model.mqtt_subscriber   import MQTTSubscriber

class BreathingMonitorManager:

    def __init__(self):

        self.console = Console(debug=True)
        self.breathing_monitor_id = "python-breathing-subscriber-{0}".format(MqttConfigurationParameters.MQTT_USERNAME)
        self.topic                = "{0}/+/+/{1}/{2}".format(
                            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
                            MqttConfigurationParameters.TELEMETRY_TOPIC,
                            MqttConfigurationParameters.BREATHING_MONITOR_TOPIC
                            )

        self.mqtt_subscriber = MQTTSubscriber(
            broker_address     = MqttConfigurationParameters.BROKER_ADDRESS,
            broker_port        = MqttConfigurationParameters.BROKER_PORT,
            subscriber_id      = self.breathing_monitor_id,
            topic              = self.topic,
            on_connect_handler = self.on_connect,
            on_message_handler = self.on_message
        )


    def run(self):
        self.mqtt_subscriber.start_connection()

    def on_connect(self,client, userdata, flags, rc):
        self.console.print("Connected with result code " + str(rc))
        self.mqtt_subscriber.subscribe_to_topic()


    def on_message(self,client, userdata, message):
        message_payload = str(message.payload.decode("utf-8"))
        self.console.print("Telemtry Data Published")
        self.console.debug(f'Payload: {message_payload}')

        measured_value = json.loads(message_payload)

        breathing_monitor = BreathingMonitor(id_room=measured_value['breathing_monitor_descriptor']['id_room'],
                            id_bed=measured_value['breathing_monitor_descriptor']['id_bed'],
                            spo2_measurement=measured_value['breathing_monitor_telemetry_data']['SpO2']['measurement'],
                            resp_measurement=measured_value['breathing_monitor_telemetry_data']['RESP']['measurement'],
                            co2_measurement=measured_value['breathing_monitor_telemetry_data']['CO2']['measurement'],
                            co2_unit=measured_value['breathing_monitor_telemetry_data']['CO2']['unit'],
                            etco2_concentration=measured_value['breathing_monitor_telemetry_data']['EtCO2']['concentration'],
                            etco2_pressure=measured_value['breathing_monitor_telemetry_data']['EtCO2']['pressure'],
                            battery_level=measured_value['breathing_monitor_telemetry_data']['battery']['level']
                            )     
        if breathing_monitor.critical_status():
            self.console.print("someone is dieing")





    
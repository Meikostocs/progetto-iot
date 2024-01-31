import paho.mqtt.client as mqtt


class MQTTPublisher:

    def __init__(self, broker_address, broker_port, publisher_id, topic, on_connect_handler, retain=False, qos=0):
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.publisher_id = publisher_id
        self.qos = qos
        self.topic = topic
        self.retain = retain
        self.on_connect_handler = on_connect_handler
        self.mqtt_client = None

    def start_connection(self):
        self.mqtt_client = mqtt.Client(self.publisher_id)
        self.mqtt_client.on_connect = self.on_connect_handler
        self.mqtt_client.connect(self.broker_address, self.broker_port)
        self.mqtt_client.loop_start()

    def publish(self, payload):
        """
            Publish data
            :param payload
            :type payload JSON Encoded string
        """
        self.mqtt_client.publish(topic=self.topic, payload=payload, qos=self.qos, retain=self.retain)

    def stop(self):
        self.mqtt_client.loop_stop()

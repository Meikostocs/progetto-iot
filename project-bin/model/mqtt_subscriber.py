import paho.mqtt.client as mqtt


class MQTTSubscriber:

    def __init__(self, broker_address, broker_port, subscriber_id, topic, on_connect_handler, on_message_handler):
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.subscriber_id = subscriber_id
        self.topic = topic
        self.on_connect_handler = on_connect_handler
        self.on_message_handler = on_message_handler
        self.mqtt_client = None

    def start_connection(self):
        self.mqtt_client = mqtt.Client(self.subscriber_id)
        self.mqtt_client.on_connect = self.on_connect_handler
        self.mqtt_client.on_message = self.on_message_handler
        self.mqtt_client.connect(self.broker_address, self.broker_port)
        self.mqtt_client.loop_forever()

    def subscribe_to_topic(self, topic=None):
        if topic is None:
            topic = self.topic
        self.mqtt_client.subscribe(topic)

    def stop(self):
        self.mqtt_client.loop_stop()

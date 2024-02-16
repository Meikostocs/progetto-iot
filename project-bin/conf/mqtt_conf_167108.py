class MqttConfigurationParameters(object):

    BROKER_ADDRESS = "broker.hivemq.com"
    BROKER_PORT = 1883
    MQTT_USERNAME = "303550@studenti.unimore.it"
    MQTT_PASSWORD = "vmqpthsvezavnhvn"
    #MQTT_BASIC_TOPIC = "/iot/user/{0}".format(MQTT_USERNAME)
    MQTT_BASIC_TOPIC = f'/iot/user/{MQTT_USERNAME}'
    TELEMETRY_TOPIC = "telemetry"
    HEART_MONITOR_TOPIC ="heart_monitor"
    ENVIORMENT_MONITOR_TOPIC  ="enviorment_monitor"
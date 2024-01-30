class MqttConfigurationParameters(object):

    BROKER_ADDRESS = "broker.hivemq.com"
    BROKER_PORT = 1883
    MQTT_USERNAME = "304579@studenti.unimore.it"
    MQTT_PASSWORD = "vmqpthsvezavnhvn"
    #MQTT_BASIC_TOPIC = "/iot/user/{0}".format(MQTT_USERNAME)
    MQTT_BASIC_TOPIC = f'/iot/user/{MQTT_USERNAME}'
    TELEMETRY_TOPIC = "telemetry"
    BREATHING_MONITOR_TOPIC ="breathing_monitor"
    INFUSION_MONITOR_TOPIC  ="infusion_monitor"
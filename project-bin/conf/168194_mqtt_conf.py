class MqttConfigurationParameters(object):
    #Basic_topic/room_id/bed_id/telemetry/light_energy_consumption
    BROKER_ADDRESS = "155.185.228.20"
    BROKER_PORT = 7883
    MQTT_USERNAME = "309309@studenti.unimore.it"
    MQTT_PASSWORD = "tknoqlgpvzusilfc"
    #MQTT_BASIC_TOPIC = "/iot/user/{0}".format(MQTT_USERNAME)
    MQTT_BASIC_TOPIC = f'/iot/user/{MQTT_USERNAME}'
    TELEMETRY_TOPIC = "telemetry"
    ROOM_ID_TOPIC = "<room_id>"
    BED_ID_TOPIC = "<bed_id>"
    ENERGY_CONSUMPTION_TOPIC ="light_energy_consumption"
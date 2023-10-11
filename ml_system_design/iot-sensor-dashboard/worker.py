# worker.py
import paho.mqtt.client as mqtt
import json
import random
import time

mqtt_client = mqtt.Client()
mqtt_client.connect('mqtt-broker', 1883, 60)

while True:
    sensor_data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2),
    }
    mqtt_client.publish('sensor_data_topic', json.dumps(sensor_data))
    time.sleep(5)

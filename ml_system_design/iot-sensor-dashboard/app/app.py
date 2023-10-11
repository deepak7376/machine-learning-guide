# app/app.py
from flask import Flask, render_template
import redis
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
mqtt_client = mqtt.Client()

@app.route('/')
def dashboard():
    sensor_data = redis_client.lrange('sensor_data', 0, -1)
    sensor_data = [json.loads(data.decode()) for data in sensor_data]
    return render_template('dashboard.html', sensor_data=sensor_data)

def on_connect(client, userdata, flags, rc):
    client.subscribe('sensor_data_topic')

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    redis_client.rpush('sensor_data', json.dumps(data))

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect('mqtt-broker', 1883, 60)

if __name__ == '__main__':
    mqtt_client.loop_start()
    app.run(host='0.0.0.0', debug=True)

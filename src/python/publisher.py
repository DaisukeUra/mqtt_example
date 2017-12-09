from time import sleep
from time import time
from datetime import datetime
import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 13232
topic = 'iktakahiro/a'
request_topic = 'iktakahiro/request'


def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))


client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(host, port=port, keepalive=60)

client.on_connect = on_connect

for i in range(5):
    dt = datetime.now()
    client.publish(topic, dt.second + dt.microsecond * 1e-6)
    sleep(0.1)

client.publish(request_topic, 11)

client.disconnect()

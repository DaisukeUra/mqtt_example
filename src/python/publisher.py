from time import sleep
import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 13232
topic = 'test_topic/a'
_qos = 2
request_topic = 'test_topic/request'


client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(host, port=port, keepalive=60)


for i in range(500):
    client.publish(topic, 1, qos=_qos)
    sleep(0.01)

sleep(0.1)
client.publish(request_topic, True, qos=_qos)

client.loop_forever()

client.disconnect()

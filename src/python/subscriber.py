import paho.mqtt.client as mqtt


host = '127.0.0.1'
port = 13232
topic = 'test_topic/a'
_qos = 2
request_topic = 'test_topic/request'


class MQTT_SUBSCRIBER(object):

    def __init__(self):
        self._data = []

        self.client = mqtt.Client(protocol=mqtt.MQTTv311)

        self.client.on_connect = self.on_connect
        self.client.message_callback_add(topic, self.on_message)
        self.client.message_callback_add(request_topic, self.on_request)

        self.client.connect(host, port=port, keepalive=60)

    def on_connect(self, client, userdata, flags, respons_code):
        print('status {0}'.format(respons_code))

        self.client.subscribe("test_topic/#", _qos)

    def on_message(self, client, userdata, msg):
        self._data.append(msg.payload)

    def on_request(self, client, userdata, msg):
        print(self._data)
        print("Num: " + str(len(self._data)))
        self._data = []


if __name__ == '__main__':

    subscriber = MQTT_SUBSCRIBER()

    subscriber.client.loop_forever()

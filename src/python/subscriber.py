import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 13232
topic = 'iktakahiro/a'
request_topic = 'iktakahiro/request'

_data = []

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))

    client.subscribe(topic)

def on_connect_request(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))

    client.subscribe(request_topic)

def on_message(client, userdata, msg):
    global _data
    _data.append(msg.payload)

def on_request(client, userdata, msg):
    global _data
    print(_data)
    _data = []

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message

    request_client = mqtt.Client(protocol=mqtt.MQTTv311)

    request_client.on_connect = on_connect_request
    request_client.on_message = on_request

    request_client.connect(host, port=port, keepalive=60)
    client.connect(host, port=port, keepalive=60)

    while 1:
        request_client.loop()
        client.loop()

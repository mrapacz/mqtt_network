import paho.mqtt.client as mqtt
import config
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for node in config.node_ids:
        client.subscribe("nodemcu/" + node)


#
# def dump_message(message):
#     pass

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    message = msg.payload.decode()
    print(message)
    # dump_message(message)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config.host, config.port, 60)
    client.loop_forever()
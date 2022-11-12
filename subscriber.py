# importing the necessary packages
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("Recieved message: ", str(message.payload.decode("utf-8")))


mqttBroker = "104.28.251.118"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker,


client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()

import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "104.28.251.118"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    message = input("Enter the Message ")
    client.publish("Message", message)
    print("Just published " + str(message) + " to Topic Message")
    time.sleep(1)

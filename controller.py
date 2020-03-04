from keypad.keypad_utils import keypad_init as ki
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
  incoming = str(message.payload.decode("utf-8"))
broker_address = "broker.mqttdashboard.com"

foo = ki()
password = [4,5,6,7]
try:
  while True:
    keys = foo.pressed_keys
    if keys:
      if (keys == password):
        print("OMG YOU HIT THE PASSWORD")
        
  

except KeyboardInterrupt:
  pass
  #client.loop_stop()

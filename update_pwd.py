import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish 
import json
import time
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser(description="Test values or nah?")
parser.add_argument('-t', dest='test', action='store_const', const=True, default=False)
args = parser.parse_args()
mqtt_updates = "ECE/lockbox/updates/asd"
broker_address = "broker.mqttdashboard.com"

if(args.test):
  start_time = datetime.now()
  duration = timedelta(minutes=2)
  end_time = start_time+duration
  pwd = [9,8,7,6]

else:
  start_time = datetime.strptime(input("What day and hour should the password start? As 3/25/20 13 for\n 1pm march 25th of 2020 please\n"),'%m/%d/%y %H')
  duration = timedelta(hours=int(input("how many hours should it be good for?\n")))
  end_time = start_time + duration
  pwd = [int(i) for i in input("What four digit password should be used?\n")]

update = {'pwd':pwd,'min':start_time.timestamp(), 'max':end_time.timestamp()}
out = json.dumps(update)
publish.single(topic=mqtt_updates,payload=out,hostname=broker_address)

"""
client = mqtt.Client() #create new instance
client.connect(broker_address) 
client.loop_start()

try:
  while True:
    time.sleep(5)
    client.publish(mqtt_updates,out)

except KeyboardInterrupt:
  client.loop_stop()
  print("")

"""
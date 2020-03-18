from keypad import keypad
import paho.mqtt.client as mqtt
import picamera
import json
import time
import threading
import RPi.GPIO as GPIO
from lock import lock
from tran_message import send_email

def on_message(client, userdata, message):
  if(message.topic == mqtt_pwd_update_t):
    password_list_update(str(message.payload.decode("utf-8")))
  else:
    incoming = str(message.payload.decode("utf-8"))
    print(incoming)
  
  
def password_list_update(incoming):
  update = json.loads(incoming)
  password_list.append((update['pwd'],update['min'],update['max']))

def valid_pwd(input):
  now = time.time()
  for entry in password_list:
    if(input == entry[0] and (now > entry[1] and now < entry[2] or entry[1] == entry[2] == 0)):
      return True
  return False

broker_address = "broker.mqttdashboard.com"
mqtt_pwd_update_t = "ECE/lockbox/updates/asd"
foo = keypad()
password_list = [([4,5,6,7],0,0),([7,7,7,7],0,0)]
client = mqtt.Client()
client.on_message=on_message 
client.connect(broker_address) 
client.loop_start()
client.subscribe(mqtt_pwd_update_t)


def email_owner(body_text):
  send_email(
          sender="Tran <trann23@seattleu.edu>"
        , recipients=['chandlerzach@seattleu.edu']
        , subject = "Lockbox notice!"
        , body_text = body_text)

#literal_lock = lock()
def p(string):
  print(string)

try:
  count_attempts = 0
  allowed_attempts = 2
  start_time = time.time()
  reset_time = 4
  start_watching = 0
  lockout_end = 0
  lockout_duration = 600
  while True:
    now = time.time()
    keys = foo.pressed_keys
    if(keys):
      p(keys)
      if (valid_pwd(keys) and now > lockout_end):
        p("correct code")
        email_owner("A correct password!")
        #threading.Thread(target=literal_lock.unlock).start() 
        
      else:
        if count_attempts == 0:
          start_watching = now
        if (now > start_watching+reset_time):
          count_attempts = 0
        count_attempts +=1
        if (count_attempts >= allowed_attempts):
          lockout_end = now + lockout_duration
          email_owner(f"STOP DOING THAT bad password is{keys}")
    
    
  

except KeyboardInterrupt:
  client.loop_stop()
  GPIO.cleanup()

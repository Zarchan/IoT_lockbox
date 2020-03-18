import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
l = []
t0 = time.time()
try:
  val = GPIO.input(6)
  while True:
  
    t1 = time.time()
    while (val == GPIO.input(6)):
      pass
    val = GPIO.input(6)
    t2 = time.time()
    print(t2 - t1)
    l.append(t2-t1)
finally:
  GPIO.cleanup()
  print(max(l))
  print(min(l))
  print(len(l))
  print(time.time() - t0)
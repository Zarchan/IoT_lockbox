import RPi.GPIO as GPIO
import threading
import time
class lock():
  def __init__(self,u=23,l=24, board_mode = GPIO.BCM):
    self.u = a
    self.l = b
    self.rotate_time = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(u,GPIO.OUT)
    GPIO.output(u, 0)
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(u, 0)
    self.hw_lock = threading.Lock()
  def lock(self):
    try:
      self.hw_lock.acquire()
      GPIO.output(self.l,1)
      time.sleep(self.rotate_time)
    finally:
      GPIO.output(self.l,0)
      self.hw_lock.release()
    
  def unlock(self):
    try:
      self.hw_lock.acquire()
      GPIO.output(self.u,1)
      time.sleep(self.rotate_time)
    finally:
      GPIO.output(self.u,0)
      self.hw_lock.release()

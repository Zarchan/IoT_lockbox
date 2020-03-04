"""
Modified from code found at
https://learn.adafruit.com/matrix-keypad/python-circuitpython
"""

import time
import digitalio
import board
import adafruit_matrixkeypad

class keypad_init:
  def __init__(self):
    cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13)]
    rows = [digitalio.DigitalInOut(x) for x in (board.D19, board.D26, board.D20, board.D21)]
    keys = ((1, 2, 3),
      (4, 5, 6),
      (7, 8, 9),
      ('*', 0, '#'))
    self.keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
    self.pwd_len = 4
    self.time = time.time()
    self.time_out = 4
    self.debounce = 0.1
    self.input = []
    self.let_go = True
  
  @property
  def pressed_keys(self):
    time_now = time.time()
    if (time_now - self.time > self.time_out):
      self.input = []
      self.time = time_now

    k_in = self.keypad.pressed_keys
    if(k_in and self.let_go):
      self.input.append(k_in[0])
      self.let_go = False
      self.time = time_now

    elif(not k_in):
      self.let_go = True

    if (len(self.input) >= self.pwd_len):
      tmp = self.input[:self.pwd_len]
      self.input = []
      self.time = time_now
      return tmp

if __name__ == "__main__":
  print("Test of keyboard function")
  keypad = keypad_init()

  while True:
    keys = keypad.pressed_keys
    if keys:
      print(f"Pressed: {keys}")


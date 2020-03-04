import time
import digitalio
import board
import adafruit_matrixkeypad

cols = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13)]
rows = [digitalio.DigitalInOut(x) for x in (board.D19, board.D26, board.D20, board.D21)]

keys = ((1, 2, 3),
  (4, 5, 6),
  (7, 8, 9),
  ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

test = True
while True:
  keys = keypad.pressed_keys
  if keys:
      if test:
          print("Pressed: ", keys)
      test = False

  else:
      test = True
  time.sleep(0.1)

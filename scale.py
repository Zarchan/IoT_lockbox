#benchmarked the bit input, never takes longer than  10-20 micro seconds
#which is below the 60us low power mode
import time
import RPi.GPIO as GPIO


class scale:
  def __init__(self,DT=17,SCLK=27,GPIO_MODE=GPIO.BCM):
    self.DT = DT
    self.SCLK = SCLK
    GPIO.setmode(GPIO_MODE)
    GPIO.setup(DT, GPIO.IN)
    GPIO.setup(SCLK, GPIO.OUT)
    GPIO.output(SCLK, 0)
    
  def get_input(self):
    try:
      val = 0
      while(GPIO.input(self.DT)): #if we are ever unable to spit data then this becomes a problem
        pass
      time.sleep(1E-7)
      for i in range(24):
        GPIO.output(self.SCLK,1)
        val <<= 1
        GPIO.output(self.SCLK,0)
        val += GPIO.input(self.DT)
        
      GPIO.output(self.SCLK,1)
      GPIO.output(self.SCLK,0)
      return val

    except(KeyboardInterrupt): #maybe just one try except in the main program?
      GPIO.cleanup()

  def get_average(self,count=5):
    average = 0
    for i in range(count):
      average += self.get_input()
    return average/count
  
  def tare(self):
    count = 5
    avg = [self.get_average() for i in range(count)]
    test = all([abs(i-k) <= k*0.01 for i in avg for k in avg]) #checking if all values are within 1% of each other
    try:
      while(not test):
        avg = [self.get_average() for i in range(5)]
        test = all([abs(i-k) <= k*0.01 for i in avg for k in avg])
    except(KeyboardInterrupt):
      print("Interrupted while taring")
      GPIO.cleanup()
      
    self.tare = int(sum(avg)/count)

if __name__ == "__main__":
  print("Assuming DT on BCM 17 and SCLK on BCM 27")
  print("Starting Calibration, don't put anything on the scale")
  s = scale()
  s.tare()
  print("Please put something on the scale")
  
  try:
    while(True):
      print("raw value of ADC is")
      print(get_input)
      sleep(2)
  except(KeyboardInterrupt):
    GPIO.cleanup()
  


"""
DT = 17
SCLK = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(DT, GPIO.IN)
GPIO.setup(SCLK, GPIO.OUT)
GPIO.output(SCLK, 0)
time.sleep(1)
try:
  while True:
    val = 0
    while(GPIO.input(DT)):
      pass
    time.sleep(1E-7)
    for i in range(24):
      GPIO.output(SCLK,1)
      val <<= 1
      GPIO.output(SCLK,0)
      val += GPIO.input(DT)
      
    GPIO.output(SCLK,1)
    #val ^= 0x800000
    #val -= 390000
    GPIO.output(SCLK,0)
    print(f"{val}      {bin(val)}")
    
  
finally:
  GPIO.cleanup()
"""
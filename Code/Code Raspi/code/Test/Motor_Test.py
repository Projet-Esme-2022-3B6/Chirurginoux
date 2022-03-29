import RPi.GPIO as GPIO
import time

#13 & 12
servoPIN = 13                    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
position=7
p.start(position) # Initialization
time.sleep(0.2)
try:
  while True:
    p.ChangeDutyCycle(0)
    x=input("enter the angle :\n")
    x=int(x)
    if x<position:
        for i in range (position*10,x*10,-1):
            p.ChangeDutyCycle(i/10)
            time.sleep(0.2)
    
    if x>position:
        for i in range (position*10,x*10,1):
            p.ChangeDutyCycle(i/10)
            time.sleep(0.2)
    position=x
    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

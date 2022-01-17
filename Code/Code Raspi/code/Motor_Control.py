import RPi.GPIO as GPIO
import time


class MotorControl:
    def __init__(self,gpio_motor,initpos=7,pos_min=2,pos_max=12,frequency=50):
        servoPIN = 12
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(gpio_motor, GPIO.OUT)
        
        self.pos_min=pos_min
        self.pos_max=pos_max
        
        self.motorPWM = GPIO.PWM(gpio_motor, frequency)
        self.position=initpos
        self.motorPWM.start(self.position) # Initialization
        time.sleep(0.2)
        self.motorPWM.ChangeDutyCycle(0)

    def goto(self,value):
        #verify and stay between 0° and 180°
        if value>self.pos_max:
            value=self.pos_max
        if value<self.pos_min:
            value=self.pos_min
        
        if value<self.position:
            for i in range (self.position*10,value*10,-1):
                self.motorPWM.ChangeDutyCycle(i/10)
                time.sleep(0.2)
        
        if value>self.position:
            for i in range (self.position*10,value*10,1):
                self.motorPWM.ChangeDutyCycle(i/10)
                time.sleep(0.2)
        self.motorPWM.ChangeDutyCycle(value)
        time.sleep(0.2)
        self.position=value
        self.motorPWM.ChangeDutyCycle(0)
    
    def Quit(self):
        self.motorPWM.stop()
        GPIO.cleanup()
  

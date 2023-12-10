import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class SetUp():
    def __init__(self, pin, frequency, max, min, neutral):
        self.pin = pin
        self.frequency = frequency

        self.__min = min
        self.__max = max
        self.__neutral = neutral

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, frequency)
        self.pwm.start(neutral)

        time.sleep(1.5)

        self.pwm.ChangeDutyCycle(0)
        
        logging.info(f'{self.__class__.__name__} initalized.')

    def start(self):
        logging.info(f'SetUp programm started.')

        self.__throttle()
        time.sleep(2)
        input(f'Press Enter to continue.')
        self.__idle()
        time.sleep(2)
        input(f'Press Enter to continue.')
        self.__brake()
        logging.info(f'SetUp programm finished.')
        return
    
    def __throttle(self):
        self.pwm.ChangeDutyCycle(self.__max)
        return
    
    def __idle(self):
        self.pwm.ChangeDutyCycle(self.__neutral)
        return
    
    def __brake(self):
        self.pwm.ChangeDutyCycle(self.__min)
        return
    
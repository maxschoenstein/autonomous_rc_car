import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.DEBUG)


class DriveControl():
    def __init__(self, pin, frequency, max, min, neutral, step):
        self.pin = pin
        self.frequency = frequency
        self.neutral = neutral
        self.min = min
        self.max = max
        self.step = step
        self.duty_cycle = neutral

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, frequency)

        self.pwm.start(neutral)
        time.sleep(1.5)
        self.pwm.ChangeDutyCycle(0)
        logging.info(f'{self.__class__.__name__} initalized\n \
        Pin: {self.pin}\n \
        PWM-Frequency: {self.frequency}\n\
        PWM-Max: {self.max}\n \
        PWM-Min: {self.min}\n \
        PWM-Neutral: {self.neutral}\n \
        PWM-Step: {self.step}\n'
        )
        
    def increase_duty_cycle(self):
        if self.duty_cycle >= self.max:
            pass
        else:
            self.duty_cycle += self.step
            self.pwm.ChangeDutyCycle(self.duty_cycle) 

        logging.info('increase')
        logging.info(self.duty_cycle)
        return

    def decrease_duty_cycle(self):
        #if self.duty_cycle == self.neutral:
        #    self._engage_reverse()
        if self.duty_cycle <= self.min:
            pass
        else:
            self.duty_cycle -= self.step
            self.pwm.ChangeDutyCycle(self.duty_cycle) 
        logging.info('decrease')
        logging.info(self.duty_cycle)
        return
    
    def _engage_reverse(self):
        self.pwm.ChangeDutyCycle(self.min)
        time.sleep(2.5)
        self.pwm.ChangeDutyCycle(self.neutral)
        return

    def exit(self):
        logging.info('exit')

        self.pwm.ChangeDutyCycle(self.neutral) 
        time.sleep(1.5)
        self.pwm.stop()
        GPIO.cleanup()
        return
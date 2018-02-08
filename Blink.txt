# Blink.py

import time
import RPi.GPIO as GPIO

led_red = 4
led_green = 17

try:
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(led_red, GPIO.OUT)
        GPIO.setup(led_green, GPIO.OUT)
        
        while True:
                    GPIO.output(led_red, True)
                    time.sleep(0.25)
                    GPIO.output(led_red, False)
                    time.sleep(0.25)

                    GPIO.output(led_green, True)
                    time.sleep(0.25)
                    GPIO.output(led_green, False)
                    time.sleep(0.25)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
 

# 1_Blinking_LED.py

import time
import RPi.GPIO as GPIO

led = 24

try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
                     
        while True:
                    GPIO.output(led, True)
                    time.sleep(0.25)
                    GPIO.output(led, False)
                    time.sleep(0.25)
                    
        print("Running Blink.py")
        os.system('python /home/pi/Desktop/FYP/Programming/Blink/2_Blinking_LEDs.py')
                   
except KeyboardInterrupt:
    pass

GPIO.cleanup()
 


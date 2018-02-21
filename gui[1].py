from tkinter import *
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led = LED(12)

## GUI
win = Tk()
win.title("LED GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')
## win.geometry('800x480')

## Functions
def ledToggle():
        if led.is_lit:
            led.off()
            ledButton["text"] = "Turn LED On"        
        else:
            led.on()
            ledButton["text"] = "Turn LED Off"
            
def close():
    RPi.GPIO.cleanup()
    win.destroy()
            
## Widgets
ledButton = Button(win, text = "LED ON", font = myFont, command = ledToggle, bg = 'bisque2', height = 2, width = 12)
ledButton.grid(row=0,column=1)

exitButton = Button(win, text = "EXIT", font = myFont, command = close, bg = 'red', height = 2, width = 6)
exitButton.grid(row=1,column=1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # loop forever 

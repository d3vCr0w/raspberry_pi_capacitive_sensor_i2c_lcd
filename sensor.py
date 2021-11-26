import LCD
from time import sleep
from datetime import datetime
from gpiozero import Button

sensor = Button(4, pull_up=False)
count = 0
display = LCD.lcd()

try:
    while True:
        if sensor.is_pressed:
            count = count + 1
            print "Object detected, Count: "+str(count)
            display.lcd_display_string("Count: "+str(count), 1)
	    display.lcd_display_string("Object detected        ", 2)
        else:
	    display.lcd_display_string("Count: "+str(count), 1)
	    display.lcd_display_string("No reading             ", 2)
            print "No reading from sensor, Count: "+str(count)
        sleep(0.2)


except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()

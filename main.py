from services import motion
from services import sound

import RPi.GPIO as GPIO
import time

################################3
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

start_button=2      #game start button
GPIO.setup(start_button, GPIO.IN)

start_lamp=3        #game start lamp
GPIO.setup(start_lamp, GPIO.OUT)

left_button=21      #left chosen button
GPIO.setup(left_button, GPIO.IN)

right_button=20     #right chosen button
GPIO.setup(right_button, GPIO.IN)

#################################
StartOn=False           #start lamp on
StartInputPrev=False    #prev start state

TurnOff=False           #turn off game


################################
try:
    while True:
        StartInput=GPIO.input(start_button)     #start button variable
        if StartInput and not StartInputPrev:   #if start button pushed
            if StartOn==False:                  #if lamp is off, change on
                StartOn=True
                GPIO.output(start_lamp, StartOn)

                ####그 외 모든 함수

            else:                               #else lame goes off
                StartOn=False
                GPIO.output(start_lamp, StartOn)#game off
                # break

        elif not StartInput and StartInputPrev: #constant state for push button 0.5 sec
            time.sleep(0.5)
        else: pass
        StartInputPrev=StartInput               #check prev start button state

################################
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
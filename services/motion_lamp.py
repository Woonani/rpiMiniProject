import RPi.GPIO as GPIO
import time

################################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

################################


def input_button(left_button, right_button):     #input left/right button

    left=GPIO.input(left_button)
    right=GPIO.input(right_button)
    if(left):
        return 'user_left'
    elif(right):
        return 'user_right'


def input_lamp(lamp, left_lamp, right_lamp):       #turn on Lamp
    if lamp=='user_left' or lamp=='comp_left':
        GPIO.output(left_lamp, True)
    
    elif lamp=='user_right' or lamp=='comp_right':
        GPIO.output(right_lamp, True)

    else:
        GPIO.output(left_lamp, False)
        GPIO.output(right_lamp, False)

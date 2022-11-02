import RPi.GPIO as GPIO
import time

start_button=4      #game start button
start_lamp=17        #game start lamp
#############################################

# global StartOn
# StartOn=False           #start lamp on

# global StartInputPrev
# StartInputPrev=False    #prev start state

# global StartInput
# StartInput=False #current start state

#############################################
def server_on(start_button, start_lamp, StartOn):
    StartInputPrev=False
    StartInput=False
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(start_button, GPIO.IN)
    GPIO.setup(start_lamp, GPIO.OUT)

    try:                    #start main
        while True:
            StartInput=GPIO.input(start_button)     #start button variable
            if StartInput and not StartInputPrev:   #if start button pushed
                print("on")
                # GPIO.output(start_lamp, StartOn)
                # StartInputPrev=StartInput
                break                           #game turns on
            elif not StartInput and StartInputPrev: #constant state for push button 0.5 sec
                time.sleep(0.5)
            else: pass
            StartInputPrev=StartInput               #check prev start button state
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()

# def server_off(start_button, start_lamp, main_control, StartOn, StartInputPrev, StartInput):
#     # global StartOn
#     # global StartInputPrev
#     # global StartInput
    
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(start_button, GPIO.IN)
#     GPIO.setup(start_lamp, GPIO.OUT)

#     try:                    #finish main
#         while True:
#             StartInput=GPIO.input(start_button)     #start button variable
#             if (StartInput and not StartInputPrev):   #if start button pushed
#                 if StartOn==True:                  
#                     StartOn=False                   #change main lamp off
#                     GPIO.output(start_lamp, StartOn)
#                     break                           #end main

#             elif not StartInput and StartInputPrev: #constant state for push button 0.5 sec
#                 time.sleep(0.5)

#             else: pass
#             StartInputPrev=StartInput               #check prev start button state
#             if not main_control:
#                 StartOn=False
#                 GPIO.output(start_lamp, StartOn)
#                 break

#     except KeyboardInterrupt:
#         pass
#     GPIO.cleanup()

#################################
#test

server_on(start_button, start_lamp, True)
# server_off(start_button, start_lamp , True)
GPIO.cleanup()
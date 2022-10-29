from services import motion
from services import sound
from services import motion_lamp
from services import sound_buzzer

import RPi.GPIO as GPIO
import time
import threading
import random

##################################

# motion.motion_test()
# sound.sound_test()
print("server on")
################################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

start_button=4      #game start button
GPIO.setup(start_button, GPIO.IN)

start_lamp=17        #game start lamp
GPIO.setup(start_lamp, GPIO.OUT)

#USER_LEFT
left_button=21      #left chosen button
GPIO.setup(left_button, GPIO.IN)
left_lamp=26        #left lamp
GPIO.setup(left_lamp, GPIO.OUT)

#USER_RIGHT
right_button=20     #right chosen button
GPIO.setup(right_button, GPIO.IN)
right_lamp=19       #right red lamp
GPIO.setup(right_lamp, GPIO.OUT)

#COMPUTER_LEFT
comp_left=24
GPIO.setup(comp_left, GPIO.OUT)

#COMPUTER_RIGHT
comp_right=23
GPIO.setup(comp_right, GPIO.OUT)

#PRINT_ANSWER_SOUND
buzzer_pin=18
GPIO.setup(buzzer_pin, GPIO.OUT)

#################################
StartOn=False           #start lamp on
StartInputPrev=False    #prev start state
StartInput=False #current start state

force_control=False     #thread off
global main_control       #main off
main_control=True

################################
def game_main():        #game-main
    global main_control

    print("GAME START") #game start
    for i in range(0,3):
        print("cham")
        time.sleep(0.5)

    computer = ["comp_left", "comp_right"]    #computer chooses answer
    computer_answer=computer[random.randint(0,1)]
   
    while True:
        temp=motion_lamp.input_button(left_button, right_button)    #input left or right

        if temp=='user_right' or temp=='user_left':
            print(temp)
            motion_lamp.input_lamp(temp, left_lamp, right_lamp)     #output left or right

            time.sleep(1)                                           #output computer answer
            print("Computer Answer is")
            print(computer_answer)
            motion_lamp.input_lamp(computer_answer, comp_left, comp_right)
            
            if(temp=='user_left' and computer_answer=='comp_left') or (temp=='user_right' and computer_answer=='comp_right'):
                                                                    #output sound answer
                print("YOU WON")
                print("YOU WON")
                print("YOU WON")
                sound_buzzer.print_answer(buzzer_pin)
            
            else:                                                   #output sound wrong
                print("YOU LOST")
                print("YOU LOST")
                print("YOU LOST")
                sound_buzzer.print_wrong(buzzer_pin)

            time.sleep(1)
            main_control=False
            break

        if force_control:       #force off
            break

game=threading.Thread(target=game_main)
#################################
try:                    #start main
    while True:
        StartInput=GPIO.input(start_button)     #start button variable
        if StartInput and not StartInputPrev:   #if start button pushed
            StartOn=True                        #change main lamp on
            GPIO.output(start_lamp, StartOn)
            StartInputPrev=StartInput
            break                           #game turns on
        elif not StartInput and StartInputPrev: #constant state for push button 0.5 sec
            time.sleep(0.5)
        else: pass
        StartInputPrev=StartInput               #check prev start button state
except KeyboardInterrupt:
    GPIO.cleanup()
#####################################

game.start()              #thread1-main starts

####################################
try:                    #finish main
    while True:
        StartInput=GPIO.input(start_button)     #start button variable
        if (StartInput and not StartInputPrev):   #if start button pushed
            if StartOn==True:                  
                StartOn=False                   #change main lamp off
                GPIO.output(start_lamp, StartOn)
                break                           #end main

        elif not StartInput and StartInputPrev: #constant state for push button 0.5 sec
            time.sleep(0.5)

        else: pass
        StartInputPrev=StartInput               #check prev start button state
        if not main_control:
            StartOn=False
            GPIO.output(start_lamp, StartOn)
            break

except KeyboardInterrupt:
    GPIO.cleanup()

force_control=True              #off game forcely
game.join()                     #wait til thread ends



#######################
#rest lamp and GPIO variable

GPIO.output(left_lamp, False)
GPIO.output(right_lamp, False)
GPIO.output(comp_left, False)
GPIO.output(comp_right, False)

print("goodbye")
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

#################################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##################################

def print_answer(buzzer_pin):     #use as answer sound for temporary
    # GPIO.setup(buzzer_pin, GPIO.OUT)

    pwm=GPIO.PWM(buzzer_pin, 1.0)
    pwm.start(50.0)

    melody = [262, 262, 330, 392, 523]

    for note in range(0, 5):
        pwm.ChangeFrequency(melody[note])
        if note==0:
            time.sleep(0.25)
        else:
            time.sleep(0.5)

    pwm.ChangeDutyCycle(0.0)

    pwm.stop()

def print_wrong(buzzer_pin):     #use as answer sound for temporary
    # GPIO.setup(buzzer_pin, GPIO.OUT)

    pwm=GPIO.PWM(buzzer_pin, 1.0)
    pwm.start(50.0)

    # melody = [523, 523, 440, 349, 294]
    melody = [440, 440, 392, 440, 392, 330, 294, 330, 294]

    for note in range(0, 9):
        pwm.ChangeFrequency(melody[note])
        if note==4 or note==8:
            time.sleep(1)
        elif note==2 or note==6:
            time.sleep(0.25)
        else:
            time.sleep(0.5)
        # if note==1:
        #     time.sleep(0.25)
        # else:
        #     time.sleep(0.5)

    pwm.ChangeDutyCycle(0.0)

    pwm.stop()

# GPIO.cleanup()
#print('haha')
#while True:
#    print('WTL')

###################################################################

# import RPi.GPIO as GPIO
# 
# button_pin =27
# 
# 
# 
# GPIO.setmode(GPIO.BCM)
# 
# GPIO.setup(button_pin, GPIO.IN)
# 
# try:
#     while True:
#         buttonInput = GPIO.input(button_pin)
#         print(buttonInput)
#         
# except KeyboardInterrupt:
#     pass
# 
# GPIO.cleanup()

####################################################################

# import RPi.GPIO as GPIO
# 
# button_pin =27
# led_pin =22
# 
# 
# GPIO.setmode(GPIO.BCM)
# 
# GPIO.setup(button_pin, GPIO.IN)
# GPIO.setup(led_pin, GPIO.OUT)
# 
# #GPIO.output(led_pin, True)
# 
# try:
#     while True:
#         buttonInput = GPIO.input(button_pin)
#         GPIO.output(led_pin, buttonInput)
#         
# except KeyboardInterrupt:
#     pass
# 
# GPIO.cleanup()
####################################################################
# 
import RPi.GPIO as GPIO

print("good")

button_pin =27
led_pin =22


GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

buttonInputPrev = False
ledOn = False
# 파이썬 재밌냐?
try:
    while True:
        buttonInput = GPIO.input(button_pin)
        
        if buttonInput and not buttonInputPrev:
            print("check",buttonInput)
            print("rising edge")
            ledOn = True if not ledOn else False
            GPIO.output(led_pin, ledOn)
#             GPIO.output(led_pin, buttonInput)
        elif not buttonInput and buttonInputPrev:
            print("check2",buttonInput)
            print("falling edge")
        else: pass
        
        buttonInputPrev = buttonInput
        
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
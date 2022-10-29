# import threading
# import time

# flag_exit=False
# def t1_main():
#     while True:
#         print("thread ")
#         time.sleep(0.5)
#         if flag_exit:
#             break

# t1=threading.Thread(target=t1_main)
# t1.start()

# try:
#     while True:
#         print("main")
#         time.sleep(1.0)

# except KeyboardInterrupt:
#     pass

# flag_exit=True
# t1.join()


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test=24
GPIO.setup(test, GPIO.OUT)

try:
    while True:
        GPIO.output(test,True)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
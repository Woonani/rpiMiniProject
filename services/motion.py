import picamera
import time

camera = picamera.PiCamera()

camera.start_preview()

time.sleep(1)
camera.resolution = (2592, 1944)
camera.capture('/home/camel/Desktop/coding/rpiMiniProject/test.jpg')

camera.stop_preview()


# import picamera
# import time

# camera = picamera.PiCamera()
# camera.resolution = (2592, 1944) # (64, 64) ~ (2592, 1944) px

# time.sleep(3)
# camera.capture('home/camel/Desktop/coding/rpiMiniProject/test.jpg')


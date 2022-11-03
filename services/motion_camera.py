import picamera
import time

# input_address=[[0]*50 for i in range(4)]
# for i in range(0, 4):
#     input_address[i]='/home/camel/Desktop/rpiMiniProject/data/origin'+str(i)+'.jpg'

#사진 4회 촬영
def picture(inadd):
    camera = picamera.PiCamera()    #picamera 사용

    camera.start_preview()          #open camera

    camera.resolution = (600, 400)  #resolve pic size
    for add in range(0, 4):         #take pic 4times pairing with cham
        camera.capture(inadd[add])

    camera.stop_preview()


# picture(input_address)
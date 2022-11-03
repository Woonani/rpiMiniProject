import cv2
import motion_camera

input_address=[[0]*50 for i in range(4)]
output_address=[[0]*50 for i in range(4)]
for i in range(0, 4):
    input_address[i]='/home/camel/Desktop/rpiMiniProject/data/origin'+str(i)+'.jpg'
    output_address[i]='/home/camel/Desktop/rpiMiniProject/data/edit'+str(i)+'.jpg'

motion_camera.picture(input_address)
#take pic
#############################

def editpic(inadd, outadd):
    for add in range(0, 4):
        img = cv2.imread(inadd[add])        #read pic using cv

        img_canny = cv2.Canny(img, 50, 150) #edit pic using cv
        cv2.imwrite(outadd[add], img_canny) #store edited pic

    cv2.waitKey(0)
    cv2.destroyAllWindows()

editpic(input_address, output_address)

# import cv2

# img1 = cv2.imread('/home/camel/Desktop/rpiMiniProject/test.jpg')

# print(type(img1))

# cv2.imshow('image1', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

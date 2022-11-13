import numpy as np
import cv2 as cv
import dlib

def determine():
    # set dlib data input&output
    add=['data/pic0.jpg', 'data/pic1.jpg', 'data/pic2.jpg', 'data/pic3.jpg']    #save 4 pics
    detector = dlib.get_frontal_face_detector()                                 #dlib trained module
    predictor = dlib.shape_predictor('services/eye_predictor.dat')
    
    # set camera
    cap = cv.VideoCapture(-1)
    ret, img_frame = cap.read()

    # take origin pic as pic0
    cv.imwrite(add[0], img_frame)

    # set range for face landmarks
    index=list(range(0,13))

    # set variable for determination
    total = []
    leftright=0
    breakpoint=0

    textPrefix='not defined'

    print("camera starts")

    # take shot while determine either left or right
    while True:
        #set breakpoint
        if breakpoint==1:
            break

        #set camera
        ret, img_frame = cap.read()

        #set face detector
        dets = detector(img_frame, 1)
        
        #loop amount of face detected
        for face in dets:

            #find landmarks from face and set
            shape = predictor(img_frame, face)
            list_points = []
            for p in shape.parts():
                list_points.append([p.x, p.y])
            list_points = np.array(list_points)

            #set center of gravity point for eye landmarks
            middle_x=0;
            for i, pt in enumerate(list_points[index]):
                pt_pos = (pt[0], pt[1])
                if i>0:         #not point between eyebrows
                    middle_x=middle_x+list_points[i][0]/12
            middle=list_points[0][0]-int(middle_x)
            # print(middle)

            #count number of left&right
            if middle>5 or middle<-5:
                leftright=leftright+1
                total.append(middle)

            #if counted left&right more then 3times,
            if leftright>4:
                print(total)

                #take last picture as pic1
                cv.imwrite(add[1], img_frame)

                #color eye, and take pic2
                for i, pt in enumerate(list_points[index]):
                    pt_pos = (pt[0], pt[1])
                    if i>0:
                        cv.circle(img_frame, pt_pos, 2, (0, 255, 255), -1)
                cv.imwrite(add[2], img_frame)

                #draw square and text, take pic3
                cv.rectangle(img_frame, (face.left(), face.top()), (face.right(),face.bottom()), (0, 0, 0), 3)
                if sum(total) < 0:
                    textPrefix = 'uesr_right'
                else:
                    textPrefix = 'user_left'
                
                print(textPrefix)
                cv.putText(img_frame, textPrefix, (face.left(), face.top()), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
                cv.imwrite(add[3], img_frame)

                #break loop
                breakpoint=1
                cap.release()
                cv.destroyAllWindows()
                break

        #break at esc
        # cv.imshow('result', img_frame)
        key = cv.waitKey(10)
        if key==27:
            break

    cap.release()
    cv.destroyAllWindows()
    return textPrefix

determine()
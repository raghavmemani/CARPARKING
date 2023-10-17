import cv2
import pickle
import cvzone

import  numpy as np

#videofeed

cap=cv2.VideoCapture('carParkingInput.mp4')
width, height = 107, 48

def checkparkingspace(imgproceed):
    spacecouter=0;
    for pos in poslist:
        x,y=pos

        imgcrop=imgproceed[y:y+height,x:x+width]
        ##cv2.imshow(str(x*y),imgcrop)
        count = cv2.countNonZero(imgcrop)
        cvzone.putTextRect(image,str(count),(x,y+height-3),scale=1,thickness=2,offset=0,colorR=(0,0,255))


        if count>5000:
             color=(0,255,0)
             thickness=5
             spacecouter+=1
        else:
            color=(0,0,255)
            thickness=2
        cv2.rectangle(image, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(image, f'Free:{spacecouter}/{len(poslist)}',(100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 255))











with open('carparkpos', 'rb') as f:
    poslist = pickle.load(f)

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):

        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    succuess, image = cap.read()

    imggray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imageblur=cv2.GaussianBlur(imggray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imageblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16)
    imahemedian=cv2.medianBlur(imgThreshold,5)
    kernel=np.ones((3,3),np.uint8)
    imagedialte=cv2.dilate(imahemedian,kernel,iterations=1)





    checkparkingspace(imagedialte)



    cv2.imshow("image1", image)
    ##cv2.imshow("image",imagedialte)


    cv2.waitKey(10)

import cv2
import pickle

try:
    with open('carparkpos', 'rb') as f:
        poslist=pickle.load(f)
except:
    poslist=[]





width, height = 107, 48



def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate( poslist):
            x1,y1=pos;
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)
    with open('carparkpos','wb') as f:
        pickle.dump(poslist,f)



while True:
    image = cv2.imread('carParkImg.png')
    ##cv2.rectangle(image,(50,190),(157,240),(255,0,255),2)

    for pos in poslist:
        cv2.rectangle(image, pos, (pos[0]+width,pos[1]+height), (255, 0, 255), 2)

    cv2.imshow("image", image)
    cv2.setMouseCallback("image", mouseclick)
    cv2.waitKey(1)


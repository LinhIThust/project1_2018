import cv2
import numpy as np

#image
img = cv2.imread('hello.png',1)
#or
# img = cv2.imread('hello.png',0)
# img = cv2.imread('hello.png',-1)
cv2.imshow('NameFrame',img)
cv2.imwrite('save.jpg',img)


#draw
#create a backgroud
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px, full is -1
cv2.line(img, (200,200), (511, 511), (255, 8, 0),5)

# Draw a Rectangle
cv2.rectangle(img, (0,0), (51, 11), (255, 8, 34),-1)

# Draw a Cicrle
cv2.circle(img,(200,200),105,(135,362,747),-1)

# Draw a Ellipse
cv2.ellipse(img,(200,200),(100,50),0,0,360,(255,135,532))

# draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[90,10],[50,130],[50,107]], np.int32)

#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],False,(0,255,255))
cv2.polylines(img,[pts],True,(0,255,255))
# true -> kin,false -> k kin

#input text
font = cv2.FONT_ITALIC
cv2.putText(img,"linhDzai",(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('draw',img)


#webcam
cap = cv2.VideoCapture(0)
#import a video
#cap = cv2.VideoCapture('link')

while(1):
    # Take each frame
    res,frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
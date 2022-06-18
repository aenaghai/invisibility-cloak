from cv2 import waitKey
import numpy as np
import time
import cv2

cap=cv2.VideoCapture(0) #capturing from device webcam
#so that the video can be captured in the first 2 seconds after running the program
time.sleep(2)
bg=0

bg = cv2.flip(bg,1)

#to capture the image in first 2 seconds
for i in range(50):
    ret,bg=cap.read()

#capturing the video
while(cap.isOpened()):
    ret,image=cap.read()
    if not ret:
        break
    #converting to hsv format
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #Now we have to take the values of the red color cloth to take any values and change till then the red color will start to disappear from the frame
    #setting the cloak values and creating masks :)
    lowerRedValue=np.array([0,120,70])
    upperRedValue=np.array([10,255,255])
    maskOne=cv2.inRange(hsv,lowerRedValue,upperRedValue)
    
    lowerRedValue=np.array([170,120,70])
    upperRedValue=np.array([180,255,255])
    maskTwo=cv2.inRange(hsv,lowerRedValue,upperRedValue)
    
    #combining the masks to make them appear in same frame to generate the final one
    maskOne=maskOne+maskTwo
    
    '''cv2.MORPH_CLOSE removes unnecessary black noise from the white region in the mask. And how much noise to remove that is defined by kernel size.
    cv2.MORPH_OPEN removes unnecessary white noise from the black region.
    cv2.dilate increases white region in the image.'''
    maskOne = cv2.morphologyEx(maskOne,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    maskOne = cv2.morphologyEx(maskOne, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    maskTwo =cv2.bitwise_not(maskOne) 
    #cv2.bitwise_not() inverse the mask pixel value. Where the mask is white it returns black and where is black it returns white   
    res = cv2.bitwise_and(bg,bg,mask=maskOne)
    #bitwise_and() combines these backgrounds and store it in res: applies mask on frame in the region where mask is true
    resfinal = cv2.bitwise_and(image,image,mask=maskTwo)
    final = cv2.addWeighted(res,1,resfinal,1,0) #blending the two images :)
    cv2.imshow('The Invisibility Cloak',final)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


'''
Algorithm:

firstly Import the Libraries that we can use to make the project.
using a webcam to capture the live feed of the person and the background.
Capturing the background firstly we have to capture the background so that if the cloth comes in it shows the background.
Setting the values for the Cloak that the cloth we selected we have to now set the values for it.
making 2 masks and applying them to the frame.
combining the mask and showing it simultaneously
Displaying the final output
'''
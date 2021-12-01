'''
    Author: Python_Elidas
    Email: pyro.elidas@gmail.com
    Python version: 3.9.1
    Date: 2021-11-12T08:54:09.237Z
    Version: 0.0.0
'''

# __LYBRARIES__ #
import numpy as np
import cv2

# __MAIN CODE__ #
camera = cv2.VideoCapture(1) #? 0 = integrated camera // 1 = USB camera

while(True):
      
    # Capture the video frame by frame
    ret, frame = camera.read()
    
    # reescalemos la imágen:
    if ret == True:
        res = cv2.resize(frame,
                         (1280,720), 
                         fx=0, fy=0,
                         interpolation=cv2.INTER_CUBIC
                        )
    else:
        break

    # eliminemos el ruidos
    dst = cv2.GaussianBlur(res,(5,5),cv2.BORDER_ISOLATED)
    
    # Display the resulting frame
    cv2.imshow('Camera Capture', dst)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
 
# __BIBLIOGRAPHY__ #
'''
Geeks for Geeks: https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
'''
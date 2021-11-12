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
from Auxiliars import set_res


# __MAIN CODE__ #
# Establecemos la configuracion de base:
file_name = 'test.avi'
fps = 24.0
my_res = '420p'

# creamos la variable de captura
cap = cv2.VideoCapture(0)
set_res(cap, my_res)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# when everithing done, release the capture
cap.release()
cv2.destroyAllWindow()


# __NOTES__ #
'''
    >
'''

# __BIBLIOGRAPHY__ #
'''
    > YouTube: https://www.youtube.com/watch?v=1eHQIu4r0Bc
'''

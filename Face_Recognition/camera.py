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
import pickle
from Auxiliars import set_res
import random


# __MAIN CODE__ #
fps = 60.0,
my_res = '1080p'

# Creemos el modelo de reconocimiento de objetos:
face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trained.yml')

# creamos las etiquetas de nombre:
with open('label.pickle', 'rb') as f:
    labels = {v: k for k, v in pickle.load(f).items()}

# creamos la variable de captura
cap = cv2.VideoCapture(0)
set_res(cap, my_res)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # creemos la estructura para capturar las caras
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5
    )

    # operamos sobre los objetosd detectados:
    for x, y, h, w in faces:
        # print(faces)
        # establecemos la region que nos interesa
        roi = gray[y:y+h, x:x+w]  # Region Of Interest

        id_, conf = recognizer.predict(roi)
        print(labels[id_], conf)
        if conf >= 35:
            # print(labels[id_], conf)
            cv2.putText(
                frame,
                labels[id_],
                (x+15, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 120),
                2,
                cv2.LINE_AA
            )

        '''color = (200, 100, 0)  # BGR
        stroke = 2  # Grosor de la linea
        cv2.rectangle(  # Dibujamos el cuadrado
            frame,
            (x, y),  # Coordenadas en las que empieza el cuadrado
            (x+w, y+h),  # Coordenadas en las que Termina el cuadrado
            color,
            stroke
        )'''

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# when everithing done, release the capture
cap.release()
cv2.destroyAllWindow()


if __name__ == '__main__':
    recording()


# __NOTES__ #
'''
    >
'''

# __BIBLIOGRAPHY__ #
'''
    > YouTube: https://www.youtube.com/watch?v=1eHQIu4r0Bc
'''

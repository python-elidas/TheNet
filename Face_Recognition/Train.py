'''
    Author: Python_Elidas
    Email: pyro.elidas@gmail.com
    Python version: 3.9.1
    Date: 2021-11-12T08:54:09.237Z
    Version: 0.0.0
'''

# __LYBRARIES__ #
import os
from PIL import Image
import numpy as np
import cv2
import pickle


# __MAIN CODE__ #
# buscamos lñas imagenes de entrenamiento:
main_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(main_dir, 'Images')

# creamos el modelo de reconocimiento de caras
face_cascade = face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# creamos el modelo de train:
current_id = 0
label_ids = dict()
x_train = list()
y_train = list()

# recorremos el directorio:
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):

            # Obtenemos la ruta a cada imagen
            path = os.path.join(root, file)
            # obtenemos el nombre de la imagen
            name = os.path.basename(root)

            # creemos el diccionario de nombres:
            if name not in label_ids:
                label_ids[name] = current_id
                current_id += 1

            id_ = label_ids[name]

            # convertimos la imgen a escala de grises:
            pil_image = Image.open(path).convert('L')
            # Convertimos la imagen a un array
            img_array = np.array(pil_image, 'uint8')

            # Buscamos las caras en las imagenes:
            faces = face_cascade.detectMultiScale(
                img_array,
                scaleFactor=2,
                minNeighbors=6
            )

            # establecemos la roi
            for x, y, w, h in faces:
                roi = img_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_train.append(id_)

# Creamos un archivo que guarde toda esta infromacion
with open('label.pickle', 'wb') as f:
    pickle.dump(label_ids, f)

# entrenamos el modelo
recognizer.train(x_train, np.array(y_train))
recognizer.save('Trained.yml')


# __NOTES__ #
'''
    >
'''

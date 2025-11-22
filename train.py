import cv2
import numpy as np
import os

def get_images_and_labels(path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    
    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        faces = face_cascade.detectMultiScale(img)
        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            id = int(os.path.split(image_path)[-1].split('.')[1])
            ids.append(id)
    return face_samples, ids

faces, ids = get_images_and_labels('dataset')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')
print(f"Training complete. {len(np.unique(ids))} users trained.")

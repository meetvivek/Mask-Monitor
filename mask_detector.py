import cv2
import numpy as np
from tensorflow.keras.models import load_model
import threading
import pyttsx3
from excel_handler import ExcelHandler
from image_saver import ImageSaver

# Initialize text-to-speech engine
engine = pyttsx3.init()

class FaceMaskDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.model = load_model("mask_model.h5")
        self.image_saver = ImageSaver()
        self.excel_handler = ExcelHandler()

    def predict_mask(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        current_status = None

        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            resized_face = cv2.resize(face_roi, (224, 224))
            normalized_face = resized_face / 255.0
            reshaped_face = np.reshape(normalized_face, (1, 224, 224, 1))
            result = self.model.predict(reshaped_face)

            if result < 0.5:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'With Mask', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                current_status = 'With Mask'
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, 'Without Mask', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                current_status = 'Without Mask'

                # Voice alert for no mask
                threading.Thread(target=self.voice_alert).start()

        return frame, current_status

    def voice_alert(self):
        print("Without Mask")
        engine.say("Mask Alert: Your safety matters. Please wear a mask. Thank you!")
        engine.runAndWait()

    def record_data_and_save_image(self, current_status, frame):
        self.excel_handler.record_to_excel(current_status)
        image_path = self.image_saver.save_image(frame, current_status)
        print(f"Recorded: {current_status} - Image saved at: {image_path}")


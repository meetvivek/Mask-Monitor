import cv2
import os
import time


class ImageSaver:
    def __init__(self, base_folder='MaskMonitor Data'):
        self.base_folder = base_folder
        self.create_base_folder()

    def create_base_folder(self):
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def save_image(self, frame, status):
        current_date = time.strftime('%d-%m-%Y')
        current_time = time.strftime('%H-%M-%S')
        date_folder = os.path.join(self.base_folder, current_date)

        if not os.path.exists(date_folder):
            os.makedirs(date_folder)

        file_name = f"{current_time}_{status}.png"
        file_path = os.path.join(date_folder, file_name)

        cv2.imwrite(file_path, frame)
        return file_path

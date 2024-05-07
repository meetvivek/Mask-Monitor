import cv2
import time
from mask_detector import FaceMaskDetector

if __name__ == "__main__":
    detector = FaceMaskDetector()

    cap = cv2.VideoCapture(0)
    delay = 5  # seconds
    min_consecutive_frames = 5
    start_time = time.time()
    consecutive_frames = 0
    last_status = None

    while True:
        ret, frame = cap.read()

        frame_with_mask, current_status = detector.predict_mask(frame)

        if current_status is not None and current_status == last_status:
            consecutive_frames += 1
        else:
            consecutive_frames = 0

        if consecutive_frames >= min_consecutive_frames and time.time() - start_time >= delay:
            detector.record_data_and_save_image(current_status, frame)
            start_time = time.time()

        last_status = current_status

        cv2.imshow('Face Mask Detection', frame_with_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

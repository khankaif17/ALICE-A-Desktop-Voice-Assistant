import cv2
import mediapipe as mp

class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.5)
        self.cap = cv2.VideoCapture(0)

    def detect(self):
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = self.face_detection.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.detections:
                for detection in results.detections:
                    self.mp_drawing.draw_detection(image, detection)

                    if detection.score[0] > 0.9:
                        print("Smile detected!")
                        cv2.imwrite("smiling_face.png", image)
                        self.cap.release()
                        cv2.destroyAllWindows()
                        return

            cv2.imshow('Face Detection', image)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np


class HandGestureVolumeControl:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.volbar = 400
        self.volper = 0
        self.volMin, self.volMax = self.volume.GetVolumeRange()[:2]

    def run(self):
        while True:
            success, img = self.cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            lmList = []
            if results.multi_hand_landmarks:
                for handlandmark in results.multi_hand_landmarks:
                    for id, lm in enumerate(handlandmark.landmark):
                        h, w, _ = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    self.mpDraw.draw_landmarks(img, handlandmark, self.mpHands.HAND_CONNECTIONS)

            if lmList != []:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                length = hypot(x2 - x1, y2 - y1)
                vol = np.interp(length, [30, 350], [self.volMin, self.volMax])
                self.volbar = np.interp(length, [30, 350], [400, 150])
                self.volper = np.interp(length, [30, 350], [0, 100])
                self.volume.SetMasterVolumeLevel(vol, None)

                cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)
                cv2.rectangle(img, (50, int(self.volbar)), (85, 400), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, f"{int(self.volper)}%", (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)

            cv2.imshow('Image', img)
            if cv2.waitKey(1) & 0xff == ord(' '):
                break

        self.cap.release()
        cv2.destroyAllWindows()
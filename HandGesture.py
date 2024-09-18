import cv2
import mediapipe as mp
import time
import numpy as np

class HandGesture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mphand = mp.solutions.hands
        self.hands = self.mphand.Hands()
        self.ptime = 0
        self.ctime = 0

    def draw(self):
        all_coordinates = []
        coordinates = []
        while True:
            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = self.hands.process(imgRGB)
            h, w, _ = img.shape

            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    lm_index_finger = handLms.landmark[8]  
                    lm_middle_finger = handLms.landmark[12]  
                    distance = ((lm_middle_finger.x*w - lm_index_finger.x*w)**2 + (lm_middle_finger.y*h - lm_index_finger.y*h)**2)**0.5
                    
                    if distance > 25:
                        cx, cy = int(lm_index_finger.x * w), int(lm_index_finger.y * h)
                        if coordinates: 
                            cv2.line(img, coordinates[-1], (cx, cy), (0, 255, 0), 3)
                        coordinates.append((cx, cy))
                        cv2.putText(img, "Drawing", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
                    else:
                        if coordinates:
                            all_coordinates.append(coordinates)
                            coordinates = []
                        cv2.putText(img, "Paused", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

                    for line in all_coordinates:
                        for i in range(1, len(line)):
                            cv2.line(img, line[i-1], line[i], (0, 255, 0), 3)
      
                    for i in range(1, len(coordinates)):
                        cv2.line(img, coordinates[i-1], coordinates[i], (0, 255, 0), 3)        

            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

        flattened_coordinates = [(x / w, y / h) for sublist in all_coordinates for (x, y) in sublist]

        return flattened_coordinates

if __name__ == "__main__":
    pass
   
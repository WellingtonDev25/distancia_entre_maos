import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import math

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8,maxHands=2)

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)

    if len(hands)==2:
        #hand 1
        h1= hands[0]
        h2 = hands[1]
        lmList1 = h1["lmList"]
        lmList2 = h2["lmList"]

        h1x = lmList1[9][0]
        h1y = lmList1[9][1]
        h2x = lmList2[9][0]
        h2y = lmList1[9][1]

        cv2.line(img, (h1x, h1y), (h2x, h2y), (255, 0, 0), 3)
        distPx = math.hypot(h1x-h2x,h1y-h2y)
        #370px = 30cm = cada px equivale a 0,0810 cm
        cm = int(distPx * 0.0810)
        ctX, ctY = (h1x + h2x) // 2, (h1y + h2y) // 2
        textCm = f'{cm} cm'
        cv2.putText(img,textCm,(ctX,ctY-20),cv2.FONT_HERSHEY_PLAIN,3,(0, 0, 255),3)

    cv2.imshow("Camera",img)
    cv2.waitKey(1)




import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("test.mp4")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    # img = cv2.imread("test1.jpg")
    img = cv2.resize(img, (600, 800))
    img = detector.findPos(img, False)
    lmList = detector.findpoints(img, False)

    if len(lmList)  != 0:
        
        #Finding angle
        angle = detector.findAngle(img, 11, 13, 15)
        # cv2.putText(img, str(int(angle)), (100, 200), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (0,0,0), 3)
        # print(angle)
        
        #Finding percentage of angle at current time
        per = np.interp(angle, (220, 280), (0,100))          # (210, 310) are min and max points of angle of buceps curl and (0, 100) are percentage range 0 to 100 percent
        bar = np.interp(angle, (220, 280), (650, 100))
        
        color = (0, 255, 0)
        
        # Counting repetitions
        if per == 100:
            if dir == 0:
                color = (255 ,0, 255)
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                color = (0,255 ,0)
                count += 0.5
                dir = 0
        
        # Draw bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
        
        # Draw count rectangle
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (0, 0, 0), 3)
        
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
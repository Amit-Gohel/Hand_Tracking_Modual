import cv2
import mediapipe as mp
import HandTrakingModual as htm
import time
####c#############################################
wCam, hCam = 640, 480
pTime = 0
cBlue = (255, 0, 0)
#################################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    # 2. Get the tip of index and middle fingers
    # 3. check which fingers are up
    # 4. only Index Finger : Moving mode
    # 5. Convert Coordinates
    # 6. smoothen value
    # 7. move mouse
    # 8. both Index and middle fingers are up : Clicking mode
    # 9. Find distance between fingers
    # 10. click mouse if distance short

    # 11. frame rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f' FPS = {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, cBlue, 2)

    # 12. display
    cv2.imshow("img", img)
    cv2.waitKey(1)

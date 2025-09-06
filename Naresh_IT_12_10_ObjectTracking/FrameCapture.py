# if i press key then it keep goes to the next frame or else it pauses.

import cv2

cap = cv2.VideoCapture(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\12_NARESH_IT_DEEP_LEARNING\Naresh_IT_12_10_ObjectTracking\istockphoto-670217518-640_adpp_is.mp4")
while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)

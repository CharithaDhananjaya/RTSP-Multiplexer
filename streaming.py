import cv2
import numpy as np
from myfunctions import recognize

face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\charithap\\AppData\\Roaming\\Python\\Python36\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")

#cap_1 = cv2.VideoCapture('rtsp://admin:123456@192.168.1.13/output.h264')
cap_2 = cv2.VideoCapture(0)

while(True):
    #ret, frame = cap_1.read()
    ret, frame = cap_2.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=6)

    for(x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_color)
        recognize('my-image.png')

        color = (0, 255, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

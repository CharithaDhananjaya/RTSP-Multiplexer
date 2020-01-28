import rtsp

# add your rtsp url and type your username / password and IP of your NVR for the stream
with rtsp.Client(rtsp_server_uri= 'rtsp: // admin: 123456@192.168.1.13: 554') as client:
    client.preview()


import cv2 
cap = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
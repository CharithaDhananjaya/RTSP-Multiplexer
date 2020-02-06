import cv2
import requests
import json
from pygments import highlight, lexers, formatters


def jsonPrint(jsonobject):

    formatted_json = json.dumps(jsonobject, sort_keys=True, indent=2)
    colorful_json = highlight(
        formatted_json,
        lexers.JsonLexer(),
        formatters.TerminalFormatter())
    print(colorful_json)

    return 0


def recognize(faceimage):
    print('---------------------------------------------')
    url = "https://covi.real.com/people?insert=true&update=true&update-if-lower-quality=false&merge=true&regroup=false&detect-age=false&detect-gender=false&detect-sentiment=false&detect-occlusion=false&differentiate=false&similar_limit=0&linear-match=false&site=default&source=default&provide-face-id=true&min-cpq=-1&min-fsq=-1&min-fcq=-1&insert-profile=false&max-occlusion=-1&event=none&context=live&type=person&include-expired=false"

    payload = open(faceimage, 'rb').read()
    headers = {
        'Accept': 'application/json;charset=UTF-8',
        'X-RPC-DIRECTORY': 'main',
        'X-RPC-AUTHORIZATION': 'mobitelpvtltd3:mic@!123',
        'Content-Type': 'image/jpeg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsonPrint(json.loads(response.text.encode('utf8')))


def multiplexCameras(name):
    faceClassifier = cv2.CascadeClassifier(
        "C:\\Users\\charithap\\AppData\\Roaming\\Python\\Python36\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")

    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceClassifier.detectMultiScale(gray, scaleFactor=2, minNeighbors=6)

        for(x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            """img_item = "my-image.png"
            cv2.imwrite(img_item, roi_color)
            recognize('my-image.png')"""

            color = (0, 255, 0)
            stroke = 2
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv2.imshow(name, frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0

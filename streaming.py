import cv2
import concurrent.futures


"""face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\charithap\\AppData\\Roaming\\Python\\Python36\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")
"""

def Video_1(name):
    cap_1 = cv2.VideoCapture(0)
    while(True):
        ret_1, frame_1 = cap_1.read()

        cv2.imshow(name, frame_1)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    return 0

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        video = ['Video_1', 'Video_2']
        results = executor.map(Video_1,video)

if __name__ == '__main__':
    main()

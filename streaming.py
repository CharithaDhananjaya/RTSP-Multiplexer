import cv2
import concurrent.futures
from myfunctions import multiplexCameras

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        video = ['Video_1']
        results = executor.map(multiplexCameras,video)

if __name__ == '__main__':
    main()

#TODO: Need to check with 2 cameras RTSP feeds.
#TODO: Adding motion detection as well combined with facedetection.
#TODO: Multithreading or Async need to manage.
#TODO: Properly Logging and Saving the required. 
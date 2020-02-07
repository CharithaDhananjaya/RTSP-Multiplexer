import cv2
import asyncio
import concurrent.futures
from myfunctions import multiplexCameras


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:

        data = [["Camera_01", "rtsp://admin:123456@192.168.1.12/output.h264", "./src/Camera_01"],
                ["Camera_02", "rtsp://admin:123456@192.168.1.13/output.h264", "./src/Camera_02"]]

        results = executor.map(multiplexCameras, data)


if __name__ == '__main__':
    main()

# TODO: Need to check with 2 cameras RTSP feeds.
# TODO: Adding motion detection as well combined with facedetection.
# TODO: Multithreading or Async need to manage.
# TODO: Properly Logging and Saving the required.

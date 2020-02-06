import cv2
import concurrent.futures
from myfunctions import multiplexCameras

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        video = ['Video_1']
        results = executor.map(multiplexCameras,video)

if __name__ == '__main__':
    main()

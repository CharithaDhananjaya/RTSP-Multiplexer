import json

data = [["Camera_01", "rtsp://admin:123456@192.168.1.12/output.h264", "./src/Camera_01"],
        ["Camera_02", "rtsp://admin:123456@192.168.1.12/output.h264", "./src/Camera_01"]]

print(str(data[0][1]))

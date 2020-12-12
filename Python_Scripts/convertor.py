# $ python3 convertor.py -i ../original_video/example.mp4 -o ../original_video/output.mp4 -f 30 -c h264

from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to output video file")
ap.add_argument("-f", "--fps", type=int, default=30, help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="avc1", help="codec of output video")
ap.add_argument("-i", "--input", required=True, help="path to input video file")
args = vars(ap.parse_args())

cap = cv.VideoCapture(args["input"])
codec_info = list(args["codec"])
codec = cv.VideoWriter_fourcc(codec_info[0], codec_info[1], codec_info[2], codec_info[3])
writer = None
(h, w) = (None, None)
zeros = None

while True :
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    if writer is None:
        (h, w) = frame.shape[:2]
        writer = cv.VideoWriter(args["output"], codec, args["fps"], (w, h), True)
        zeros = np.zeros((h, w), dtype="uint8")

    # print(frame.shape)
    
    writer.write(frame)

    # cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
writer.release()
cv.destroyAllWindows()
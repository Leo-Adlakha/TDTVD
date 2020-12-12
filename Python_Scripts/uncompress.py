# $ python3 uncompress.py -i ../original_video/example.mp4 -o ../frames/

import numpy as np
import cv2 as cv
import shutil
import imutils
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to output frames folder")
ap.add_argument("-i", "--input", required=True, help="path to input video file")
args = vars(ap.parse_args())

out_dir = args["output"]
in_file = args["input"]

cap = cv.VideoCapture(in_file)
count = 1
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
# Clearing the folder for frames
shutil.rmtree(out_dir)
os.mkdir(out_dir)

    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    cv.imwrite(out_dir + "%d.jpg" % count, frame)
    count += 1
    
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
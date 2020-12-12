# Importing Required Libraries
import os
import cv2

# Initializing Parameters
input_folder = "Input_Videos/"
output_folder = "Output_Videos/"
codec = cv2.VideoWriter_fourcc('a','v','c','1')
input_files = os.listdir(input_folder)
out_size = (1920,1080)

# Main Program
for video in input_files:
    vid = cv2.VideoCapture(input_folder+video)
    out = cv2.VideoWriter(output_folder+video.split("")[0]+".avi", codec, 30.0, out_size)
    while vid.isOpened():
        ret, frame = vid.read()
        if(ret!=True):
            break
        frame = cv2.resize(frame,out_size)
        out.write(frame)
    vid.release()
    out.release()
import numpy as np
import cv2 as cv

txt_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input.txt"

with open(txt_file, "r") as my_input_file :
    data = my_input_file.read().splitlines(True)

for i in range(len(data)):
    data[i] = data[i].rstrip('\n')

for i in range(len(data)) :

    (insert_in, insert_from, start_ins, ins_start, ins_end) = data[i].split(" ")

    cap = cv.VideoCapture("../original_video/example.mp4")
    cap2 = cv.VideoCapture("../original_video/example2.mp4")
    codec = cv.VideoWriter_fourcc(*"h264")
    writer = None
    (h, w) = (None, None)
    ins_start = 30
    ins_end = 80
    start_ins = 100
    count = 0
    storage = []

    while True :
        
        ret, frame = cap2.read()
        if not ret :
            print("Can't receive frame (stream end?). Exiting ...")
            break
            
        count += 1
        
        if writer is None :
            (h, w) = frame.shape[:2]
        
        if count >= ins_start and count <= ins_end :
            storage.append(frame) 
            
        if cv.waitKey(1) == ord('q') :
            break 

    writer = cv.VideoWriter("../test/output_insertion.mp4", codec, 30, (w, h), True)
    count = 0 
    while True :
        
        ret, frame = cap.read() ;
        if not ret :
            print("Can't receive frame (stream end?). Exiting ...")
            break
            
        count += 1
            
        if cv.waitKey(1) == ord('q') :
            break 

    total_frames = count
    count = 0 
    cap = cv.VideoCapture("../original_video/example.mp4")

    while True :
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break 
            
        count += 1
            
        if count == start_ins :
            for i in storage :
                writer.write(i)
                count += 1
        
        if count == total_frames + 1 :
            break
        
        writer.write(frame)
        
        # Display the resulting frame
        # cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
            
    cap.release()
    cap2.release()
    writer.release()
    cv.destroyAllWindows()
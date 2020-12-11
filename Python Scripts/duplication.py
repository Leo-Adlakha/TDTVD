import numpy as np
import cv2 as cv

cap = cv.VideoCapture("../original_video/example.mp4")
codec = cv.VideoWriter_fourcc(*"h264")
writer = None
(h, w) = (None, None)
zeros = None
dup_start = 50
dup_end = 80
dup_ins = 140 
count = 1
storage = []

while True :
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if writer is None :
        (h, w) = frame.shape[:2]
    
    if count >= dup_start and count <= dup_end :
        storage.append(frame)
    
    count += 1
    
    # Display the resulting frame
#     cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

total_frames = count - 1
count = 0 
frames_left = total_frames - len(storage)
writer = cv.VideoWriter("../test/output_duplication.mp4", codec, 30, (w, h), True)
cap = cv.VideoCapture("../original_video/example.mp4")

while True :
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break 
    count += 1
        
    if count == dup_ins - 1 :
        for i in storage :
            writer.write(i)
            count += 1
            
    if count == total_frames :
        break 
    
    writer.write(frame)
    
    # Display the resulting frame
    # cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
        
cap.release()
writer.release()
cv.destroyAllWindows()
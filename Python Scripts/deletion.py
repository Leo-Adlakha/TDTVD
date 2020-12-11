import numpy as np
import cv2 as cv

cap = cv.VideoCapture("../original_video/example.mp4")
codec = cv.VideoWriter_fourcc(*"h264")
writer = None
(h, w) = (None, None)
zeros = None
del_start = 50
del_end = 80
count = 1

while True :
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if writer is None:
        (h, w) = frame.shape[:2]
        writer = cv.VideoWriter("../test/output_deletion.mp4", codec, 30, (w, h), True)
        zeros = np.zeros((h, w), dtype="uint8")
       
    if count >= del_start and count <= del_end :
        count += 1
        continue
    else :
        count += 1
        writer.write(frame)
    
    if cv.waitKey(1) == ord('q'):
        break
        
cap.release()
writer.release()
cv.destroyAllWindows()
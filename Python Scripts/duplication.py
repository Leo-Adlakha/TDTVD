import numpy as np
import cv2 as cv

txt_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_dup.txt"

with open(txt_file, "r") as my_input_file :
    data = my_input_file.read().splitlines(True)

for i in range(len(data)):
    data[i] = data[i].rstrip('\n')

for i in range(len(data)) :

    inp = data[i]
    got_addr = 0 
    last_idx = 0
    imp_data = []
    for j in range(len(inp)) :
        if inp[j:j+4] == 'mp4 ' :
            imp_data.append(inp[last_idx:j+3])
            got_addr += 1
            last_idx = j + 4
        
        if got_addr >= 1 : 
            inp = inp[last_idx:]
            break
            
    end_data = inp.split()
    imp_data.append(end_data)
    print(imp_data)

    cap = cv.VideoCapture(imp_data[0])
    codec = cv.VideoWriter_fourcc(*"h264")
    writer = None
    (h, w) = (None, None)
    zeros = None
    dup_ins = int(imp_data[1][0])
    dup_start = int(imp_data[1][1])
    dup_end = int(imp_data[1][2])
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
    writer = cv.VideoWriter("../Frame_Duplication/" + str(i+1) + ".mp4", codec, 30, (w, h), True)
    cap = cv.VideoCapture(imp_data[0])

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
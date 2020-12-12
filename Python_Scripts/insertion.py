import numpy as np
import cv2 as cv

txt_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_ins.txt"

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
        
        if got_addr >= 2 : 
            inp = inp[last_idx:]
            break
            
    end_data = inp.split()
    imp_data.append(end_data)
    # print(imp_data)

    cap = cv.VideoCapture(imp_data[0])
    cap2 = cv.VideoCapture(imp_data[1])
    codec = cv.VideoWriter_fourcc('a','v','c','1')
    writer = None
    (h, w) = (None, None)
    start_ins = int(imp_data[2][0])
    ins_start = int(imp_data[2][1])
    ins_end = int(imp_data[2][2])
    ins_type = imp_data[2][3]
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

    if ins_type == 'S' :
        writer = cv.VideoWriter("../Frame_Insertion/Same/" + str(i+1) + ".mp4", codec, 30, (w, h), True)
    else :
        writer = cv.VideoWriter("../Frame_Insertion/Different/" + str(i+1) + ".mp4", codec, 30, (w, h), True)

    count = 0 
    while True :
        
        ret, frame = cap.read() 
        if not ret :
            print("Can't receive frame (stream end?). Exiting ...")
            break
            
        count += 1
            
        if cv.waitKey(1) == ord('q') :
            break 

    total_frames = count
    count = 0 
    cap = cv.VideoCapture(imp_data[0])

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
import numpy as np
import cv2 as cv

txt_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_del.txt"

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
    # print(imp_data)

    cap = cv.VideoCapture(imp_data[0])
    codec = cv.VideoWriter_fourcc('a', 'v', 'c', '1')
    writer = None
    (h, w) = (None, None)
    del_start = int(imp_data[1][0])
    del_end = int(imp_data[1][1])
    count = 1

    while True :
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        if writer is None:
            (h, w) = frame.shape[:2]
            writer = cv.VideoWriter("../Frame_Deletion/" + str(i+1) + ".mp4", codec, 30, (w, h), True)
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
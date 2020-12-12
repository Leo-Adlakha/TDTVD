import csv

csv_file = ["/Users/leoadlakha/Documents/Research Work/TDTVD/csv/insertion.csv", "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/duplication.csv", "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/deletion.csv"]
txt_file = ["/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_ins.txt", "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_dup.txt", "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input_del.txt"]

for i in range(len(csv_file)) :
    with open(txt_file[i], "w") as my_output_file:
        with open(csv_file[i], "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)] 
        my_output_file.close()


    with open(txt_file[i], 'r') as input_file:
        data = input_file.read().splitlines(True)

    with open(txt_file[i], 'w') as output_file:
        output_file.writelines(data[1:])

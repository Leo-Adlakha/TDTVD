import csv

csv_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/insertion.csv"
txt_file = "/Users/leoadlakha/Documents/Research Work/TDTVD/csv/input.txt"

with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)] 
    my_output_file.close()


with open(txt_file, 'r') as input_file:
    data = input_file.read().splitlines(True)

with open(txt_file, 'w') as output_file:
    output_file.writelines(data[1:])

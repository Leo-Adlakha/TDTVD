#! /bin/bash
echo "Welcome to the Temporal Domain Tampering Pipeline."
echo "Hoping that you have already filled up the csv files for the input to the pipeline."
echo -n "---|"
for i in {1..50}
do
    echo -n "#"
done
echo "|---"
cd ../Python_Scripts/
python3 csv_to_input.py
python3 insertion.py
python3 duplication.py
python3 deletion.py

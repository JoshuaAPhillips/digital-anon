# imports

import os
import sys
import csv

# get data filename

file = sys.argv[-1]

# save raw data as list

def csvreader(file):

    try:
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            raw_data = []
            for row in reader:
                raw_data.append(row)
        #print(raw_data)
        return raw_data
    
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
        sys.exit(1)

    except csv.Error as e:
        print(f"Error reading CSV file {file}: {e}")
        sys.exit(1)

csvreader(file)

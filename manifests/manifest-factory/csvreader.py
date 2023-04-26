# imports

import os
import sys
import csv

# get data filename

file = sys.argv[-1]

# save data as tuple

def csvreader(file, dialect='excel'):
    data = []
    try:
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(tuple(row))
        return data
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
        sys.exit(1)
    except csv.Error as e:
        print(f"Error reading CSV file {file}: {e}")
        sys.exit(1)

csvreader(file)
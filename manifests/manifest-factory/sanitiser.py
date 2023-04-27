#imports

import sys
import csvreader

# get data filename

file = sys.argv[-1]

def sanitise(file):

    # pull raw data from CSV

    raw_data = csvreader.csvreader(file)

    # data cleanup - turns number-like strings into ints

    data = [[int(item) if item.isdigit() else item for item in sublist] for sublist in raw_data]
    
    return data

sanitise(file)
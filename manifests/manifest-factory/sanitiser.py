#imports

import sys
import csvreader

# get data filename

file = sys.argv[-1]

def sanitise(file):

    # pull raw data from CSV

    raw_data = csvreader.csvreader(file)

    # data cleanup - turns number-like strings into ints
    data = ()
    for tuple in raw_data:
        new_tpl = ()
        for item in tuple:
            if item.isdigit():
                new_tpl += (int(item),)
            else:
                new_tpl += (item,)
        data += new_tpl

    return data

sanitise(file)
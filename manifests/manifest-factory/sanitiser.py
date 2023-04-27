#imports

import sys
import csvreader

# get data filename

file = sys.argv[-1]

data = []

def sanitise(file):
    # pull raw data from CSV

    raw_data = csvreader.csvreader(file)

    # data cleanup - turns number-like strings into ints
    if not raw_data:
        print("Empty list!")

    else:

        for tuple in raw_data:
            new_tpl = ()
            for item in tuple:
                if item.isdigit():
                    new_tpl += (int(item),)
                elif type(item) is None:
                    continue
                else:
                    new_tpl += (item,)
        data.append(new_tpl)

    print(data)

sanitise(file)
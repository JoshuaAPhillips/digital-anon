# imports

import sys
from IIIFpres import iiifpapi3
import csvreader

# base manifest setup

iiifpapi3.BASE_URL = "https://iiif.io/api/cookbook/recipe/0009-book-1/"
manifest = iiifpapi3.Manifest()
manifest.set_id(extendbase_url="manifest.json")
manifest.add_label("en","Simple Manifest - Book")
manifest.add_behavior("paged")

# get data filename

file = sys.argv[-1]

# pull data from CSV

data = csvreader.csvreader(file)

print(data)


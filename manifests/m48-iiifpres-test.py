# imports

from IIIFpres import iiifpapi3
import csv
import os

# setup

iiifpapi3.BASE_URL = 'https://iiif.io/api/cookbook/recipe/0009-book-1/'
manifest = iiifpapi3.Manifest()

# ingest data into python-friendly format

with open('m48-data.csv', newline='') as data:
    data = csv.reader(data, delimiter=' ')
    for row in data:
        print(', '.join(row))

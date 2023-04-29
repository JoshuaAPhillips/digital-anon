import os
import csv

max = int(input("Please enter the number of pages for this document: "))
length = range(max)
doc = input("Please enter the m-number for this document: ")

def csvwriter():

  with open("{}-data.csv".format(doc), "x") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    
    for idx, i in enumerate(length):


        folio = 0
        w = 2766
        h = 3500
        base = f"https://llkn576nqxepo6yucgfh2nl2ea0kkigc.lambda-url.eu-west-2.on.aws/iiif/2/{doc}/{doc}-{i + 1}"
        service = "full/max/0/default.tif"

        newdata = [folio, w, h, base, service]
        writer.writerow(newdata)

csvwriter()

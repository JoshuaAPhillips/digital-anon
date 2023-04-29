import csv

# requests inputs

max = int(input("Please enter the number of pages for this document: "))
doc = input("Please enter the m-number for this document: ")

# sets constants

w = [2766 for i in range(max)]

h = [3500 for i in range(max)]

service = ["full/max/0/default.tif" for i in range(max)]

# creates variables

base = [f"https://llkn576nqxepo6yucgfh2nl2ea0kkigc.lambda-url.eu-west-2.on.aws/iiif/2/{doc}/{doc}-{i+1}" for i in range(max)]

# print(base)

folios = []
half_max = int(max / 2)

for i in range(1, half_max +1):
    folios.append(f"{i} recto")
    folios.append(f"{i} verso")

# print(pages)

rows = [folios, w, h, base, service]
print(rows)
# find a way of accessing the nth item from each list

def csvwriter(rows):

  with open(f"{doc}-data.csv", "x") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for idx in range(len(rows[0])):
      row = [inner_list[idx] for inner_list in rows]
      writer.writerow(row)

csvwriter(rows)

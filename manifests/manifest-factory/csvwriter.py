import csv

class Document:
    
    def __init__(self, max_pages, doc_number):
        self.max_pages = max_pages
        self.doc_number = doc_number

        # sets constants

        self.widths = [2766 for i in range(max_pages)]
        self.heights = [3500 for i in range(max_pages)]
        self.services = ["full/max/0/default.tif" for i in range(max_pages)]

        # sets base URI

        self.base_urls = [f"https://llkn576nqxepo6yucgfh2nl2ea0kkigc.lambda-url.eu-west-2.on.aws/iiif/2/m{doc_number}/m{doc_number}-{i + 1}" for i in range(max_pages)]

        # sets foliation

        self.folios = []
        half_max = int(max_pages / 2)

        for i in range(1, half_max + 2):
            self.folios.append(f"{i} recto")
            self.folios.append(f"{i} verso")

        self.thumbs = [f"https://llkn576nqxepo6yucgfh2nl2ea0kkigc.lambda-url.eu-west-2.on.aws/iiif/2/m{doc_number}/thumbs/thumb_m{doc_number}-{i + 1}" for i in range(max_pages)]
            
        self.rows = [self.folios, self.widths, self.heights, self.base_urls, self.services, self.thumbs]

        print(self.max_pages)
        print(self.doc_number)

    def status(self):
        print(f"Output: {self.doc_number} saved... \n")

    def write_csv(self):
        with open(f"./data/m{self.doc_number}-data.csv", "w") as csv_file:
            print(f"{self.doc_number} saved to CSV... \n")
            writer = csv.writer(csv_file, delimiter=',')
            for idx in range(len(self.rows[0])):
                row = [inner_list[idx] for inner_list in self.rows]
                writer.writerow(row)

    def __del__(self):
        print(f"{self.doc_number} destroyed")

newdoc = Document(1, "m54-11")
newdoc.write_csv()
del(newdoc)

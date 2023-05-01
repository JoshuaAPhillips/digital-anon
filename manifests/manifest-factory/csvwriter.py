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
            
        self.rows = [self.folios, self.widths, self.heights, self.base_urls, self.services]

    def write_csv(self):
        with open(f"m{self.doc_number}-data.csv", "x") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for idx in range(len(self.rows[0])):
                row = [inner_list[idx] for inner_list in self.rows]
                writer.writerow(row)
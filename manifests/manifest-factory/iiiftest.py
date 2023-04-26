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

# where the magic happens

for idx, i in enumerate(data):
    idx +=1

    # set canvas properties

    canvas = manifest.add_canvas_to_items()
    canvas.set_id(extendbase_url="canvas/p%s"%idx)
    canvas.set_height(data[2])
    canvas.set_width(data[1])
    canvas.add_label("en", data[0])

    # set canvas annotations - create annopage object for each canvas

    annopage = canvas.add_annotationpage_to_items()

    # add annotation (i.e., facsimile taking up entire canvas) to annopage and provide information

    annopage.set_id(extendbase_url="page/p%s/1"%idx)
    annotation = annopage.add_annotation_to_items(target=canvas.id)
    annotation.set_id(extendbase_url="annotation/p%s-image"%str(idx).zfill(4))
    annotation.set_motivation("painting")
    annotation.body.set_id("".join(data[3]))
    annotation.body.set_type("Image")
    annotation.body.set_format("image/jpeg")
    annotation.body.set_width(data[1])
    annotation.body.set_height(data[2])

    # specify service for above canvas annotations

    service = annotation.body.add_service()
    service.set_id(data[3])
    service.set_type("ImageService3")
    service.set_profile("level1")

# finishing touches - inspecting canvas for required and recommended properties, and saving out JSON file

canvas.inspect()
manifest.show_errors_in_browser()
#manifest.json_save()

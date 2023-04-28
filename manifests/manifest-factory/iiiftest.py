# imports
"""
import sys
from IIIFpres import iiifpapi3
import sanitiser
"""
import metadata
"""
# base manifest setup
iiifpapi3.BASE_URL = "https://iiif.io/api/cookbook/recipe/0009-book-1/"
manifest = iiifpapi3.Manifest()
manifest.set_id(extendbase_url="manifest.json")
manifest.add_label("en","M48 test manifest")
manifest.add_behavior("paged")

# get data filename

file = sys.argv[-1]

# pull data from CSV and sanitises

data = sanitiser.sanitise(file)
"""
metadata_filename = metadata.getfilename()
metadata_root = metadata.getRoot(metadata_filename)
metadata_raw = metadata.metadataParse(metadata_root)
metadata_dict = metadata.metadataDict()

print(metadata_dict)

# where the magic happens
"""
def manifestFactory():


    if data is not None:

        for idx, i in enumerate(data):

            # set canvas properties

            canvas = manifest.add_canvas_to_items()
            canvas.set_id(extendbase_url="canvas/p%s"%idx)
            canvas.set_height(data[idx][2])
            canvas.set_width(data[idx][1])
            canvas.add_label("en", data[idx][0])

            # set canvas annotations - create annopage object for each canvas

            annopage = canvas.add_annotationpage_to_items()

            # add annotation (i.e., facsimile taking up entire canvas) to annopage and provide information

            annopage.set_id(extendbase_url="page/p%s/1"%idx)
            annotation = annopage.add_annotation_to_items(target=canvas.id)
            annotation.set_id(extendbase_url="annotation/p%s-image"%str(idx).zfill(4))
            annotation.set_motivation("painting")
            annotation.body.set_id(data[idx][3])
            annotation.body.set_type("Image")
            annotation.body.set_format("image/jpeg")
            annotation.body.set_width(data[idx][1])
            annotation.body.set_height(data[idx][2])

            # specify service for above canvas annotations

            service = annotation.body.add_service()
            service.set_id(data[idx][3])
            service.set_type("ImageService3")
            service.set_profile("level1")

        # finishing touches - inspects manifest for required and recommended properties

        manifest.inspect()
        
        # asks for a filename for the file output and saves out .json file

        # filename = input("Please enter a name for this file: ")
        # manifest.json_save('{}.json'.format(filename))
        manifest.show_errors_in_browser()

    else:
        print("Data is None :()")
        """

# imports

import sys
from IIIFpres import iiifpapi3
import sanitiser
import metadata
from metadata import *

# pull data from CSV (specified as argument when program run) and sanitises

file = sys.argv[-1]
data = sanitiser.sanitise(file)

# pulls metadata from given XML (input) into dictionary

metadata_dict = metadata.metadataDict(idno, title, author, editor, summary, provider, repository)

print(metadata_dict)

# where the magic happens

def manifestFactory():

    # sets manifest-level properties

    iiifpapi3.BASE_URL = "https://iiif.io/api/cookbook/recipe/0009-book-1/"
    manifest = iiifpapi3.Manifest()
    manifest.set_id("https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/manifests/{}-manifest.json".format(metadata_dict["idno"]))
    manifest.add_label("en",metadata_dict["title"])
    manifest.add_behavior("paged")
    manifest.add_metadata("Author:",metadata_dict["author"],"en", "en")
    manifest.add_metadata("Editor:",metadata_dict["editor"],"en", "en")
    manifest.add_metadata("Repository:", metadata_dict["repository"], "en", "en")
    manifest.add_summary("en", metadata_dict["summary"])
    manifest.set_requiredStatement("Copyright: ", metadata_dict["provider"],"en","en")

    # sets manifest-level thumbnails

    thumb = manifest.add_thumbnail()
    thumb.set_id(data[0][-1])
    thumb.set_type("Image")
    thumb.set_format("image/jpeg")
    thumb.set_hightwidth("386", "300")
    thumb.add_label("en", "Thumbnail")


        # sets provider information

    provider = manifest.add_provider()
    provider.set_id("https://www2.societyofauthors.org")
    provider.add_label("en", metadata_dict["provider"])

    # generates canvases and sets canvas-level properties

    if data is not None:

        for idx, i in enumerate(data):

            canvas = manifest.add_canvas_to_items()
            canvas.set_id(extendbase_url="canvas/p%s"%idx)
            canvas.set_height(data[idx][2])
            canvas.set_width(data[idx][1])
            canvas.add_label("en", data[idx][0])

            # sets canvas-level thumbnails

            canvas_thumb = canvas.add_thumbnail()
            canvas_thumb.set_id(data[idx][-1])
            canvas_thumb.set_type("Image")
            canvas_thumb.set_format("image/jpeg")
            canvas_thumb.set_hightwidth("386", "300")
            canvas_thumb.add_label("en", "Thumbnail")

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

            # specify service (i.e., deep zoom capability) for above canvas annotations

            service = annotation.body.add_service()
            service.set_id(data[idx][3])
            service.set_type("ImageService3")
            service.set_profile("level1")

        # finishing touches - inspects manifest for required and recommended properties

        manifest.inspect()
        
        # asks for a filename for the file output and saves out .json file

        # filename = input("Please enter a name for this file: ")
        manifest.json_save('./../{}-manifest.json'.format(metadata_dict["idno"]))
        # manifest.show_errors_in_browser()

    else:
        print("Data is None :()")

manifestFactory()
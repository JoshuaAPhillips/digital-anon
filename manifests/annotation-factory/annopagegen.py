import json
import xmlparser
from xmlparser import Parser
from IIIFpres import iiifpapi3


class annotationPage:

    # initialises class

    def __init__(self) -> None:
        return
    
    # streams xml from xmlparser()

    def xmlParser(self):
        xml = xmlparser.Parser()
        print(xml)

    # returns JSON file

    def toJson(self):
        items = []
        for item in self.items:
            item = {
                "id": id,
                "type": "Annotation",
                "motivation": "Commenting",
                "body": {
                    "type": "TextualBody",
                    "language": "en",
                    "format": "text/html",
                    "value": self.annotation_value
                }
            }
            items.append(item)

        annotationPage = {
            "@context": self.context,
            "id": self.page_id,
            "type": "AnnotationPage",
            "items": self.items
        }
        return json.dumps(annotationPage, indent=4)
    
test = annotationPage()

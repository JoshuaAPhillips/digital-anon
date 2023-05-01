import json
import os

class annotationPage:

    # initialises class

    def __init__(self, context, page_id, type, items) -> None:
        self.context = context
        self.page_id = page_id
        self.type = type
        self.items = items

    # ???

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
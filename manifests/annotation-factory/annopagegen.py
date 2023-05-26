import json
import xmlparser
from xmlparser import *
    
# streams xml from xmlparser()

def xmlParser():
    global idno, xml, facs_list, child_list

    idno = xmlparser.idno.text
    facs_list = xmlparser.facs_list
    child_list = xmlparser.child_list

    # print(idno, xml)

    return idno, facs_list, child_list

# creates JSON

def toJson(idno, facs_list, child_list):

    global annotation_page
    annotation_page = {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "id": f"https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/manifests/{idno}-annotations.json",
        "type": "Manifest",
        "items": []
    }

    for i in child_list:
        counter = 1
        annotation = {
            "id": f"https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/manifests/{idno}-annotation-{counter}.json",
            "type": "Annotation",
            "motivation": "Commenting",
            "target": facs_list[counter],
            "body": {
                "type": "TextualBody",
                "language": "en",
                "format": "text/html",
                "body": child_list[counter]
            }
        }
        annotation_page["items"].append(annotation)
        counter += 1

xmlParser()
toJson(idno, facs_list, child_list)

print(json.dumps(annotation_page, indent=4))

with open (f"{idno}-annotations.json", "w") as json_file:
    json.dump(annotation_page, json_file, indent=4)


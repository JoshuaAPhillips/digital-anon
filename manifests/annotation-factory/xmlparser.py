import xml.etree.ElementTree as ET
import sys

global filename
PATH = '../../transcriptions/'

class Parser():
    
    def __init__(self) -> None:
        return
    
    # gets file path for parsing

    def getFile(self):
        filename = sys.argv[-1]
        xmlfile = PATH + filename
        # print(xmlfile)
        return xmlfile
    
    # parses root and streams to metadataParse()

    def getRoot(self):
        xmlfile = self.getFile()
        tree = ET.parse(xmlfile)

        root = tree.getroot()
        return root
    
    def parse(self):
        xmlfile = self.getFile()
        root = self.getRoot()
        # print(root)

        # get idno for document

        global idno
        idno = root.find('.//{http://www.tei-c.org/ns/1.0}msIdentifier/{http://www.tei-c.org/ns/1.0}idno')
        print(idno.text)

        # get children of divs which have @facs attributes

        facs = root.findall('.//{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}*[@facs]')

        # return children as list of strings

        element_list = []

        for element in facs:

            child_string = ET.tostring(element, encoding="unicode")
            list_element = ({
                "facs": element.attrib,
                "value": child_string
            })
            element_list.append(list_element)
        print(element_list)
        return element_list
    
test = Parser()
test.parse()

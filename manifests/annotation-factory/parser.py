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
        #mprint(xmlfile)
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
        print(root)

        # get idno for document

        idno = root.find('.//{http://www.tei-c.org/ns/1.0}msIdentifier/{http://www.tei-c.org/ns/1.0}idno')
        print(idno.text)

        # get children of divs which have @facs attributes

        facs = root.findall('.//{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}*[@facs]')

        # return children as string

        for i in facs:
            print(i.attrib)
            child_string = ET.tostring(i, encoding="unicode")
            # print(child_string)

            return child_string

    
test = Parser()
test.parse()

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
    
    # gets root and streams to parse()

    def getRoot(self):
        xmlfile = self.getFile()
        tree = ET.parse(xmlfile)

        root = tree.getroot()
        return root
    
    #  parses root and gets idno, list of @facs attribs and list of 
    
    def parse(self):
        xmlfile = self.getFile()
        root = self.getRoot()
        # print(root)

        # get idno for document

        global idno
        idno = root.find('.//{http://www.tei-c.org/ns/1.0}msIdentifier/{http://www.tei-c.org/ns/1.0}idno')
        #print(idno.text)

        # get children of divs which have @facs attributes

        facs = root.findall('.//{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}*[@facs]')

        # exports list of facs attribs
    
        global facs_list

        facs_list = []
        for i in facs:
            facs_list.append(i.attrib["facs"])
        print(facs_list)

        # exports list of children for each @facs attrib

        global child_list

        child_list = []

        for i in facs:
            raw_child_string = ET.tostring(i, encoding="unicode")
            sanitised_string_list = []

            # sanitises list of children

            split_child_string = raw_child_string.split("\n")
            for j in split_child_string:
                child_string = j.strip()
                sanitised_string_list.append(child_string)
            child_list.append(sanitised_string_list)
        #print(child_list)

        return facs_list, child_list

parser = Parser()
parser.parse()

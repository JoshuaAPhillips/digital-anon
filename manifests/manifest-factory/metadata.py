# imports

import xml.etree.ElementTree as ET

# get filename

def getfilename():

    filename = input("Please enter the metadata filename: ")
    global xml_file 
    xml_file = '../../transcriptions/v2/{}'.format(filename)
    return xml_file

# parses root and streams to metadataParse()

def getRoot(xml_file):

    parser = ET.XMLParser(encoding='UTF-8')
    tree = ET.parse(xml_file)
    global root
    root = tree.getroot()
    print(root.tag)
    return root

# pulls out metadata items

def metadataParse(root):

    # teiHeader = root.find('./{http://www.tei-c.org/ns/1.0}teiHeader')
    title = root.find('.//{http://www.tei-c.org/ns/1.0}title')
    print(title.text)

getfilename()
getRoot(xml_file)
metadataParse(root)
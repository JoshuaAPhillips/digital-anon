# imports

import xml.etree.ElementTree as ET

# get filename

def getfilename():

    filename = input("Please enter the metadata filename: ")
    global xml_file 
    xml_file = '../../transcriptions/v2/{}'.format(filename)
    return xml_file

# pull metadata from xml

def metadataParse(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    print(root)

getfilename()
print(xml_file)
metadataParse(xml_file)
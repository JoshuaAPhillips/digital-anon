# imports

import xml.etree.ElementTree as ET

global metadata_dict

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
    return root

# pulls out metadata items

def metadataParse(root):

    global title, author, editor, summary, provider, repository

    # title
    title = root.find('.//{http://www.tei-c.org/ns/1.0}title')
    #print(title.text)

    # author
    author = root.find('.//{http://www.tei-c.org/ns/1.0}author')
    #print(author.text)

    # editor (me!)
    editor = root.find('.//{http://www.tei-c.org/ns/1.0}respStmt/{http://www.tei-c.org/ns/1.0}name')
    #print(editor.text)

    # summary
    summary = root.find('.//{http://www.tei-c.org/ns/1.0}physDesc/{http://www.tei-c.org/ns/1.0}p')
    #print(summary.text)

    # provider/copyright (required statement?)
    provider_a = root.find('.//{http://www.tei-c.org/ns/1.0}authority')
    provider_b = root.find('.//{http://www.tei-c.org/ns/1.0}availability/{http://www.tei-c.org/ns/1.0}p')
    provider = provider_a.text + ". " + provider_b.text + "."
    #print(provider)

    # repository
    repo_a = root.find('.//{http://www.tei-c.org/ns/1.0}institution')
    repo_b = root.find('.//{http://www.tei-c.org/ns/1.0}repository')
    repository = repo_a.text + ", " + repo_b.text + "."
    #print(repository)

    return title.text, author.text, editor.text, summary.text, provider, repository

# does the thing

getfilename()
getRoot(xml_file)
metadataParse(root)

def metadataDict(title, author, editor, summary, provider, repository):

    # creates and returns dictionary of metadata
    
    global metadata_dict
    metadata_dict = dict(
        title = title.text,
        author = author.text,
        editor = editor.text,
        summary = summary.text,
        provider = provider,
        repository = repository
        )
    #print(metadata_dict)
    return metadata_dict

metadataDict(title, author, editor, summary, provider, repository)

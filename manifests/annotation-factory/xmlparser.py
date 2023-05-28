import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import json
import sys

BASE_URL = 'https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/transcriptions/'

class xmlParser:

  def __init__(self) -> None:
    return

  def getFilename(self):
    """
    gets name of XML file to open and appends to BASE_URL
    """
    global idno
    idno = sys.argv[-1]
    filename = BASE_URL + idno
    return filename

  def getFile(self):

    """
    requests XML from address specified in {filename}
    """

    filename = self.getFilename()

    print(f"Loading file from URL: {filename}")
    r = requests.get(filename)
    return r

  def makeSoup(self):

    """
    returns text of requested file as a BeautifulSoup object
    """

    r = self.getFile()
    soup = BeautifulSoup(r.text, 'xml')
    return soup
  
  def allDivs(self):
    soup = self.makeSoup()
    all_divs = soup.find_all('div')
    return all_divs

  def facsDict(self):

    """
    returns a dictionary of facs attributes arranged by div
    """

    all_divs = self.allDivs()

    facs_dict = {}
    for div in all_divs:
        parent_facs = div.get('facs')
        children = div.find_all(attrs={'facs': True})
        
        child_facs_list = []
        
        for child in children:
            child_facs_list.append(child.get('facs'))
        
        facs_dict[parent_facs] = child_facs_list
    return facs_dict

  """def childDict(self):
      
      
      returns a dictionary of child attributes arranged by div --- doesn't work...
      
      all_divs = self.allDivs()

      n = [div.get("n") for div in all_divs]
      pp(n)

      for div in all_divs:
         child_sublist = []
         for child in div:
            sub_child = str(child).strip()
            child_sublist.append(sub_child)

      child_dict = dict(zip(n, child_sublist))
      return child_dict
"""
  def toJson(self):
     
     """
     saves dicts to Json
     """
     facs_dict = self.facsDict()
     child_dict = self.childDict()

     with open ('./annodata/{}-facs.json'.format(idno.strip('.xml')), 'w') as json_file:
        json.dump(facs_dict, json_file, indent=4)

     """
     with open ('./annodata/{}-children.json'.format(idno.strip('.xml')), 'w') as json_file:
        json.dump(child_dict, json_file, indent=4)
     """
test = xmlParser()
test.toJson()
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


test = xmlParser()
test.makeSoup()
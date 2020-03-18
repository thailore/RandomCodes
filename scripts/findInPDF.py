# import packages
import PyPDF2
import re
from urllib.request import urlopen
from io import StringIO

pdfUrl = input("Enter pdf to be searched: ")
searchTerm = input("Enter search term: ")

# open the pdf file
remoteFile = urlopen(pdfUrl).read()
print(remoteFile)
memoryFile = StringIO(remoteFile)
object = PyPDF2.PdfFileReader(memoryFile)

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = searchTerm

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)

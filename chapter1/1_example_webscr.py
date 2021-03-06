# First draft of .py file
# from urllib2 import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(), "html5lib")
# print(bsObj.h1)

from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj= BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print('Title could not be found')
else:
	print(title)
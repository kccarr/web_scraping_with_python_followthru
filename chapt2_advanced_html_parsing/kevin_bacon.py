from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html5lib")

for link in bsObj.findAll("a"):
	if "href" in link.attrs:
		print(link.attrs["href"])
# If you want to find only descandants that are children, you can use the .children tag:
from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table", {"id":"giftList"}).children:
	print(child)
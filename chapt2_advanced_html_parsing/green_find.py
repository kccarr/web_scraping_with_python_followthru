from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text())



nameList = bsObj.findAll(text="the prince")
print(len(nameList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text)

allTags = bsObj.findAll("span", {"class":{"green", "red"}})
for tag in allTags:
	print(tag.get_text())
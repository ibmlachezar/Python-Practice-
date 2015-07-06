import requests
from bs4 import BeautifulSoup

'''
#Get links
r = requests.get("http://www.yellowpages.com/search?search_terms=coffocation_terms=San+Francisco%2C+CA")
#print r.content

soup = BeautifulSoup(r.content)

#print soup.prettify()
# This gives a lsit of links
b = soup.find_all("a")

for link in b:
	#prints all links
	#print link.get("href")
	#print link.text
	#print link.text, link.get("href")
	print  "<a href='%s >%s</a>" %(link.get("href"), link.text)
'''

url = "http://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=San+Francisco%2C+CA"

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")
'''
for link in links:
	if "http" in link:
		 print "<a href ='%a'>%s</a>" %(link.get("href"),link.text)

'''
g_data = soup.find_all("div",{"class":"info"})
#prnts a list of data
#print g_data

'''
#print it nicely
for item in g_data:
	print item.text
'''
'''
#will print a list of lists[[1],[2]...]
for item in g_data:
	print item.contents
'''
#will print the first of the children of the info tag
for item in g_data:
	#PRINTS the second div element
	#print item.contents[1]
	print item.contents[0].find_all("a",{"class":"business-name"})[0].text
	#print item.contents[1].find_all("p",{"class":"adr"})[0].text

	try:	
		print item.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text

	except:
		pass
	try:	
		print item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text.replace(",","")

	except:
		pass
	try:	
		print item.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text

	except:
		pass
	try:	
		print item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].tex

	except:
		pass
	try:

		print item.contents[1].find_all("div",{"class":"phones phone primary"})[0].text

	except:
		pass	

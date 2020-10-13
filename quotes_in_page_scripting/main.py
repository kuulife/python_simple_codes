import requests
from bs4 import BeautifulSoup


res = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(res.text, 'lxml')
author = soup.select('.author')
author_set = set()

for i in author:
	author_set.add(i.text)
#printing authors in first page of website
print(author_set)

print('\n')

quotes =  soup.select('.text')
li = []
for i in quotes:
	li.append(i.text)
#printing list of quotes in first page
print(li)


topten = soup.select('.tag-item')
for i in topten:
	print(i.text) #printing top ten tags
 
 #loop through all the website pages and print all authors in each page

url = 'http://quotes.toscrape.com/page/'
page_still_valid = True
authors = set()
page = 1
while page_still_valid:
	page_url = url+str(page)

	res = requests.get(page_url)
	if 'No quotes found!' in res.text:
		break

	soup = BeautifulSoup(res.text, 'lxml')

	for name in soup.select('.author'):
		authors.add(name.text)
	page += 1
#printing all authors that exist in website
print(authors)





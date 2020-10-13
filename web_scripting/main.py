import requests
from bs4 import BeautifulSoup

#we are gonna scripting this website
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
#get requests
res = requests.get(base_url.format(1))

soup = BeautifulSoup(res.text, 'lxml')

#take a class called .product_pod
products  = soup.select('.product_pod') 

two_star_title = []


for n in range(1,51):
	scrape_url = base_url.format(n)
	res = requests.get(scrape_url)

	soup = BeautifulSoup(res.text, 'lxml')
	books = soup.select('.product_pod')

	for book in books:
		if len(book.select('.star-rating.Two')) != 0:
			book_title = book.select('a')[1]['title']
			two_star_title.append(book_title)
			
print(two_star_title)
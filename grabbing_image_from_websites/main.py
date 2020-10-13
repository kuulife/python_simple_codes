import requests
from bs4 import BeautifulSoup

#choose which imgage in which website to download
#and get requst to that website and continue step below

#make get request to the website
result = requests.get('https://ru.dota2.com')

#use to soup to beautify your response
soup = BeautifulSoup(result.text, 'lxml')

#inspect website to find scr of image 
img = soup.select('.entry-content img')[3]

#printing image src
print(img['src'])

#assigning image source to the variable
img_url = img['src']

#making new request to the image url
#and create file with name dota2.png
#beacause our image link is in png format
#wb is: > write binary
res = requests.get(img_url)
with open('dota3.png','wb') as f:
	f.write(res.content)



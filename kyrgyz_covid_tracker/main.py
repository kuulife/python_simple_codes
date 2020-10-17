import requests
from bs4 import BeautifulSoup

res = requests.get('https://covid.kg/ru')
soup = BeautifulSoup(res.text, 'lxml')
covid = soup.select('.data-number.data-today')[0].text.strip()
print('today Covid Disease cases :',covid+' in Kyrgyzstan')
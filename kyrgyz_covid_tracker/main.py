import requests
from bs4 import BeautifulSoup

res = requests.get('https://covid.kg/ru')
soup = BeautifulSoup(res.text, 'lxml')

data_recovered = soup.select('.data-recovered')[0].text.strip()
covid_cases = soup.select('.data-number.data-today')[0].text.strip()
data_name = soup.select('.data-name')[0].text.strip()
data_info = soup.select('.data-info')[0].text.strip()
data_title = soup.select('.data-title')[0].text.strip()
data_title_recovered = soup.select('.data-title')[1].text.strip()
data_death = soup.select('.data-death')[0].text.strip()
data_title_death = soup.select('.data-title')[2].text.strip()

print(data_name)
print(data_info+'\n')

print(f'{data_title}: {covid_cases}')
print(f'{data_title_recovered}: {data_recovered}')
print(f'{data_title_death}: {data_death}')
print('\n')
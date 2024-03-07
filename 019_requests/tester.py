import requests
from bs4 import BeautifulSoup

url = 'https://xkcd.com/353'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.a['href'])
match = soup.find('div', id='topContainer')

print(list(match.children))
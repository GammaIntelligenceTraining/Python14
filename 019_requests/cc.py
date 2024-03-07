import requests
from bs4 import BeautifulSoup as BS


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

usd_to_yen = 'https://www.google.com/search?q=usd+to+yen&sca_esv=580203348&sxsrf=AM9HkKljYpDpb6Elx7-K2uTDEh5p2fNYOQ%3A1699382694347&source=hp&ei=poVKZcyWEJySxc8ProCEkAI&iflsig=AO6bgOgAAAAAZUqTtnm0fdOmfoEJs3ffYobOruZcXjUH&ved=0ahUKEwjMgdHuxbKCAxUcSfEDHS4AASIQ4dUDCAo&uact=5&oq=usd+to+yen&gs_lp=Egdnd3Mtd2l6Igp1c2QgdG8geWVuMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEiuMlAAWM4vcAB4AJABAJgB7gGgAZENqgEFMC44LjK4AQPIAQD4AQHCAgcQIxiKBRgnwgIIEAAYigUYkQLCAgUQLhiABMICCxAuGIAEGMcBGNEDwgIHEC4YigUYQ8ICBxAAGIoFGEPCAg0QLhiKBRjHARjRAxhDwgIHEAAYgAQYCg&sclient=gws-wiz'
response = requests.get(usd_to_yen, headers=headers)

soup = BS(response.content, 'html.parser')

data = soup.find('span', class_='DFlfde SwHCTb')
print(float(data.text.replace(',', '.')))
print(type(data['data-value']))
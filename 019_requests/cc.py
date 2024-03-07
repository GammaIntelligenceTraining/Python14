import requests
from bs4 import BeautifulSoup

eur_yen = 'https://www.google.com/search?q=euro+to+yen&sca_esv=ed313d50f24d50b8&sxsrf=ACQVn09tQoELQAQADdp6kzE51t3gh0fl6w%3A1709835614783&ei=XgXqZc-PL5WO9u8PxNq6yAw&ved=0ahUKEwjPtsWD4uKEAxUVh_0HHUStDskQ4dUDCBA&uact=5&oq=euro+to+yen&gs_lp=Egxnd3Mtd2l6LXNlcnAiC2V1cm8gdG8geWVuMhAQABiABBiKBRiRAhhGGIICMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMhwQABiABBiKBRiRAhhGGIICGJcFGIwFGN0E2AEBSMkOUN4FWPcJcAF4AZABAJgBpwGgAfwDqgEDMS4zuAEDyAEA-AEBmAIEoAKiA8ICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIIEAAYBxgeGA_CAgsQABiABBiKBRiRAsICBxAAGIAEGAqYAwCIBgGQBgq6BgYIARABGBOSBwMxLjOgB4UX&sclient=gws-wiz-serp'
aud_gbp = 'https://www.google.com/search?q=aud+to+gbp&sca_esv=ed313d50f24d50b8&sxsrf=ACQVn09ZdSBNSD6r_9Eb0-dESWlPhkjzDQ%3A1709835634048&ei=cgXqZYeyAtHs7_UPxLui0AM&ved=0ahUKEwiHs92M4uKEAxVR9rsIHcSdCDoQ4dUDCBA&uact=5&oq=aud+to+gbp&gs_lp=Egxnd3Mtd2l6LXNlcnAiCmF1ZCB0byBnYnAyDxAAGIAEGIoFGEMYRhiCAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIbEAAYgAQYigUYQxhGGIICGJcFGIwFGN0E2AEBSJUjUABYiBpwAXgBkAEAmAHFAqAB3QyqAQczLjYuMS4xuAEDyAEA-AEBmAIMoALtDcICCxAuGIAEGMcBGNEDwgIFEC4YgATCAgoQABiABBiKBRhDwgILEC4YgAQYxwEYrwHCAgoQABiABBgUGIcCwgIMEAAYgAQYChhGGIICwgIHEAAYgAQYCsICCBAAGBYYHhgKwgIGEAAYFhgewgIYEAAYgAQYChhGGIICGJcFGIwFGN0E2AEBmAMAugYGCAEQARgTkgcHMi44LjEuMaAH6Uo&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def convert(url):
    response = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # price = float(soup.find('span', class_='DFlfde SwHCTb').text.replace(',', '.'))
    price = float(soup.find('span', class_='DFlfde SwHCTb')['data-value'])
    return price


print(1000 * convert(eur_yen))
print(1000 * convert(aud_gbp))
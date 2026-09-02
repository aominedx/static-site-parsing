import requests
from bs4 import BeautifulSoup
from time import sleep
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

def get_url():
    for count in range(2,3): #выбрать количество страниц в зависимости от сайта\желания
        url = f"https://killprice24.ru/catalog/samsung-galaxy?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        data = soup.find_all('li', class_='col-lg-6 col-md-8 col-xs-12')
        for item in data:
            card_url = "https://killprice24.ru/" + item.find('div', class_='image').find('a').get('href')
            yield card_url

def parse():
    for card_url in get_url():

        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        data = soup.find('section', class_='col-md-18 col-md-push-6')

        name = data.find('div', class_='heading').find('h1').text
        price = data.find('div', class_='price').find('span').text
        text = data.find('div', class_='tabsBlock').find('div', class_='tab-pane fade in active').text
        url_img = data.find('div', class_='image').find('img').get('src')
        yield name,price,text,url_img

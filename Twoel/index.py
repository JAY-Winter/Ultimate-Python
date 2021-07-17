import requests
from bs4 import BeautifulSoup
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://www.twoel.net/shop_goods/goods_list.htm?category=0I000000')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('div.glores-A-goods-sort.topSort')
latest = posts.text

with open(os.path.join(BASE_DIR, 'latest.text'), 'w+') as f:
    f.write(latest)


#container > div.subContent > div > div.pdList > ul > li:nth-child(1) > a > dl > dt > span
#container > div.subContent > div > div.pdList > ul > li:nth-child(2) > a > dl > dt > span
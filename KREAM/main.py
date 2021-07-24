<<<<<<< HEAD
# import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError

url = "https://kream.co.kr/products/28721?size=280"

try:
    html_open = urlopen(url)
except HTTPError as e:
    print(e)
else:
    html_soup = BeautifulSoup(html_open.read(),'lxml')
    print(html_soup)
=======
404 not found !
>>>>>>> adde03bdae20124a2d85de291a7b36f36c2beb04

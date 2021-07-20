import requests
from bs4 import BeautifulSoup
from page import page_list


def max_page():
    page_list()


    maxVal = len(pages)
    print(maxVal)

max_page()
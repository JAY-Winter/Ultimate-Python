import requests
from bs4 import BeautifulSoup

# 기본 구조

# url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91&limit=50'
# html = requests.get(url)
# soup = BeautifulSoup(html.text, 'html.parser')


# lables = soup.find("ul", {'class' : 'pagination-list'})
# # print(lables)

# aria = lables.get('aria-label')
# print(aria)
# print(lables.get('aria-label'))


# print(lables)
# aria = lables.find('b')
# aria = lables.find('a')
# aria = lables.find({'aria-label':1},'a')

# print(aria.string)
# print(aria)


# def page():
    

    # 1 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0
    # 2 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=50
    # 3 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=100
    # 4 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=150
    # 5 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=200
    # 6 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=250
    # 7 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=300
    # https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=350




def max_url():
    n = 0
    i = 0
    while i <= 350:
        i = n*50    
        n = n+1
        url = f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={i}'
        print(url)


    


max_url()
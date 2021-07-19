import requests
from bs4 import BeautifulSoup

# 기본 구조

url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91&limit=50'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


lables = soup.find("ul", {'class' : 'pagination-list'})
# # print(lables)

# aria = lables.get('aria-label')
# print(aria)
# print(lables.get('aria-label'))
# print(soup.select('.pagination-list'>'aria-label'))


# i=0
# while i<10:
    
#     i = i+1

#     print(i)

# print(lables)

aria = lables.find('li','aria-label')
# aria = lables.find({'aria-label':1},'a')


# if tag = a or b





# print(lables)
print(aria)

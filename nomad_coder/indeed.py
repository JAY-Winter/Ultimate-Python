#https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0 크롤링

# 페이지 기본 주소 

    # 1 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0
    # 2 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=50
    # 3 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=100
    # 4 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=150
    # 5 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=200
    # 6 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=250
    # 7 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=300
    # 8 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=350
    # n https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=(n-1)*50

import requests
from bs4 import BeautifulSoup

#url 기반으로 page_list 찾는 함수
def page_list():
    n = 1
    i = 0

#pages 전역화 함으로써 max_page() 에서 pages 변수를 이용할 수 있게한다
    global pages
    pages = []

# 임시로 900 까지 지정
    while i <= 900:
        i = (n-1)*50    
        
        url = f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={i}'
        html = requests.get(url)
        
        soup = BeautifulSoup(html.text, 'html.parser')
        current_page = soup.find("b",{'aria-label':{n}}).string
        pages.append(int(current_page))

        n = n+1
# 코드 마지막 부분

# 페이지 중 가장 큰 값을 찾는 반복문 
# 일단 i =(n-1)*50 에서 가장 큰 n 값을 찾는 것이 우선
def max_page():
    maxVal = pages[0]
    for i in range(1,len(pages)):
        if maxVal < pages[i]:
            maxVal = pages[i]

import requests
from bs4 import BeautifulSoup

# 기본 구조

    # 1 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0
    # 2 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=50
    # 3 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=100
    # 4 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=150
    # 5 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=200
    # 6 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=250
    # 7 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=300
    # 8 https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=350



def max_url():
    n = 1
    i = 0

    while i <= 350:
        i = (n-1)*50    
        
        url = f'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start={i}'
        html = requests.get(url)
        
        soup = BeautifulSoup(html.text, 'html.parser')
        current_page = soup.find("b",{'aria-label':{n}}).string

        print(current_page)
        n = n+1



max_url()

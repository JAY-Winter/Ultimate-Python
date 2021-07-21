from re import search
import requests
from bs4 import BeautifulSoup

        
url = 'https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=0'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')


# search_title = search_tag.get_text()

print(soup)
page_zone = soup.find("h2", {"class" : "jobTitle jobTitle-color-purple"}).span.string
                                        
# print(page_zone)

# page_table = soup.find('table',{"class" : "jobCard_mainContent"})


# page_span = page_table.span.string
# print(page_span)



# page_table = soup.find('table',{"class" : "jobCard_mainContent"})
# # print(page_table)
# page_title = page_table.select_one("span[title]").string
# print(page_title)
# # page_span = page_table.span.string

# # print(page_span)




# print(soup.find({'span' : '데이터누리 데이터 분석가 정규직'}, {{'class' : 'new topLeft holisticNewBlue desktop'}}))




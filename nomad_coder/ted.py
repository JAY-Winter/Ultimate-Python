import requests
from bs4 import BeautifulSoup
#어 여기까지 하루걸렸구

indeed_resul = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EA%B0%9C%EB%B0%9C%EC%9E%90&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=%EC%84%9C%EC%9A%B8&fromage=last&limit=50")
#indeed사이트에서 정보를 갖고옴

indeed_soup = BeautifulSoup(indeed_resul.text,"html.parser")
#indeed사이트에서 뷰티풀슾을 이용하여 html자료 text들을 다 끌어옴

pagination = indeed_soup.find("div",class_="pagination")
#페이지를 나타내는 pagination, 슾에서 div 자료의 pagination을 다 갖고온다.

pages = pagination.find_all('a')
current_pages = pagination.find('b')
spans = []
spans.append((int(current_pages.string)))
for page in pages: 
    spans.append(page.find("span").string) 

print(spans[:-1])


<h1> Etoos.API</h1>
def list

1) CountPage() :
    전체 페이지 갯수 카운트 하는 함수

2) CrawlingQ(Page_count) :
    CountPage 에서 return 된 Page_count 를 매개변수로 하여
    문제 Crawling 하는 함수

<h1> 진행 과정</h1>

1.  BeautifulSoup 를 사용할 것인가 - headless
    Selenium 을 사용할 것인가 - head
-> selenium 을 이용해 크롬 제어
- name -> id -> css -> xpath 순으로 제어했다

1-1. Selenuium 을 사용해야하는 이유
   일단 학생 중 특정 한 명을 고정해서 이용하는 것은 불가능함
   왜? 수시로 학생의 명단이 바뀔 수도 있는 불확실성이 있기 때문에
   고로 특정 학생을 지목하는 것을 제외 후 
   학생 list 를 펼쳤을 때 최상단에 있는 학생을 지목 후 그 학생의
   정보를 이용하는 것이 최선임을 고안함

2. class Etoos
- 중복되는 부분을 우선 def 로 나눴고
이후 더 큰 틀인 class 로 정의했다.

<h1> TO-DO </h1>

1. 문제 Crawling
- 문제 img src Tag 를 이용하여 문제 사진을 다운받아야함

<h1> Problem </h1>

* Vscode 에서 commit&pull,push 해도 커밋 카운트가 안 된다

1. 특정 학생 My 247
: 수시로 변동될 수도 있는 학생 명단 중 특정 학생 한 명을 지목 후 
문제를 뽑아내는 건 불확실성이 크다.
그럼 어떻게 고정되어있는 학생을 선별할 수 있을까?

-> 학생 list 중 최상단에 위치한 학생 지명

<h1> Etoos.API</h1>

<h3> class Etoos </h3>

<h4> def list </h4>

1) login() :
   selenium 을 이용해 url 를 open 한 뒤 로그인 후
   학생 관리페이지 open

2) selectMajor() :
   국어(언매, 화작) 또는 수학(확통~기하) 중 희망하는 과목의 시험 페이지 open
   이미 들어와있는 페이지일 경우 print 후 return Major

3) countTotalPage() :
    시험 페이지 개수가 총 몇 개인지 카운트

4) crawlingQuestion(total_page, Major, Input_day) :
    3개의 매개변수를 통해 crawling 을 희망하는 과목 선택 및
    원하는 날짜 입력 후 countTotalPage 를 통해 return 된 total_page 만큼 
    문제 crawling
    
5) countDay() :
    월 별 시행되는 데일리테스트 개수가 몇 개인지 count 후
    return day_list
    
6) selectDay() :
    희망하는 날짜 입력 후 countDay()에서 return 된 day_list
    를 통해 희망하는 날짜와 day_list 에 속해있는 날짜가 일치할 시
    해당 날짜 클릭
    

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
 
2. 학생 지정
: 수시로 변동될 수도 있는 학생 명단 중 특정 학생 한 명을 지목 후 
문제를 뽑아내는 건 불확실성이 크다.
그럼 어떻게 고정되어있는 학생을 선별할 수 있을까?

-> 학생 list 중 최상단에 위치한 학생 지명

3. class Etoos
- 중복되는 부분을 우선 def 로 나눴고
이후 더 큰 틀인 class 로 정의했다.

4. 문제 중복 Crawling 
- 특이하게 첫 번째 문제 사진이 2번 다운로드 되고 마지막 사진이 다운로드가
안된다. 어떻게 해결할 것인가? 코드 구조 문제인듯 아마?

5. 희망하는 날짜 지정 후 찾기
- 문제 Crawling 원하는 날짜를 input 한 뒤 일치하는 text 를 가진
날짜를 찾아야하는데 어떻게 할 것인가?
-> Etoos.CountDay 참고
-> webelement -> cssSelector 로 다시 convert 하는 방법을 찾아서
webelement 가 아닌 cssSelector 를 클릭하는 방법을 생각해보았다
-> 왜? Inputday 와 찾은 날짜가 동일하면 찾은 날짜의 cssSelector 를 누를거여서!
-> 희망하는 날짜 지정 완료

6. 양식에 맞지 않은 날짜 입력시 오류

희망하는 날짜를 입력하세요. ex) 07 / 01 : 08 //002
양식에 맞는 날짜를 입력해주세요.

Traceback (most recent call last):
  File "/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/main.py", line 126, in <module>
    Etoos.select_day(day_list,day_list2, Find_day_key)
  File "/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/main.py", line 79, in select_day
    return Etoos.select_day()
TypeError: select_day() missing 3 required positional arguments: 'day_list', 'day_list2', and 'Find_day_key'

오류 해결해야함

7. urlretrieve : 0번째 index 가 중복돼서 다운로드 되는 현상 발생
코드 구조가 문제인걸까?
-> 다시 적었더니 된다.. 뭐지? for 문을 수정하지도 않았다..!

8. Etoos.countDay() 
    retun 속도가 너무 느림 왜 그럴까?
-> 날짜 출력 시간이 30초 이상 걸려서 이유를 확인해본 결과 selenium 의 기본 time set 은
30초로 되어있었기 때문이다. 따라서 implicitly.wait() 를 걸어줘서 값이 출력되는 시간을 단축!

9. Etoos.crawlingQ(total_page, Major,Input_day) :
    Input_day 가 ex. 08 / 20 이라서 '/' 로 다음 경로가 만들어짐
    어떻게 하나의 하위 폴더만 만들 수 있을까?
-> makedirs 를 통해 새로운 여러 경로 및 폴더 생성 가능
-> 각 과목별 -> 날짜별 로 출력 
<h1> TO-DO </h1>

1. 양식에 맞지 않은 날짜 입력시 오류 해결
2. crawlingQ 가 끝난 후 추가로 crawling 원할 시 과목 입력 후 함수가 종료된다 왜 그런거지?
3. 국어 같은 경우 지문 사진이 따로 있는데 이걸 어떻게 다운받을 것 인가?

<h1> Problem </h1>

* Vscode 에서 commit&pull,push 해도 커밋 카운트가 안 된다


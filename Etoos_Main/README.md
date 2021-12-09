<h1> Etoos</h1>

## **1. Rule ([PEP8](http://pythonstudy.xyz/python/article/511-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%94%A9-%EC%8A%A4%ED%83%80%EC%9D%BC))**

### **a. 코드 레이아웃**

- 들여쓰기를 할 때 Tab 대신 공백(Space)을 사용한다. 특히 Python 3는 Tab과 공백을 혼용해서 사용하는 것을 허용하지 않는다. 단 VSCode에서의 Tab은 공백 4개로 대체됨
- 문법적으로 들여쓰기를 할 때는 4개의 공백을 사용한다
- 각 라인은 79자 이하로 한다. 라인이 길어서 다음 라인으로 넘어갈 때는 원래 들여쓰기 자리에서 4개 공백을 더 들여쓴다
- 함수나 클래스는 2개의 공백 라인을 추가하여 구분한다. 메서드는 한 개의 공백 라인으로 구분한다
- import는 (여러 모듈을 콤마로 연결하지 말고) 한 라인에 하나의 모듈을 import한다
    
    `No:
    import os, sys
    
    Yes:
    import os
    import sys`
    
- 컬렉션 인덱스나 함수 호출, 함수 파라미터 등에서 불필요한 공백을 넣지 않는다
    
    `No:
    spam( ham[ 1 ], { eggs: 2 } )
    bar = (0, )
    spam (1)
    
    Yes:
    spam(ham[1], {eggs: 2})
    bar = (0,)
    spam(1)`
    
- 변수 할당시 할당자 앞뒤로 하나의 공백만 넣는다
    
    `No: i=i+1
    
    Yes: i = i + 1`
    

### **b. 명명 규칙**

- 함수, 변수, Attribute는 소문자로 단어 간은 밑줄(_)을 사용하여 연결한다   `예: total_numbers`
- 클래스는 단어 첫 문자마다 대문자를 써서 연결하는 CapWords 포맷으로 명명한다   `예: CoreClass`
- 모듈명은 짧게 소문자로 사용하며 밑줄을 쓸 수 있다. 패키지명 역시 짧게 소문자를 사용하지만 밑줄은 사용하지 않는다   `예: serial_reader`
- 모듈 상수는 모두 대문자를 사용하고 단어마다 밑줄로 연결하는 ALL_CAPS 포맷으로 명명한다   `예: MAX_COUNT = 100`
- 클래스의 public attribute는 밑줄로 시작하지 말아야 한다   `예: name`
- 클래스의 protected instance attribute는 하나의 밑줄로 시작한다   `예: _initialized`
- 클래스의 private instance attribute는 2개의 밑줄로 시작한다   `예: __private_var`
- 인스턴스 메서드는 (객체 자신을 가리키기 위해) self 를 사용한다   `예: def copy(self, other):`
- 클래스 메서드는 (클래스 자신을 가리키기 위해) cls 를 사용한다   `예: def clone(cls, other):`

### **c. 문장과 표현식**

- if, for, while 블럭 문장을 한 라인으로 작성하지 말 것여러 라인에 걸쳐 사용하는 것이 더 명료함
    
    `No:
    if a < 0: a = 0
    
    Yes:
    if a < 0:
        a = 0`
    
- a는 b가 아니다를 표현할 때 a is not b 를 사용한다not a is b 를 사용하지 말 것
    
    `No: if not a is b
    
    Yes: if a is not b`
    
- 값이 비어있는지 아닌지를 검사하기 위해 길이를 체크하는 방식을 사용하지 말 것대신 if mylist 와 같이 표현함
    
    `No: if len(mylist) == 0
    Yes: if not mylist
    
    No: if len(mylist) > 0
    Yes: if mylist`
    
- import 문은 항상 파일의 상단에 위치하며, 표준 라이브러리 모듈, 3rd Party 모듈, 그리고 자신의 모듈 순으로 import 한다
    
    `import os
    import numpy
    import mypkg`
    
- 모듈 import시 절대 경로를 사용할 것을 권장한다예를 들어, sibling 모듈이 현재 모듈과 같은 폴더에 있더라도 패키지명부터 절대 경로를 사용함단, 복잡한 패키지 경로를 갖는 경우 상대경로(.)를 사용할 수 있다
    
    `No:
    import sibling
    
    Yes:
    import mypkg.sibling
    from mypkg import sibling
    from . import sibling # 상대경로
    from .sibling import example`



<h1> 작동 구조 </h1>
<img src="/Users/heyon/Desktop/JAY/Jay-Thomas-code/KEYNOTE/selenium과 함께라면 - 2/2번/2번.002.jpeg" alt="">

<h3> class Etoos </h3>

<h4> def list </h4>

1) login() :

   selenium 을 이용해 url 를 open 한 뒤 로그인 후
   학생 관리페이지 open
   global driver 선언

2) selectMajor(subject) :

   subject 를 매개변수로 하여 subeject 가 for 반복문에
   따라 1씩 증가할 수록 과목이 국어 -> 수학 순으로 재정의 되며
   과목이 새로 정의될 때 마다 각 과목별 xpath 를 찾아 클릭 후 
   subject 를 return
   
3) countDay() :

    days 는 key : day_key, value : day_values 로
    이루어져있으며 key 는 text값, values 는 xpath값을 나타냄

    월 별 시행되는 데일리테스트 개수가 몇 개인지 count 후
    day_list 를 return 

4) selectDay(day_list, Input_day) :

    희망하는 날짜 입력 후 countDay()에서 return 된 day_list
    를 통해 희망하는 날짜와 day_list 에 속해있는 날짜가 일치할 시
    해당 날짜 클릭


5) countTotalPage() :

    시험 페이지 개수가 총 몇 개인지 카운트

6) crawlingQuestion(total_page, Major, var_Input_day) :

    3개의 매개변수를 통해 crawling 을 희망하는 과목 선택 및
    원하는 날짜 입력 후 countTotalPage 를 통해 return 된 total_page 만큼 
    문제 crawling
    국어(언매 or 화작) 그리고 수학(확통1 or ... or 기하2)으로 묶어서 작동

6-1) downloadAndeditImg(question_link, file_path, subject) :

    1) urlretrieve(question_link, file_path) 를 통해 question_link 의 파일을 file_path 값으로 다운로드 
    2) cropImage(file_path) 를 통해 다운로드 받은 문제 외곽의 여백부분 제거
    3) resizeImage(file_path) 를 통해 다운로드 받은 문제 크기 조정


7) addSelectsubject() :

    새로운 alert 가 뜨면 switch 한 후 accept alert 이후
    다음 과목 선택

8) removeDuplicatedQuestion(edit_var_Input_day) :

    edit_var_Input_day 를 매개변수로 해서 지정된 path 에 맞은
    문제를 찾고 문제 중 중복된 문제를 제거

9) closeDriver() :

    코드 작동 완료시 작동


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

10. Etoos.removeDuplicatedQuestion(edit_var_Input_day) 생성
    위 함수를 통해 중복 문제 제거





<h1> Problem </h1>

* Vscode 에서 commit&pull,push 해도 커밋 카운트가 안 된다.. 내일 해결하기

1. 특정 학생 My 247
: 수시로 변동될 수도 있는 학생 명단 중 특정 학생 한 명을 지목 후 
문제를 뽑아내는 건 불확실성이 크다.
그럼 어떻게 고정되어있는 학생을 선별할 수 있을까?

https://ilsandonggu247.etoos.com/lms/schedule/my_schedule.do?student_cd=297306&branch_cd=2013&group_year=2021&group_cd=3&std_mem_no=6215503&page_gb=
https://ilsandonggu247.etoos.com/lms/schedule/my_schedule.do?student_cd=304881&branch_cd=2013&group_year=2021&group_cd=3&std_mem_no=6825376&page_gb=



학생 일일플래너 뷰 : https://ilsandonggu247.etoos.com/lms/schedule/my_schedule.do?student_cd=310136&branch_cd=2013&group_year=2021&group_cd=6&std_mem_no=7601329&page_gb=

데일리테스트 국어 메인 뷰 : https://ilsandonggu247.etoos.com/lms/exam/daily_test_main_view.do?student_cd=297306&branch_cd=2013&group_year=2021&group_cd=3&page_gb=&subjt_cd=C220100
데일리테스트 수학 메인 뷰 : https://ilsandonggu247.etoos.com/lms/exam/daily_test_main_view.do?student_cd=297306&branch_cd=2013&group_year=2021&group_cd=3&page_gb=&subjt_cd=C220150

<h2> 접근방식  </h2>
1.  BeautifulSoup 를 사용할 것인가 - headless
    Selenium 을 사용할 것인가 - head

2. Selenuium 을 사용해야하는 이유
   일단 학생 중 특정 한 명을 고정해서 이용하는 것은 불가능함
   왜? 수시로 학생의 명단이 바뀔 수도 있는 불확실성이 있기 때문에
   고로 특정 학생을 지목하는 것을 제외 후 
   학생 list 를 펼쳤을 때 최상단에 있는 학생을 지목 후 그 학생의
   정보를 이용하는 것이 최선임을 고안함

3. 




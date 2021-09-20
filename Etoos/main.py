from Dailytest import Etoos


Etoos.login()
        
print("""
<선택 과목>

- 언어와 매체 : 언매
- 화법과 작문 : 화작

- 데일리하이퍼 확통 : 확통1
- 데일리하이퍼 미적분 : 미적분1
- 데일리하이퍼 기하 : 기하1

- 2등급거저먹기 확통 : 확통2
- 2등급거저먹기 미적분 : 미적분2
- 2등급거저먹기 기하 : 기하2
""")

len_subject = 8

input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")


for subject in range(len_subject) :

    subject = Etoos.selectSubject(subject)
    
    day_list = Etoos.countDay()

    var_input_day = Etoos.selectDay(day_list, input_day)

    total_page = Etoos.countTotalPage()

    Etoos.crawlingQuestion(total_page, subject, input_day)

    Etoos.addSelectsubject()


edit_var_input_day = var_input_day.replace("/","")

Etoos.removeDuplicatedQuestion(edit_var_input_day)


Etoos.closeDriver()


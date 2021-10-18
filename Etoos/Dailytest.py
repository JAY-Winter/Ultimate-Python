import os.path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, NoSuchWindowException, StaleElementReferenceException
from urllib.request import urlretrieve
import time
from dotenv import load_dotenv
from editImg import cropImage, resizeImage





class Etoos:
# ETOOS 데일리테스트 문제 crawling 하기 위해 작성된 코드입니다.
    def __init__() :
        print("class Etoos operate")





    def acceptAlert() :
        
        alert = driver.switch_to.alert
        time.sleep(0.25)
        alert.accept()





    def login() : 
        # 로그인 후 과목 선택 전까지 작동 코드
        try : 
            URL = "https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do"
            
            load_dotenv()
            ID = os.environ.get("ID")
            PW = os.environ.get("PW")

            global driver
            driver = webdriver.Chrome("chromedriver")
            driver.get(URL)

            # 첫 번째로 띄워진 window
            global window_before
            window_before = driver.window_handles[0]

            print("로그인 중 입니다...")
            # ID 작성
            driver.find_element_by_id("mem_id")
            ActionChains(driver).send_keys(ID).perform()

            # PW 작성
            driver.find_element_by_name("pwdtmp").click()
            ActionChains(driver).send_keys(PW).perform()

            # Login 클릭
            driver.find_element_by_class_name("btn_login").click()
            driver.implicitly_wait(10)

            # 첫 번째 메뉴 클릭
            driver.find_element_by_css_selector("#lnbmenu > ul > li:nth-child(1) > a").click()
            driver.implicitly_wait(10)

            # 첫 번째 메뉴 - 전체 학생 관리
            driver.find_element_by_id("m_PB200922").click()
            driver.implicitly_wait(50)

            # 첫 번째 학생 관리 페이지 클릭
            driver.find_element_by_css_selector("#content > div.wrap_tbl_sdw.mgt_20 > table > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()

            # 두 번째로 띄워진 window 으로 driver 가 넘어감
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            return

        except NoSuchWindowException :
            print("실행 중 창이 닫혔습니다.")

        except : 
            print("회원 아이디 또는 비밀번호가 일치하지 않습니다.")
            driver.close()
            return Etoos.login()





    def selectSubject(subject) : 

        try : 
            # 국어 선택과목
            if subject == 0 : 
                subject = "언매"
                try :
                # 국어 과목 클릭
                    driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
                    time.sleep(0.25)                
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[1]").click()
                    
                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:
                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 1 : 
                subject = "화작"

                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[2]").click()
                    
                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:
                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            # 수학 선택과목
            elif subject == 2 : 
                subject = "확통1"              

                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[1]").click()

                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:

                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 3 : 
                subject = "미적분1"

                try : 
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[2]").click()

                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:

                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 4 : 
                subject = "기하1"

                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[3]").click()

                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:

                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 5 :
                subject = "확통2"

                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[4]").click()

                    Etoos.acceptAlert()

                    return subject 

                except NoAlertPresentException as e:
                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 6 :
                subject = "미적분2" 
                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[5]").click()

                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:
                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

            elif subject == 7 : 
                subject = "기하2"

                try :
                    driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                    time.sleep(0.25)
                    driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[6]").click()

                    Etoos.acceptAlert()

                    return subject

                except NoAlertPresentException as e:
                    print("이미 들어와 있는 페이지입니다.", e)
                    return subject

        except NoAlertPresentException as e : 
            print("일시적 오류입니다.",e)
            pass





    def countDay() :
    # countDay return 하는 시간이 30초 이상 걸렸던 이유는 drvier.timeout = 30sec 로 초기 설정되어있었기 때문
    # 따라서 driver.implicitly_wait() 로 수정했다.
        day_list = []

        for week in range(1,6) :

            for day in range(1, 6) :

                driver.implicitly_wait(0.1)

                try : 
                    day_key = driver.find_element_by_xpath(f"/html/body/div[2]/div[6]/div[2]/div/div[3]/div[2]/table/tbody/tr[{week}]/td[{day}]/div/strong").text
                    day_values = driver.find_element_by_xpath(f"/html/body/div[2]/div[6]/div[2]/div/div[3]/div[2]/table/tbody/tr[{week}]/td[{day}]/div/strong")
                    
                    days = {day_key : day_values}
                    
                    day_list.append(days)

                    day_list_last_key = list(day_list[-1].keys())

                except NoSuchElementException:
                    pass
        
        for i in range(len(day_list)) :

            if "31" in day_list_last_key[0] : 
                print("31일까지 입니다.") 
                return day_list

            elif "31" not in day_list_last_key[0] and "30" in day_list_last_key[0] :
                print("30일까지 입니다.")
                return day_list

            elif "30" not in day_list_last_key[0] and "29" in day_list_last_key[0] :
                print("29일까지 입니다.")
                return day_list

            elif "29" not in day_list_last_key[0] and "28" in day_list_last_key[0] :
                print("28일까지 입니다.")
                return day_list





    def selectDay(day_list, input_day) : 

        # try :
            var_input_day = input_day
            # input_day 를 새로 var_input_day 로 선언하는 이유는
            # input_day 의 고유 값이 변하면 안 되기 때문이다.
            # 아래와 같이 var_input_day 값에 변화를 줌
            
            list_input_day = f"['{var_input_day}']"

            keys_list = []
            values_list = []

            for i in range(len(day_list)) :

                # try :

                keys_list.append(str(list(day_list[i].keys())))
                # keys() 를 통해 dict type 으로 반환된 day_list[i] 값을 list type 으로 변환 후 
                # str type 으로 최종 변환을 통해 keys_list 에 append

                if list_input_day == keys_list[i] :
                    # list_input_day 는 var_input_day 를 list index 처럼 보이게 선언된 변수
                    # day_list 개수 만큼의 반복문을 통해 key_list[i] 와 input_day(내가 입력한 day) 같을 시 

                    values_list = list(day_list[i].values())
                    values_list[0].click()
                    # dict Index로 이루어진 day_list Index 중 values 값을 list type 으로 변환한 값이 values_list 
                    # list type 으로 변환된 values_list[0] 의 첫 번째 Index 를 클릭
                    Etoos.acceptAlert()
                    # 새로운 알람창이 뜨며 클릭

                    return var_input_day

                elif len(var_input_day) != 7 :

                    print("양식에 맞는 날짜를 입력해주세요.")
                    return Etoos.selectDay(day_list, input_day)

                # except :

                #     print("기타 오류 발생")
                #     return Etoos.selectDay(day_list, input_day)

        # except :
        #     print("기타 오류입니다.!")
        #     return Etoos.selectDay(day_list, input_day)





    def countTotalPage() :

        driver.implicitly_wait(2)
        total_page_tag = driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > span").text
        # css_selector 를 통해 찾은 값을 text화 : 1 / 6 이런 식으로 나옴
        position_slash = total_page_tag.rfind("/")
        # '/' 이 우측 기준으로 몇 번째 칸에 있는지 확인
        print("total_page_tag : ", (total_page_tag))

        total_page = int(total_page_tag[-position_slash:])
        #total_page_tag 값을 역으로 '/' 값이 우측에서 몇 번째 칸에 있는지 확인한 후 그 만큼의 값을 int type 으로 변환

        return total_page





    def crawlingQuestion(total_page, subject, var_input_day) :

        edit_var_input_day = var_input_day.replace(" / ","_")
        kor_folder_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/국어/{edit_var_input_day}"
        math_folder_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/{edit_var_input_day}"
        filetype = "PNG"

        def downloadAndeditImg(question_link, file_path, subject) :
            
            urlretrieve(question_link, file_path)            
            
            time.sleep(0.5)

            cropImage(file_path)
            time.sleep(0.5)

            resizeImage(file_path)
            time.sleep(0.5)
            
            return print(f"{subject} 문제{page}번 다운로드 완료")

        if subject == "언매" or subject == "화작" :

            if not os.path.isdir(kor_folder_path) :
            
                print("폴더를 생성합니다.")            
                os.makedirs(kor_folder_path)
                time.sleep(0.5)

            for page in range(1, total_page+1) :

                question_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
                file_path = f"{kor_folder_path}/{subject}_문제{page}번.{filetype}"
                
                downloadAndeditImg(question_link, file_path, subject)

                driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()            
                time.sleep(1.0)
                # 다음 페이지로 넘어가기 전 1.0 s 시간을 줘 동잂 파일이 2번 다운로드 되지 않게 함
            return edit_var_input_day
            
        elif subject == "확통1" or subject == "미적분1" or subject == "기하1" or subject == "확통2" or subject == "미적분2" or subject == "기하2" :
            
            if not os.path.isdir(math_folder_path) :
            
                print("폴더를 생성합니다.")            
                os.makedirs(math_folder_path)
                time.sleep(0.5)

            for page in range(1, total_page+1) :

                question_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
                file_path = f"{math_folder_path}/{subject}_문제{page}번.{filetype}"

                downloadAndeditImg(question_link, file_path, subject)

                driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()            
                time.sleep(1.0)

            return edit_var_input_day






    def addSelectSubject() :

        alert = driver.switch_to.alert
        alert.accept()

        print("다음 과목으로 넘어갑니다.")
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/a").click()

        return 





    def closeDriver() :

        driver.close()
        driver.switch_to_window(window_before)
        driver.close()

        return print("""
프로그램을 종료합니다.
문의 : ETOOS247 일산동구점 정재현
        """)





    def removeDuplicatedQuestion(edit_var_input_day) :

        kor_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/국어/{edit_var_input_day}"
        math_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/{edit_var_input_day}"
        # 과목 별 path 지정

        kor_file_list = os.listdir(kor_path)
        math_file_list = os.listdir(math_path)
        # 지정 된 path 에 위치한 파일들을 list 로 모아서 저장

        kor_file_list.sort()
        math_file_list.sort()
        # list 로 저장된 파일들을 이름 순으로 정렬
        # 왜? os.listdir 시 어떤 순으로 정렬되는진 모르겠지만 무규칙적으로 정렬

        kor_file_size_list = []
        math_file_size_list = []
        # filesize 를 담을 배열 생성

        for list in range(len(kor_file_list)) :

            kor_file_size = os.path.getsize(f"{kor_path}/{kor_file_list[list]}")
            # 국어/선택한 날짜 폴더 내 파일 사이즈 확인
            #kor_file_list[list] : 언매 1번 문제 ...

            kor_file_size_list.append(kor_file_size)
            # size_list 에 file_size 추가

        for list in range( len(math_file_list) ) :

            math_file_size = os.path.getsize(f"{math_path}/{math_file_list[list]}")
        
            math_file_size_list.append(math_file_size)

        start = 1
        # start = 1 and start +=1 로 지정한 이유 : 비교 대상은 비교할 대상보다 1만큼 더 커야하므로

        for i in range(len(kor_file_size_list)-1 ) :
            
            for j in range(start, len(kor_file_size_list) ) :

                if kor_file_size_list[i] == kor_file_size_list[j] :
                    print(kor_file_list[j])

                    try :
                        os.remove(f"{kor_path}/{kor_file_list[j]}")
                        
                    except :
                        pass
                    # 에외처리를 한 이유 : 반복문 구성 중 이미 삭제된 파일을 다시 삭제하려는 현상이 나타나 예외처리함

            start += 1

        start = 1
        # 국어에서 마무리 된 start 는 초기 값 1보다 크므로 재선언

        for i in range(len(math_file_size_list)-1 ) :
            
            for j in range(start, len(math_file_size_list) ) :
                
                if math_file_size_list[i] == math_file_size_list[j] :
                    print(math_file_list[j])

                    try : 
                        os.remove(f"{math_path}/{math_file_list[j]}")

                    except : 
                        pass

            start += 1

        return print("중복 파일 제거 완료")



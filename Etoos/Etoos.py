import os.path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, NoSuchWindowException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.request import urlretrieve
import time
from dotenv import load_dotenv
from editImg import cropImage, resizeImage
class Etoos:
# ETOOS 데일리테스트 문제 crawling 하기 위해 작성된 코드입니다.
    def __init__() :
        print("class Etoos operate")




    def login() : 
        # 로그인 후 과목 선택 전까지 작동 코드
        try : 
            URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'
            
            load_dotenv()
            ID = os.environ.get("ID")
            PW = os.environ.get("PW")

            global driver
            driver = webdriver.Chrome('chromedriver')
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





    def selectMajor() : 

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

        try :

            Major = input("출력이 필요한 과목을 입력하세요 : ")
            # 국어 선택과목
            if Major == '언매' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[1]")))
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[1]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '화작' :
                driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[2]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major            

            # 수학 선택과목
            elif Major == '확통1' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[1]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '미적분1' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[2]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '기하1' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[3]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '확통2' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[4]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '미적분2' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[5]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            elif Major == '기하2' : 
                driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[2]/select/option[6]").click()
                alert = driver.switch_to.alert
                time.sleep(0.5)
                alert.accept()
                return Major

            else :
                print("올바른 과목을 입력해주세요.")
                return Etoos.selectMajor()

        except NoAlertPresentException as e :
            print("이미 들어와 있는 페이지입니다.", e)
            return Major





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
                    print("달력에 표시되지 않은 날입니다.")
                    pass
        
        for i in range(len(day_list)) :

            if '31' in day_list_last_key[0] : 
                print("31일까지 입니다.") 
                return day_list

            elif '31' not in day_list_last_key[0] and '30' in day_list_last_key[0] :
                print("30일까지 입니다.")
                return day_list

            elif '30' not in day_list_last_key[0] and '29' in day_list_last_key[0] :
                print("29일까지 입니다.")
                return day_list

            elif '29' not in day_list_last_key[0] and '28' in day_list_last_key[0] :
                print("28일까지 입니다.")
                return day_list





    def selectDay(day_list) : 

        try :
            Input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")

            list_Input_day = f"['{Input_day}']"

            keys_to_list = []
            values_to_list = []

            for i in range(len(day_list)) :

                try :

                    keys_to_list.append(str(list(day_list[i].keys())))

                    if list_Input_day == keys_to_list[i] :

                        values_to_list = list(day_list[i].values())
                        values_to_list[0].click()

                        alert = driver.switch_to.alert
                        time.sleep(0.5)
                        alert.accept()

                        return Input_day

                    elif len(Input_day) != 7 :

                        print("양식에 맞는 날짜를 입력해주세요.")
                        return Etoos.selectDay(day_list)

                except :

                    print("기타 오류 발생")
                    return Etoos.selectDay(day_list)

        except :
            print("기타 오류입니다.!")
            return Etoos.selectDay(day_list)




    def countTotalPage() :

        driver.implicitly_wait(2)
        tatal_page_tag = driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > span").text
        position_slash = tatal_page_tag.rfind('/')
        str(tatal_page_tag)

        total_page = int(tatal_page_tag[-position_slash:])

        return total_page





    def reading(total_page, Major,Input_day) :

        edit_Input_day = Input_day.replace("/","")
        folder_path = f'./국어/{edit_Input_day}'
        filetype = "PNG"

        if not os.path.isdir(folder_path) :

            os.makedirs(folder_path)
            time.sleep(1.0)

        for i in range(1, total_page+1) :

            Question_PNG_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
            File_Path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/{folder_path}/{Major} 문제{i}번.{filetype}"
            # Question_PNG_link 뜨는거 기다려야할듯 중복 다운로드됨
            urlretrieve(Question_PNG_link, File_Path)            
            print(f"{Major} 문제{i}번 다운로드 완료")
            time.sleep(0.5)

            cropImage(File_Path)
            time.sleep(0.5)

            resizeImage(File_Path)
            time.sleep(0.5)

            driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()            
            time.sleep(1.0)

        alert = driver.switch_to.alert
        alert.accept()

        return





    def math(total_page, Major,Input_day) :
    
        edit_Input_day = Input_day.replace("/","")
        folder_path = f'./수학/{edit_Input_day}'
        filetype = "PNG"

        if not os.path.isdir(folder_path) :

            os.makedirs(folder_path)
            time.sleep(1.0)

        for i in range(1, total_page+1) :

            Question_PNG_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
            File_Path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/{folder_path}/{Major} 문제{i}번.{filetype}"

            urlretrieve(Question_PNG_link, File_Path)
            print(f"문제{i}번 다운로드 완료")

            cropImage(File_Path)
            time.sleep(0.5)

            resizeImage(File_Path)
            time.sleep(0.5)

            driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()            
            time.sleep(1.0)
            # 다음 페이지로 넘어가기 전 1.0 s 시간을 줘 동잂 파일이 2먼 다운로드 되지 않게 함
        alert = driver.switch_to.alert
        alert.accept()

        return





    def addSelectMajor() :

        isAdded = input("출력이 더 필요한 과목이 있습니까?(예 또는 아니오) : ")

        if isAdded == "예" :
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/a").click()
            pass

        elif isAdded == "아니오" :

            print("""
프로그램을 종료합니다.
문의 : ETOOS247 일산동구점 정재현
            """)
            driver.close()
            driver.switch_to_window(window_before)
            driver.close()
            
            return False

        else :
            print("올바른 선택지를 입력해주세요.")
            return Etoos.addSelectMajor()





    def crawlingQuestion(total_page, Major,Input_day) :
        
        if Major == '언매' : 

            Etoos.reading(total_page, Major,Input_day)
            # 여기서 selectDay 가 다시 이루어지고
            # 크롤링이 다시 이뤄져야함

        elif Major == '화작' : 
            Etoos.reading(total_page, Major,Input_day)

        elif Major == '확통1' : 

            Etoos.math(total_page, Major,Input_day)

        elif Major == '미적분1' : 

            Etoos.math(total_page, Major,Input_day)                

        elif Major == '기하1' : 

            Etoos.math(total_page, Major,Input_day)

        elif Major == '확통2' : 

            Etoos.math(total_page, Major,Input_day)

        elif Major == '미적분2' : 

            Etoos.math(total_page, Major,Input_day)

        elif Major == '기하2' : 

            Etoos.math(total_page, Major,Input_day)

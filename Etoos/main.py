from os import major
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from urllib.request import urlretrieve
import time
from selenium.common.exceptions import NoSuchElementException

class Etoos() :
# ETOOS 데일리테스트 문제 crawling 하기 위해 작성된 코드입니다.

    def login() : 
        # 로그인 후 과목 선택 전까지 작동 코드
        try : 
            URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'
            ID = input("아이디를 입력하세요 : ")
            PW = input("비밀번호를 입력하세요 : ")

            global driver
            driver = webdriver.Chrome('chromedriver')
            driver.get(URL)

            # 첫 번째로 띄워진 window
            window_before = driver.window_handles[0]

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
            
        except : 
            print("회원 아이디 또는 비밀번호가 일치하지 않습니다.")
            driver.close()
            return Etoos.login()



    def selectMajor() : 
    # 데일리테스트 - 국어 
        global Major
        Major = input("출력이 필요한 과목을 입력하세요. ex) 국어, 수학 : ")
        
        if Major == '국어' : 
            driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
            print("Loading ...")
            

        elif Major == '수학' : 
            driver.find_element_by_css_selector("#menuList > ul > li.subject2 > a").click()
            print("Loading ...")
            

        else :
            print("올바른 과목을 입력해주세요 : ")
            return Etoos.selectMajor()

    def countTotalPage() :

        tatal_page_tag = driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > span").text
        position_slash = tatal_page_tag.rfind('/')
        str(tatal_page_tag)

        total_page = int(tatal_page_tag[-position_slash:])

        return total_page

    def crawlingQ(total_page, Major,Input_day) :
        
        edit_Input_day = Input_day.replace("/","")

        Reading_folder = './국어/{}'.format(edit_Input_day)
        Math_folder = './수학/{}'.format(edit_Input_day)
        filetype = "PNG"

        if Major == '국어' : 

            if not os.path.isdir(Reading_folder) :

                os.makedirs(Reading_folder)
                time.sleep(2.0)

            for i in range(1, total_page+1) :

                Question_PNG_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
                Text_PNG_link = driver.find_element_by_css_selector(f"#text_img_nm{i}").get_attribute("src")

                try :

                    urlretrieve(Question_PNG_link, f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/{Reading_folder}/문제{i}번.{filetype}")
                    urlretrieve(Text_PNG_link, f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/{Reading_folder}/지문{i}번.{filetype}")
                    time.sleep(1.0)
                    driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()

                except NoSuchElementException:  
                    pass
                    
                
            alert = driver.switch_to.alert
            alert.accept()

        else :

            if not os.path.isdir(Math_folder) :
                
                os.makedirs(Math_folder)
                time.sleep(2.0)
                
            for i in range(1, total_page+1) :

                Question_PNG_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")

                urlretrieve(Question_PNG_link, f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/{Math_folder}/문제{i}번.{filetype}")
                time.sleep(1.0)
                driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()

            alert = driver.switch_to.alert
            alert.accept()

    def countDay() :

        day_list = []
        day_selector_list = []

        for week in range(6) : 

            days = driver.find_elements_by_css_selector("#math_day > td:nth-child({}) > div > strong".format(week+1))

            for day in range(5) :                     

                try : 

                    Find_day = days[day].text
                    Find_day_key = days[day]

                    day_list.append(Find_day)
                    day_selector_list.append(Find_day_key)            

                except (IndexError, NoSuchElementException):
                    print("에러에러에러에러")
                    pass

                finally :
                    
                    print(day_list)

                    if week == 5 and day ==4 :

                        return print("끝")
                        # return day_list, day_selector_list
        

    def selectDay(day_list, day_selector_list) : 
        
        global Input_day
        Input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")
        
        for i in range(len(day_list)) : 

            if Input_day == day_list[i] : 
                
                day_selector_list[i].click()
                
                alert = driver.switch_to.alert
                alert.accept()

            elif len(Input_day) != 7 :

                print("양식에 맞는 날짜를 입력해주세요.")
                return Etoos.selectDay()

Etoos.login()

Etoos.selectMajor()

day_list,day_selector_list = Etoos.countDay()
Etoos.selectDay(day_list,day_selector_list)

total_page = Etoos.countTotalPage() 

# Etoos.crawlingQ(total_page, Major, Input_day)

print("정상 작동")
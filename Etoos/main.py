from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from urllib.request import urlretrieve
import time

class Etoos() :

    def CountPage() :

        page_tag = driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > span").text
        position_slash = page_tag.rfind('/')
        str(page_tag)

        page_count = int(page_tag[-position_slash:])

        return page_count

    def CrawlingQ(Page_count) :

        PNG_folder = './Reading_PNG'
        filetype = "PNG"

        if not os.path.isdir(PNG_folder) :
            os.mkdir(PNG_folder)

        for i in range(Page_count) :
            
            PNG_link = driver.find_element_by_css_selector("#wr_question > div.cont > img").get_attribute("src")
            time.sleep(3)
            urlretrieve(PNG_link, "/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/Reading_PNG/{}.{}".format(i+1,filetype))
            time.sleep(0.5)

            driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()
            
        alert = driver.switch_to.alert
        alert.accept()

        return print("출력 완료")
        
    def CountDay() :

        day_list = []
        day_list2 = []
        for week in range(6) : 

            days = driver.find_elements_by_css_selector("#math_day > td:nth-child({}) > div > strong".format(week+1))

            for day in range(5) :                     
                try : 

                    Find_day = days[day].text
                    Find_day_key = days[day]
                    day_list.append(Find_day)
                    day_list2.append(Find_day_key)
                except : 
                    pass

        return day_list, day_list2, Find_day_key

    def select_day(day_list, day_list2, Find_day_key) : 
        
        print("Loading ...")
        Input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")
        

        for i in range(len(day_list)) : 

            if Input_day == day_list[i] : 
                
                day_list2[i].click()
                
                alert = driver.switch_to.alert
                alert.accept()

            elif len(Input_day) != 7 :

                print("양식에 맞는 날짜를 입력해주세요.")
                return Etoos.select_day()

    def login() : 

        URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'
        ID = "ilsan247"
        PW = "isd151208^^"

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

# 데일리테스트 - 국어 
driver.find_element_by_css_selector("#menuList > ul > li.subject1 > a").click()
driver.implicitly_wait(50)

day_list,day_list2, Find_day_key = Etoos.CountDay()

Etoos.login()

Etoos.select_day(day_list,day_list2, Find_day_key)

Page_count = Etoos.CountPage() 

Etoos.CrawlingQ(Page_count)

print("테스트 정상작동")
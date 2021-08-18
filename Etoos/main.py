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
            urlretrieve(PNG_link, "{}.{}".format(i+1,filetype))
            time.sleep(0.5)

            driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()
            
            # if os.path.isfile("{}.{}".format(i+1,filetype)) :
                # return print("파일이 있습니다.")

    def CountDay() :

        Input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")

        day_list = []
            
        for week in range(6) : 
            
            days = driver.find_elements_by_css_selector("#math_day > td:nth-child({}) > div > strong".format(week+1))

            for day in range(5) : 
                try : 
                    
                        # day_list.append(days[day].text)

                    Find_day = days[day].text
                    Find_day_key = days[day]
                    # print(Find_day)
                    # print(Find_day)
                    if Input_day == Find_day : 
                        # days[day].click()
                        print(By.cssSelector(days[day]))
                        # Find_day_key.click()
                        return 

                    # else : 
                        # print("날짜를 잘 못 입력했습니다.")
                        # break
                except : 
                    pass

                # finally : 
                    # return 

URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'

driver = webdriver.Chrome('chromedriver')

ID = "ilsan247"
PW = "PW"

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

Etoos.CountDay()

# 예시로 8/9 일자 클릭

# driver.implicitly_wait(50)
# driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[3]/div[2]/table/tbody/tr[3]/td[2]").click()
# # 시험응시 알람버튼이 생성 시 alert 로 넘어간 뒤 accept
# alert = driver.switch_to.alert
# alert.accept()

# 전체 페이지 갯수 찾은 후 사진 crawling 하는 def 

# Page_count = Etoos.CountPage() 

# Etoos.CrawlingQ(Page_count)

print("Operate")
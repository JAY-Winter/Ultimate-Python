
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from urllib.request import urlretrieve

# class Login():

URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'

driver = webdriver.Chrome('chromedriver')

ID = "ilsan247"
PW = "="

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

# 예시로 8/9 일자 클릭
driver.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[1]").click()
driver.implicitly_wait(50)

# 시험응시 알람버튼이 생성 시 alert 로 넘어간 뒤 accept
alert = driver.switch_to.alert
alert.accept()

# 전체 페이지 갯수 찾은 후 사진 crawling 하는 def 

def CountPage_and_CrawlingPic() :

    # 아래 있는 정리 후 넣을거임





# 전체 페이지 찾는 코드
# a : css_selector 로 찾음
a = driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > span")

# b : parsing 한 text 를 str 화 함. 왜? '/' 가 포함되어있어서 float 취급받음
b = str(a.text)

# c : a 에서 뽑은 text 를 우측 기준으로 '/' 가 몇 번째에 있는 지 찾음
c = a.text.rfind('/')

# d : parsing -> str 후 끝에서 2번째 까지 뽑아낸 뒤 int 화. 왜? 전체 페이지 갯수 를 구하는 것이기 때문에
d = int(b[-2:])

# 폴더 생성
PNG_folder = './Reading_PNG'

if not os.path.isdir(PNG_folder) :
    os.mkdir(PNG_folder)

# 데일리테스트 문제 사진 크롤링
PNG = driver.find_element_by_css_selector("#wr_question > div.cont")

link = "https://eci.etoos.gscdn.com/247/MT/K002/8/9/K002Q116001.png"

start = link.rfind('.')
end = link.rfind('g')


filetype = link[start:end+1]

urlretrieve(link, "1{}".format(filetype))



print("Operate")

# 첫 번째 문제 후 두 번째 문제로 넘어가는 코드
# driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()
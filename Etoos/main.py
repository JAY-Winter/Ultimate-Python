# from selenium import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# class Login():

URL = 'https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do'

driver = webdriver.Chrome('chromedriver')

ID = "ilsan247"
PW = "isd151208^^"

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

print("Operate")

# 첫 번째 문제 후 두 번째 문제로 넘어가는 코드
driver.find_element_by_css_selector("#DailyTestCommentaryForm > div > div > div.wrap_test_answer > div.wrap_test > div.paging_etc.clear > div > a.bt_next").click()
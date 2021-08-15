# from selenium import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://www.etoos.com/member/login.asp'

driver = webdriver.Chrome('chromedriver')

ID = "ilsan247"
# PW = "isd151208^^"

driver.get(URL)

# try:
# id_box = driver.find_element_by_name("mem_id")
id_box = driver.find_element_by_name("mem_id")
print("정상 작동")
id_box.send_keys("123", Keys.ENTER)
# id_box.send_keys(ID)

# id.send_keys("ilsan247")

driver.implicitly_wait(2)
driver.close()
    
# except :
#     # print("오류 발생")
#     driver.close()






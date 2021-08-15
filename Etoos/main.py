# from selenium import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://www.etoos.com/member/login.asp'

driver = webdriver.Chrome('chromedriver')

ID = "ilsan247"
PW = "isd151208^^"

driver.get(URL)

# try:


# id_box = driver.find_element_by_name("mem_id")



# driver.find_element_by_name("mem_id").click()
# ActionChains(driver).send_keys(ID).perform()

driver.find_element_by_name("pwdtmp").click()
ActionChains(driver).send_keys(PW).perform()

print("정상 작동")

driver.implicitly_wait(2)
# driver.close()
    
# except :
#     # print("오류 발생")
#     driver.close()






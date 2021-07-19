from selenium import webdriver
# from bs4 import BeautifulSoup
# from requests import get

driver = webdriver.Chrome(executable_path='/Users/heyon/Desktop/chromedriver_mac64')

driver.implicitly_wait(2)
driver.get("https://www.etoos.com/member/login.asp?returnUrl=http://247.etoos.com/lms/index.do")


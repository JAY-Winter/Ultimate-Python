from selenium import webdriver
# from bs4 import BeautifulSoup
# from requests import get

driver = webdriver.Chrome('/usr/local/bin/chromedriver/')
driver.implicitly_wait(2)
driver.get("https://www.etoos.com/member/login.asp?returnUrl=http://247.etoos.com/lms/index.do")


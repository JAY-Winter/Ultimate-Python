import requests
from bs4 import BeautifulSoup

session = requests.session()

url = "https://www.etoos.com/member/login.asp?returnUrl=http://ilsandonggu247.etoos.com/lms/index.do"

data = {
    "mem_id" : "ilsan247",
    "pwdtmp" : "isd151208^^"

}


response = session.get(url)

print(response.status_code)




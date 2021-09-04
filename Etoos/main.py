
from Etoos import Etoos

Etoos.login()

while True :

    Major = Etoos.selectMajor()

    day_list = Etoos.countDay()

    Input_day = Etoos.selectDay(day_list)

    total_page = Etoos.countTotalPage()
    
    Etoos.crawlingQuestion(total_page, Major, Input_day)

    isAdded = Etoos.addSelectMajor()
    
    if isAdded == False:
        break 
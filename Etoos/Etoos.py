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

        day_list = []

        for week in range(6) : 

            days = driver.find_elements_by_css_selector("#math_day > td:nth-child({}) > div > strong".format(week+1))

            for day in range(5) :                     
                try : 

                    Find_day = days[day].text
                    # Find_day_key = days[day]
                    day_list.append(Find_day)

                except : 
                    pass

                finally : 
                    print(day_list)
                

        Input_day = input("희망하는 날짜를 입력하세요. ex) 07 / 01 : ")

        for i in range(len(day_list)) : 

            if Input_day == Find_day[i] : 
                # days[day].click()
                # print(By.cssSelector(days[day]))
                # Find_day_key.click()
                print("확인!")
                # return Etoos.CountDay()

            # elif type(Input_day) == str : 
            #     print("올바른 날짜를 입력해주세요.")
            #     return Etoos.CountDay()
            
            # elif len(Input_day) != 7 :
                # print("올바른 날짜를 입력해주세요.")
                # return Etoos.CountDay()

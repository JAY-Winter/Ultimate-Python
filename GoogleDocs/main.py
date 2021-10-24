from operator import index
import os.path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import natsort

SCOPES = [    
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file", 
]

document_id = "1lqxaQvncxOIOONhIEHNbbDJnMS2Xt2swCxSiHRz0zJ4"


if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

service = build("docs", "v1", credentials=creds)

def main() :

    input_day = "10_20"
    # subject =   ["기하1", "미적1", "확통1", "기하2", "미적2", "확통2"]
    subject =  ["(1)","(2)","(3)","(4)","(5)","(6)"]
    subject_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/{input_day}"
    subject_file_list = os.listdir(subject_path)
    subject_file_list.remove(".DS_Store")
    subject_file_list.sort()
    sorted_subject_file_list = natsort.natsorted(subject_file_list)
        
    print("데일리 테스트 시험지 작성 시작")

    function_lotation = 1
    point = 0 

    while 1 <= function_lotation < 8 :
        # 새로운 페이지가 생성되면 그 페이지의 첫 번째로 가야함
        # for i 문에 index_location = 1 을 선언했을 때
        # 첫 번째 페이지의 첫 번째 index 로 삽입됨
        # for i 문이 돌 때마다 새롭게 생기는 페이지의 1번째 index 로 들어가야함

        index_location = 1
    
        for i in range( len(subject) ) :
        
            n = 1
            
            for j in range( point, len(sorted_subject_file_list) ) :
                
                subject_name_in_file_list = sorted_subject_file_list[j][0:3]

                if subject[i] == subject_name_in_file_list :

                    urls = f"https://etoos-dailytest-storage.s3.ap-northeast-2.amazonaws.com/수학/{input_day}/{sorted_subject_file_list[j]}"

                    requests = [{
                        "insertInlineImage": {
                            "location": {"index": index_location},
                            "uri": urls ,
                        }
                    }]

                    body = {"requests": requests}

                    response = service.documents().batchUpdate(documentId=document_id, body=body).execute()

                    print(f"""
                    {sorted_subject_file_list[j]}번 삽입 완료
                    """)
                    print(f"{index_location}")
                    n += 1
                    point += 1
                    index_location += 1

                else :
                # 과목 명이 다를 때 새로운 페이지 생성
                    print("새로운 페이지 생성") 
                    print(f"{index_location}")
                    # requests = [{
                    #     "insertPageBreak" : {
                            
                    #         "endOfSegmentLocation" : {}
                    #     }
                    #     }]

                    requests = [{
                        
                        "insertPageBreak" : {
                            "location" : {
                                "index" : index_location
                            }
                        },

                        # "insertText" :{
                        #     "text" : "<{subject}>",
                        #     "location" : {
                        #         "index" : index_location+1
                        #     }
                        # }

                        }]

                    textRequests = {

                            "insertText" :{

                                "text" : "<subject>",

                                "location" : {
                                    "index" : index_location+1
                                }
                            }
                            
                        }
                    requests.append(textRequests)
                    body = {"requests": requests}

                    response = service.documents().batchUpdate(documentId=document_id, body=body).execute()
                    

                    index_location += 2
                    break

            # 반복문 i 끝났을 때
            function_lotation += 1

    return print("""
프로그램을 종료합니다.
문의 : ETOOS247 일산동구점 정재현
""")




main()
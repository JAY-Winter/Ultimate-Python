import os.path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = [    
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file", 
]

document_id = '1lqxaQvncxOIOONhIEHNbbDJnMS2Xt2swCxSiHRz0zJ4'


if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('docs', 'v1', credentials=creds)

def main() :

    input_day = "10_20"
    # subject =   ["기하1", "미적1", "확통1", "기하2", "미적2", "확통2"]
    subject =  ["(1)","(2)","(3)","(4)","(5)","(6)"]
    subject_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/{input_day}"
    subject_file_list = os.listdir(subject_path)
    subject_file_list.remove(".DS_Store")
    subject_file_list.sort()
    
    print("데일리 테스트 시험지 작성 시작")

    function_lotation = 1
    point = 0 

    while 1 <= function_lotation < 8 :
        
        index_location = 1

        for i in range( len(subject) ) :
        
            n = 1
            
            for j in range( point, len(subject_file_list) ) :
                
                subject_name_in_file_list = subject_file_list[j][0:3]
                print(subject_name_in_file_list)
                if subject[i] == subject_name_in_file_list :

                    urls = f'https://etoos-dailytest-storage.s3.ap-northeast-2.amazonaws.com/수학/{input_day}/{subject_file_list[j]}'

                    requests = [{

                        'insertInlineImage': {

                            'location': {'index': index_location},
                            'uri': urls ,

                        }
                    }]

                    body = {'requests': requests}

                    response = service.documents().batchUpdate(
                        documentId=document_id, body=body).execute()

                    insert_inline_image_response = response.get('replies')[0].get(
                        'insertInlineImage')

                    print(f"""
                    구글 docs 데일리테스트 {subject_file_list[j]}번 삽입 완료
                    """)

                    n += 1
                    point += 1
                    index_location += 1

                elif subject[i] != subject_name_in_file_list :
                # 과목 명이 다를 때 새로운 페이지 생성
                    print("새로운 페이지 생성") 

                    requests = [{

                        'insertPageBreak' : {
                            
                            'endOfSegmentLocation' : {}
                        }
                        }]

                    body = {'requests': requests}

                    response = service.documents().batchUpdate(
                    documentId=document_id, body=body).execute()

                    insert_page_break_response = response.get('replies')[0].get(
                    'insertPageBreak')

                    break


            # 반복문 i 끝났을 때
            function_lotation += 1





main()
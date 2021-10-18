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

    input_day = "10_15"
    subject =  ["기하1", "미적1", "확통1", "기하2", "미적2", "확통2"]
    subject_path = f"/Applications/mampstack-8.0.3-1/apache2/htdocs/jay/Git/GIT/Python/Ultimate-Python/Etoos/수학/{input_day}"
    subject_file_list = os.listdir(subject_path)
    subject_file_list.sort()
    
    print("데일리 테스트 시험지 작성 시작")

    lotation = 1
    location = 1

    while 1 <= lotation < 8 :

        for i in range( len(subject) ) :

            n = 1

            for j in range( len(subject_file_list) ) :

                location += 1
                subject_name_in_file_list = subject_file_list[j][0:3]

                if subject[i] == subject_name_in_file_list :

                    urls = f'https://etoos-dailytest-storage.s3.ap-northeast-2.amazonaws.com/수학/{input_day}/{subject[i]}_문제{n}번.PNG'

                    requests = [{

                        'insertInlineImage': {

                            'location': {'index': location},
                            'uri': urls ,

                        }
                    }]

                    body = {'requests': requests}

                    response = service.documents().batchUpdate(
                        documentId=document_id, body=body).execute()

                    insert_inline_image_response = response.get('replies')[0].get(
                        'insertInlineImage')

                    print(f"""
                    구글 docs 데일리테스트 {subject[i]}_문제{n}번 삽입 완료
                    Inserted image with object ID: {insert_inline_image_response.get('objectId')}
                    """
                        )

                    n += 1

                else :

                    continue

            #페이지 새로 생성
            lotation += 1





main()
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# 아래 코드는 token.json 생성 코드

# If modifying these scopes, delete the file token.json.
SCOPES = [    
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file", 
]
# only read 만  제공

# The ID of a sample document.
DOCUMENT_ID = '569415776417-ikohr1do82g3gi0ehqo1d8bkk9fa2fpl.apps.googleusercontent.com'
# OAuth client ID 입력

def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    # 초기 credentials 상태는 none

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    # 경로에 token.json 이 있으면 creds = Credentials 모듈에서 from_authorized_user_file method 
    # Creates a Credentials instance from an authorized user json file.
    # 즉, 사용자화 user json file 에서 credntials instance 를 생성한다
    # SCOPES 내에서만 유효한?

    if not creds or not creds.valid:
        # creds 가 없거나 or 유효하지 않을 때

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print('The title of the document is: {}'.format(document.get('title')))


if __name__ == '__main__':
    main()
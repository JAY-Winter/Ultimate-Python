from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

service = build('drive', 'v3')

nested_collection = service.featured().stamps()


with build('drive', 'v3') as service : 



    try : 
        response = request.execute()

    except HttpError as e:
        print('Error response status code :{0}, reason : {1}'.format(e.status_code, e.error_details))

        
import json
from re import S

import cv2
from dotenv import load_dotenv
from itsdangerous import exc
import requests
import sys

import os

from sklearn.feature_extraction import image


LIMIT_PX = 2048
LIMIT_BYTE = 2048*2048  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

    #     # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        cv2.imwrite(image_path, image)

        return image_path
    return image_path


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'


    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()


    return requests.post(API_URL, headers=headers, files={"image": data})


def main():

    load_dotenv()
    API_KEY = os.environ.get("API_KEY")
    appkey = API_KEY

    # image folder
    image_folder_path = "/Users/heyon/Desktop/JAY/Jay-Thomas-code/Project/ETOOS_OCR/image"
    image_folder_list = os.listdir(image_folder_path)
    image_folder_list.sort()    # 현재 image_folder 배열형태 - 순서대로 나열되어있는 형태
    
    saved_image_folder_path = "/Users/heyon/Desktop/JAY/Jay-Thomas-code/Project/ETOOS_OCR/saved_image"  # 이름 변경된 사진이 저장될 폴더

    date = input("이름 앞에 붙을 날짜를 입력해주세요(ex. 20220701) : " )

    for image in range(1, len(image_folder_list), 2) : 
        
        image_path = f"{image_folder_path}/{image_folder_list[image]}"  # image file 의 경로가 들어와야함
        print(f"image_path : {image_path}")
        resize_impath = kakao_ocr_resize(image_path)
        
        if resize_impath is not None:
            image_path = resize_impath

        output = kakao_ocr(image_path, appkey).json()

        OCR_result = output['result'][7] # 현재 8번 째 property 가 이름 value을 갖고있음 > 양식 수정함에 따라서 바뀐 위치 확인해야함
        print(OCR_result)

        student_name = OCR_result['recognition_words'][0]   # OCR_result.json file 중 0번째 index 가 이름 value
        print(student_name)

        os.rename((f"{image_folder_path}/{image_folder_list[image]}"), f"{saved_image_folder_path}/{date} {student_name}.jpg")
        os.rename((f"{image_folder_path}/{image_folder_list[image+1]}"), f"{saved_image_folder_path}/{date} {student_name}(1).jpg")



if __name__ == "__main__":
    main()


## Issue
# - OCR_result, 즉 이름 index 의 위치가 파일마다 다를 수가 있다
# > 데일리 플래너 틀 수정 필요함

# - 앞 페이지 : 이름1, 뒷 페이지 : 이름2 어떻게 해야할까

# - 중복 이름 어떻게 해야할까

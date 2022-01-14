import json

import cv2
import requests
import sys

import os


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
        image_path = "{}_resized.jpg".format(image_path)
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
    # if len(sys.argv) != 3:
        # print("Please run with args: $ python example.py /path/to/image appkey")
    argv = ["/Users/heyon/Desktop/JAY/Jay-Thomas-code/Project/ETOOS_OCR/image/2022_000.jpg", "d15d88de56c4ec36b2466e0ee817ace0"]
    image_path, appkey = argv[0], argv[1]

    image_folder = []


    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, appkey).json()
    # print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)))
    print(output['result'][9])
    # print(output)
    json_result = output['result'][9]

    json_name = json_result['recognition_words'][0]

    old_file_name = image_path[-3:]

    file_name = {json_name : old_file_name}


    re_name = os.rename(image_path, json_name+".jpg")
    

if __name__ == "__main__":
    main()


## Issue
# - json_result, 즉 이름 index 의 위치가 파일마다 다를 수가 있다
# > 데일리 플래너 틀 수정 필요함

# - 앞 페이지 : 이름1, 뒷 페이지 : 이름2 어떻게 해야할까

# - 중복 이름 어떻게 해야할까

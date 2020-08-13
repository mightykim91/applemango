# -*- coding: utf-8 -*- 
from PIL import Image
from pytesseract import *
import re
import cv2
from skimage import io  # url 이미지 읽는 라이브러리
import os



def Text_Filtering_jpg(res):
    file_path = './insta_tmp_image/'
    # [1] url로 온 모든 이미지 저장
    j = 0
    for food_info in res:
        if len(food_info) > 0:
            img_url = food_info[0]
            input_path = file_path + "input_img%d.jpg" % j
            try:
                wget.download(img_url, input_path)
                j += 1
            except:
                print("url error")

    for file in os.scandir(file_path):
        img = cv2.imread(file.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img ,lang='kor')
        if len(text) > 3:
            os.remove(file.path)

def Text_Filtering_url(res):
    tmp_res = []
    for food_info in res:
        img_url = food_info[0]
        img = cv2.imread(img_url)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img ,lang='kor')
        if len(text) > 3:
            print("텍스트 필터링된 url")
            print(img_url)
        else:
            tmp_res.append(food_info)

    return tmp_res

urll=[["https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/117263714_216146473155101_2596481953184265637_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=e9bm-0ZFGq4AX-9ehrp&oh=53a72450879e959d6b362b6c110cbdea&oe=5F5EBD72"]]
Text_Filtering_url(urll)
# categories = ["jjajangmyeon" ,"lamyeon", "donkkaseu", "udong" ,"paseuta", "gimbab", "samgyeobsal", "jjamppong", "chikin", "pija", "jogbal", "bossam", "tteogbokk-i", "sundaegugbab", "janchigugsu", "tangsuyug"]
# categories = ["jogbal", "bossam", "tteogbokk-i", "sundaegugbab", "janchigugsu", "tangsuyug"]

# for categorie in categories:
#     print(categorie)
#     Text_Filtering_jpg(categorie)
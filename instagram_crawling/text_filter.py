from PIL import Image
from pytesseract import *
import re
import cv2
from skimage import io  # url 이미지 읽는 라이브러리
import os



def Text_Filtering_jpg(categorie):
    groups_folder_path = "./cnn_sample/"
    file_path = groups_folder_path + categorie + '/'

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
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img ,lang='kor')
        if len(text) > 3:
            print("텍스트 필터링된 url")
            print(img_url)
        else:
            tmp_res.append(food_info)

    return tmp_res
# categories = ["jjajangmyeon" ,"lamyeon", "donkkaseu", "udong" ,"paseuta", "gimbab", "samgyeobsal", "jjamppong", "chikin", "pija", "jogbal", "bossam", "tteogbokk-i", "sundaegugbab", "janchigugsu", "tangsuyug"]
# categories = ["jogbal", "bossam", "tteogbokk-i", "sundaegugbab", "janchigugsu", "tangsuyug"]

# for categorie in categories:
#     print(categorie)
#     Text_Filtering_jpg(categorie)
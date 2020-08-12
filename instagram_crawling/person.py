# # 사람 filter
# import cv2
# import numpy as np
# from os import listdir
# from os.path import isfile, join
# # 테스트 이미지 불러오기
# mypath='./cnn_sample/'
# path = './data/haarcascades'

# onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]

# personfiles = ['haarcascade_eye.xml', 'haarcascade_eye_tree_eyeglasses.xml', 'haarcascade_frontalcatface.xml', 'haarcascade_frontalcatface_extended.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_fullbody.xml', 'haarcascade_lefteye_2splits.xml', 'haarcascade_lowerbody.xml', 'haarcascade_profileface.xml', 'haarcascade_righteye_2splits.xml', 'haarcascade_russian_plate_number.xml', 'haarcascade_upperbody.xml']

# for i in onlyfiles:
#     image = cv2.imread('./image/'+i)
#     image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     for p in personfiles:

#         person_cascade = cv2.CascadeClassifier('./data/haarcascades/' + p)
#         person = person_cascade.detectMultiScale(image_gray, 1.3, 5)
#         # print(person,p)
#         if len(person) != 0:
#             break
#     # print("사람입니다.")
#     cv2.imshow('img',image) # 이미지 띄우기
#     cv2.waitKey(0)          
#     cv2.destroyAllWindows() # 윈도우 종료


###################################################################################
# 2. 사람 filter
###################################################################################
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from skimage import io  # url 이미지 읽는 라이브러리
from urllib.request import urlopen


def person_filter(res_url_menu):
    # 테스트 이미지 불러오기
    # root_path='./cnn_sample/'
    path = './data/haarcascades'
    personfiles = ['haarcascade_eye_tree_eyeglasses.xml', 'haarcascade_frontalcatface.xml', 'haarcascade_frontalcatface_extended.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_fullbody.xml', 'haarcascade_lefteye_2splits.xml', 'haarcascade_lowerbody.xml', 'haarcascade_profileface.xml', 'haarcascade_righteye_2splits.xml', 'haarcascade_russian_plate_number.xml', 'haarcascade_upperbody.xml']
    # personfiles = ['haarcascade_eye.xml', 'haarcascade_eye_tree_eyeglasses.xml', 'haarcascade_frontalcatface.xml', 'haarcascade_frontalcatface_extended.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_fullbody.xml', 'haarcascade_lefteye_2splits.xml', 'haarcascade_lowerbody.xml', 'haarcascade_profileface.xml', 'haarcascade_righteye_2splits.xml', 'haarcascade_russian_plate_number.xml', 'haarcascade_upperbody.xml']
    rm_list = []
    L = len(res_url_menu)
    for i in range(L):
        url = res_url_menu[i][0]
        menu = res_url_menu[i][1]
        try:
            image = io.imread(url)  # skimage.io 를 이용한 url 이미지 불러오기
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for p in personfiles:
                person_cascade = cv2.CascadeClassifier('./data/haarcascades/' + p)
                person = person_cascade.detectMultiScale(image_gray, 1.3, 5)
                if len(person) != 0:
                    rm_list.append(i)
                    print(p)
                    print("사람입니다.")
                    break
        except:
            rm_list.append(i)
            print("url error!!!!!")
    
    rm_list.sort(reverse=True)
    for idx in rm_list:
        obj = res_url_menu[idx]
        res_url_menu.remove(obj)
    # print(res_url_menu)
    return res_url_menu

# tmp = []
# tmp1 = []
# res_url = ["http://res.heraldm.com/phpwas/restmb_jhidxmake.php?idx=5&simg=201810041148404470367_20181004115111_01.jpg",
# "https://i.pinimg.com/originals/db/02/72/db0272819238616e457b94d6d0f161a5.jpg",
# "https://i.ytimg.com/vi/GWoVIwoU92U/maxresdefault.jpg","https://cdn.crowdpic.net/detail-thumb/thumb_d_97EEEC2FC54D14B6C66BF2009DD4C949.jpg",
# "https://th.bing.com/th/id/OIP.bahHgIwvNhMm8OdKVtNZhAHaEI?pid=Api&rs=1",
# "https://freshdon.com/wp-content/uploads/2018/06/%EB%B6%88%EA%B0%88%EB%B9%84%EB%8F%88%EA%B9%8C%EC%8A%A4%EB%A9%94%EC%9D%B82.jpg"
# ,"https://i.ytimg.com/vi/cJl-vN_yNc8/maxresdefault.jpg"]

# res_menu = [str(i) for i in range(len(res_url))]
# for i in range(len(res_url)):
#     tmp = []
#     tmp.append(res_url[i])
#     tmp.append(res_menu[i])
#     tmp1.append(tmp)
# print(tmp1)
# person_filter(tmp1)
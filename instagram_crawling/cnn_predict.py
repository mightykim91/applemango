import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
import wget

ca = ["jjajangmyeon", "lamyeon", "donkkaseu" ,"udong" ,"paseuta", "gimbab" ,"samgyeobsal" ,"jjamppong", "chikin" ,"pija", "jogbal", "bossam", "tteogbokk-i", "sundaegugbab" ,"janchigugsu" ,"tangsuyug"]
def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)

####################################################################################
# 1. 기존의 훈련된 모델인 bingforcnn과 비교하면서 이미지 분류
####################################################################################
def Predict(src_list, menu):
    file_path = './insta_tmp_image/'
    # [1] url로 온 모든 이미지 저장
    j = 0
    for url in src_list:
        if len(url) > 0:
            input_path = file_path + "input_img%d.jpg" % j
            try:
                wget.download(url, input_path)
                j += 1
            except:
                print("url error")
    
    # [2] 이미지를 예측하기 위한 input 데이터셋으로 다시 만듬
    src = []
    name = []
    test = []
    image_dir = "./insta_tmp_image/"
    for file in os.listdir(image_dir):
        if (file.find('.jpg') is not -1):
            src.append(image_dir + file)
            name.append(file)
            test.append(Dataization(image_dir + file))

    # [3] 만든 데이터셋을 모델과 비교하면서 이미지 분류
    test = np.array(test)
    model = load_model('bingforcnn.h5')
    predictions = model.predict(test)   # 확률을 제공
    # predict = model.predict_classes(test) # 클래스 레이블을 제공
    # print("===============================")
    # print(src_list)
    # print(menu)
    # print(len(test))
    res_url_menu = []
    for i in range(len(src_list)):
        print(np.max(predictions[i]))
        if np.max(predictions[i]) >= 0.9:
            tmp = []
            num = np.argmax(predictions[i])
            # print(name[i],"의 음식분류는 ",menu[num])
            tmp.append(src_list[i])
            tmp.append(menu[num])
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print(src_list[i])
            # print((menu[num]))
            # print(ca[num])
            # tmp.append(num)
            res_url_menu.append(tmp)

    # [4] insta_tmp_image폴더에 있는 모든 이미지 파일 지우기
    if os.path.exists(file_path):
        for file in os.scandir(file_path):
            os.remove(file.path)

    return res_url_menu

# q = ["https://t1.daumcdn.net/cfile/tistory/9933463B5CF6FA2821", "https://i.imgur.com/D2T8R2T.jpg","https://contents.sixshop.com/thumbnails/uploadedFiles/39154/default/image_1576811394455_1000.png","https://economy.donga.com/IMAGE/2017/04/14/83849831.3.jpg", "https://i1.wp.com/sharehows.com/wp-content/uploads/2019/07/0-%EC%8D%B8%EB%84%A4%EC%9D%BC.jpg?fit=800%2C400","https://cdn.crowdpic.net/detail-thumb/thumb_d_E8713DEDB7067CF98E30AA6683D7FE29.jpg","https://recipe1.ezmember.co.kr/cache/recipe/2018/01/08/8ae1b5468ae886aeb17ca81d0f18fc4a1.jpg"]
# categories = ['donkkaseu', 'jjajangmyeon',"asdqw"]
# res_url_menu = Predict(q,categories)
# print(res_url_menu)
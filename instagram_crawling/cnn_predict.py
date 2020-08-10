import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
import wget


def Dataization(img_path):
    image_w = 28
    image_h = 28
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/256)
 
def Predict(src_list):
    # [1] url로 온 모든 이미지 저장
    file_path = './insta_tmp_image/'
    for i, url in enumerate(src_list):
        if len(url) > 0:
            input_path = file_path + "input_img%d.jpg" % i
            try:
                wget.download(url, input_path)
            except:
                print("url error")
    
    # [2] 저장된 이미지 비교
    src = []
    name = []
    test = []
    image_dir = "./insta_tmp_image/"
    for file in os.listdir(image_dir):
        if (file.find('.jpg') is not -1):      
            src.append(image_dir + file)
            name.append(file)
            test.append(Dataization(image_dir + file))
    
    test = np.array(test)
    model = load_model('Gersang.h5')
    predictions = model.predict(test)
    predict = model.predict_classes(test)
    res = []
    for i in range(len(test)):
        if np.max(predictions[i]) >= 0.9:
            res.append(src_list[i])
            # print(name[i] + " : , Predict : "+ str(categories[predict[i]])) # 메뉴이름 추출
    
    if os.path.exists(file_path):
        for file in os.scandir(file_path):
            os.remove(file.path)
            
    return res

    
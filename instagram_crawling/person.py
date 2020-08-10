# 사람 filter
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
# 테스트 이미지 불러오기
mypath='./cnn_sample/'
path = './data/haarcascades'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]

personfiles = ['haarcascade_eye.xml', 'haarcascade_eye_tree_eyeglasses.xml', 'haarcascade_frontalcatface.xml', 'haarcascade_frontalcatface_extended.xml', 'haarcascade_frontalface_alt.xml', 'haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_alt_tree.xml', 'haarcascade_frontalface_default.xml', 'haarcascade_fullbody.xml', 'haarcascade_lefteye_2splits.xml', 'haarcascade_lowerbody.xml', 'haarcascade_profileface.xml', 'haarcascade_righteye_2splits.xml', 'haarcascade_russian_plate_number.xml', 'haarcascade_upperbody.xml']

for i in onlyfiles:
    image = cv2.imread('./image/'+i)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for p in personfiles:

        person_cascade = cv2.CascadeClassifier('./data/haarcascades/' + p)
        person = person_cascade.detectMultiScale(image_gray, 1.3, 5)
        # print(person,p)
        if len(person) != 0:
            break
    # print("사람입니다.")
    cv2.imshow('img',image) # 이미지 띄우기
    cv2.waitKey(0)          
    cv2.destroyAllWindows() # 윈도우 종료

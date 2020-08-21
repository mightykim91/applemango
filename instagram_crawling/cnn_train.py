# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
import os, re, glob
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model
import cv2
import time

from menu import find_name

start = time.time()
ko_foods = list(input("음식명:").split())
foods = find_name(ko_foods)
print("foods ==>", foods)
####################################################################################
# 1. 이미지 파일을 학습을 위한 데이터셋 생성
####################################################################################
# 데이터용량을 줄기위해 크기조절
num_classes = len(foods)

image_w = 28
image_h = 28
X = []
Y = []
for idex, food in enumerate(foods):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    # image_dir : 해당 이미지의 경로를 불러옴
    image_dir = './cnn_sample/' + food + '/'
    print(image_dir)
    e = 0
    for top, dir, files in os.walk(image_dir):
        for filename in files:
            if os.path.splitext(filename)[1].lower() == '.jpg':
                try:
                    img = cv2.imread(image_dir+filename)
                    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
                    X.append(img/256)
                    Y.append(label)
                except:
                    e+=1
                    print("학습 이미지 에러 발생")
                    print(food,"의 ",filename)
    print('에러발생횟수 : ',e)


X = np.array(X)
Y = np.array(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)
# dataset_name = "./model_and_datasets/datasets/" + food
# print(dataset_name)
np.save("./img_datas.npy", xy)

####################################################################################
# 2. CNN 알고리즘 => dataset을 이용용하여 학습을 시켜 모델을 만든다.
####################################################################################
    # 저장된 dastaset을 바로 불러와 학습진행

X_train, X_test, Y_train, Y_test = np.load("./img_data.npy")

model = Sequential()
model.add(Convolution2D(16, 3, 3, border_mode='same', activation='relu',
                        input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3,  activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,activation = 'softmax'))

model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=32, epochs=30)
# model_name = "./model_and_datasets/model/" + food + "_model.h5"
model.save('newbingforcnns.h5')

print("모든 학습을 위한 걸린시간은 ",time.time()-start,"초 입니다.")
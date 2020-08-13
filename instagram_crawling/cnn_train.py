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
start = time.time()
# categories = ["ganjang-gejang","donkkaseu","doenjangjjigae","ramyeon","miyeoggug",
#             "bossam","sundaegugbab","jogbal","jjajangmyeon","jjamppong","paseuta"]

# categories = list(input("영어 음식명:").split())
# print("categories ==>", categories)
####################################################################################
# 1. 이미지 파일을 학습을 위한 데이터셋 생성
####################################################################################
# 데이터용량을 줄기위해 크기조절
groups_folder_path = './cnn_sample/'
categories = os.listdir(groups_folder_path)
print(categories)
num_classes = len(categories)

image_w = 28
image_h = 28

X = []
Y = []

for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'
    for top, dir, files in os.walk(image_dir):
        for filename in files:
            if os.path.splitext(filename)[1].lower() == '.jpg':
                try:
                    img = cv2.imread(image_dir+filename)
                    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
                    X.append(img/256)
                    Y.append(label)
                except:
                    print("학습 이미지 에러 발생")
                    print(categorie,"의 ",filename)
X = np.array(X)
Y = np.array(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save("./img_data.npy", xy)

####################################################################################
# 2. CNN 알고리즘 => 학습을 시켜 모델을 만든다.
####################################################################################

X_train, X_test, Y_train, Y_test = np.load('./img_data.npy')

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
model.save('bingforcnn.h5')
print("학습을 위한 걸린시간은 ",time.time()-start,"초 입니다.")